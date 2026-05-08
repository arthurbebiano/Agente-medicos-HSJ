"""
SADC - Sistema de Apoio à Decisão Clínica
Hospital Geral São José - Contagem/MG
Arquivo único: app.py
"""

import streamlit as st
import hashlib
import base64
import json
import re
import time
from typing import Optional

# ─────────────────────────────────────────────
# CONFIGURAÇÃO DA PÁGINA (deve ser 1ª chamada)
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="SADC | HGS José",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────
# CSS GLOBAL – tema dark premium
# ─────────────────────────────────────────────
GLOBAL_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Syne:wght@400;600;700;800&family=Inter:wght@300;400;500&display=swap');

:root {
  --bg:       #0a0d14;
  --surface:  #111520;
  --card:     #161c2d;
  --border:   #1e2a42;
  --accent:   #3b82f6;
  --accent2:  #6366f1;
  --danger:   #ef4444;
  --success:  #10b981;
  --warn:     #f59e0b;
  --text:     #e2e8f0;
  --muted:    #64748b;
  --mono:     'DM Mono', monospace;
  --sans:     'Inter', sans-serif;
  --head:     'Syne', sans-serif;
}

html, body, [data-testid="stAppViewContainer"] {
  background: var(--bg) !important;
  color: var(--text) !important;
  font-family: var(--sans) !important;
}

/* Ocultar menu padrão do Streamlit */
#MainMenu, footer, header { visibility: hidden; }

/* Sidebar */
[data-testid="stSidebar"] {
  background: var(--surface) !important;
  border-right: 1px solid var(--border) !important;
}
[data-testid="stSidebar"] * { color: var(--text) !important; }

/* Inputs */
[data-testid="stTextInput"] input,
[data-testid="stTextArea"] textarea,
[data-testid="stSelectbox"] select,
.stSelectbox > div > div {
  background: var(--card) !important;
  border: 1px solid var(--border) !important;
  color: var(--text) !important;
  border-radius: 8px !important;
  font-family: var(--sans) !important;
}
[data-testid="stTextInput"] input:focus,
[data-testid="stTextArea"] textarea:focus {
  border-color: var(--accent) !important;
  box-shadow: 0 0 0 2px rgba(59,130,246,0.25) !important;
}

/* Botões */
.stButton > button {
  background: linear-gradient(135deg, var(--accent), var(--accent2)) !important;
  color: #fff !important;
  border: none !important;
  border-radius: 10px !important;
  font-family: var(--head) !important;
  font-weight: 600 !important;
  letter-spacing: .04em !important;
  padding: 0.55rem 1.4rem !important;
  transition: transform .15s, box-shadow .15s !important;
}
.stButton > button:hover {
  transform: translateY(-2px) !important;
  box-shadow: 0 8px 20px rgba(59,130,246,.4) !important;
}

/* Expander */
[data-testid="stExpander"] {
  background: var(--card) !important;
  border: 1px solid var(--border) !important;
  border-radius: 10px !important;
}

/* Chat */
[data-testid="stChatMessage"] {
  background: var(--card) !important;
  border: 1px solid var(--border) !important;
  border-radius: 10px !important;
  margin-bottom: .5rem !important;
}

/* Scrollbar */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: var(--border); border-radius: 3px; }

/* Labels */
label, .stSelectbox label, .stTextInput label, .stTextArea label {
  color: var(--muted) !important;
  font-size: .78rem !important;
  letter-spacing: .06em !important;
  text-transform: uppercase !important;
  font-family: var(--mono) !important;
}

/* Radio */
[data-testid="stRadio"] label { text-transform: none !important; font-size: .9rem !important; }

/* Metric */
[data-testid="stMetric"] { background: var(--card); border: 1px solid var(--border); border-radius: 10px; padding: 1rem; }
</style>
"""

LANDING_CSS = """
<style>
.lp-wrap {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: radial-gradient(ellipse 80% 60% at 50% -10%, rgba(59,130,246,.18) 0%, transparent 70%),
              radial-gradient(ellipse 50% 40% at 90% 90%, rgba(99,102,241,.12) 0%, transparent 60%),
              #0a0d14;
  font-family: 'Inter', sans-serif;
}
.lp-card {
  width: 420px;
  background: rgba(22,28,45,.85);
  border: 1px solid rgba(59,130,246,.25);
  border-radius: 20px;
  padding: 3rem 2.5rem 2.5rem;
  backdrop-filter: blur(20px);
  box-shadow: 0 32px 80px rgba(0,0,0,.6), 0 0 0 1px rgba(255,255,255,.04) inset;
  text-align: center;
}
.lp-logo {
  width: 64px; height: 64px;
  background: linear-gradient(135deg, #3b82f6, #6366f1);
  border-radius: 18px;
  display: inline-flex; align-items: center; justify-content: center;
  font-size: 2rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 8px 24px rgba(59,130,246,.4);
}
.lp-title {
  font-family: 'Syne', sans-serif;
  font-size: 1.6rem; font-weight: 800;
  color: #e2e8f0;
  margin: 0 0 .3rem;
  letter-spacing: -.02em;
}
.lp-subtitle {
  font-size: .82rem; color: #64748b;
  margin: 0 0 2rem;
  line-height: 1.5;
}
.lp-badge {
  display: inline-block;
  background: rgba(239,68,68,.12);
  border: 1px solid rgba(239,68,68,.3);
  color: #fca5a5;
  font-size: .7rem;
  padding: .25rem .65rem;
  border-radius: 999px;
  font-family: 'DM Mono', monospace;
  letter-spacing: .08em;
  margin-bottom: 1.8rem;
}
.lp-divider {
  border: none; border-top: 1px solid rgba(255,255,255,.06);
  margin: 1.5rem 0;
}
.lp-footer {
  font-size: .72rem; color: #374151;
  margin-top: 1.5rem;
}
</style>
"""

# ─────────────────────────────────────────────
# SYSTEM PROMPT – contexto hospitalar rígido
# ─────────────────────────────────────────────
SYSTEM_PROMPT = """Você é o SADC (Sistema de Apoio à Decisão Clínica) do Hospital Geral São José, situado em Contagem, MG.
Você auxilia o médico plantonista no Pronto Atendimento de Clínica Médica.

=== CONTEXTO INSTITUCIONAL IMPERATIVO ===
Recursos EXTREMAMENTE LIMITADOS. NUNCA ignore isso:

EQUIPE MÉDICA: Apenas 1 Clínico Geral, 1 Pediatra, 1 Cirurgião Geral no plantão.

INTERNAÇÃO: Capacidade QUASE ZERO. Priorize SEMPRE: alta com orientações, observação rápida (<12h) ou transferência/encaminhamento. Internação é ÚLTIMO recurso.

LABORATÓRIO DISPONÍVEL APENAS:
  - Troponina
  - EAS (Urina Tipo 1)
  - Gasometria Arterial/Venosa (com eletrólitos: Na, K, Cl, HCO3, Lactato, pH, pCO2, pO2, BE, SatO2)
  NÃO HÁ: hemograma, PCR, creatinina isolada, lipase, bilirrubinas, coagulograma, TSH, β-HCG, culturas.
  Não solicite exames que não existem. Se precisar justificar uma transferência, mencione o exame como necessidade na unidade de destino.

IMAGEM DISPONÍVEL:
  - Radiografia (tórax, abdome, ossos)
  - Tomografia computadorizada SEM contraste
  - ECG (o próprio clínico deve laudar)
  NÃO HÁ: USG, RM, TC COM contraste, ecocardiograma.

MEDICAÇÕES: Foque em medicamentos de referência do SUS/RENAME, disponíveis em PA de periferia. Evite medicações de alto custo, uso exclusivo hospitalar de referência ou que requeiram UTI para administração.

=== FORMATO DE SAÍDA OBRIGATÓRIO ===
Responda SEMPRE em XML com as tags abaixo quando for avaliação inicial ou complemento:

<visao_geral>Resumo clínico em 2-3 frases. Impacto clínico imediato.</visao_geral>

<sit_box>SITUAÇÃO: [frase curta descrevendo o cenário clínico atual]</sit_box>

<hma_box>HMA formatada em prosa clínica. Inclua: queixa principal, tempo de evolução, caracterização dos sintomas, fatores de melhora/piora, sintomas associados, investigação prévia.</hma_box>

<hpp_box>HPP/Antecedentes: doenças crônicas, cirurgias, alergias, medicações em uso contínuo.</hpp_box>

<exame_fisico_box>Exame Físico sistematizado: estado geral, sinais vitais com interpretação, sistemas relevantes.</exame_fisico_box>

<exames_complementares_box>Exames prévios relevantes com interpretação clínica.</exames_complementares_box>

<hd_box>
HD Principal: [hipótese mais provável com justificativa clínica breve]
HDs Secundárias:
  1. [hipótese 2]
  2. [hipótese 3]
Diagnósticos a excluir: [urgências que NÃO podem ser perdidas com base nos recursos disponíveis]
</hd_box>

<meds_intra_box>
MEDICAÇÕES A ADMINISTRAR NO PA:
Para cada medicação:
  - Droga: [nome]
  - Dose: [dose exata em mg/mcg/etc]
  - Via: [IV/IM/VO/SC/SL/Inalatória]
  - Posologia: [frequência e duração no PA]
  - Preparo e Administração: [diluição exata, volume, tempo de infusão ou gotas/minuto se gravitacional, observações de segurança]
</meds_intra_box>

<exames_intra_box>
EXAMES SOLICITADOS NO PA:
Para cada exame:
  - Exame: [nome]
  - Justificativa: [1 linha resumindo o caso e por que esse exame muda a conduta]
</exames_intra_box>

<encaminhamento_box>
RESUMO PARA TRANSFERÊNCIA/ENCAMINHAMENTO:
Paciente: [nome], [idade], [sexo]
Motivo da transferência: [diagnóstico/suspeita]
Resumo clínico: [HMA condensada, vitais, achados relevantes]
Conduta realizada no HGS José: [meds e exames feitos]
Necessidade na unidade de destino: [o que precisa que não temos]
Condição de transferência: [estável/instável, via aérea ou terrestre sugerida]
</encaminhamento_box>

<receita_casa_box>
RECEITUÁRIO DOMICILIAR:
Para cada medicação:
  Rx [número]: [nome comercial/genérico]
  [dose] — [forma farmacêutica]
  Tomar [posologia clara em linguagem acessível]
  Duração: [X dias]
  Quantidade: [X caixas/frascos/comprimidos]
</receita_casa_box>

<orientacoes_box>
ORIENTAÇÕES DE ALTA:
1. [orientação objetiva]
2. [sinais de alarme para retorno]
3. [encaminhamento ambulatorial se necessário]
4. [retorno ao PA se: ...]
</orientacoes_box>

Para REAVALIAÇÃO, use a tag adicional:
<reavaliacao_box>
REAVALIAÇÃO — [timestamp/momento]
Evolução clínica: [o que mudou]
Exames: [resultados relevantes com interpretação]
Conduta atual: [manutenção, ajuste, nova medicação]
Plano: [alta / obs / transferência / internação com justificativa]
</reavaliacao_box>

Para DÚVIDA clínica, responda em texto livre sem XML, como um colega médico experiente.

=== IMPERATIVOS FINAIS ===
- Nunca solicite exames não disponíveis no HGS José.
- Nunca recomende internação sem justificar exaustivamente por que alta ou transferência não são opções.
- Seja preciso nas doses. Em caso de dúvida, cite a faixa terapêutica.
- Use terminologia médica adequada, mas com clareza.
- Pense como um médico de trincheira: recursos mínimos, decisão máxima.
"""

# ─────────────────────────────────────────────
# UTILITÁRIOS – hash / storage
# ─────────────────────────────────────────────

def _get_pepper() -> str:
    """Retorna o PEPPER dos secrets ou usa fallback para dev."""
    try:
        return st.secrets["PEPPER"]
    except Exception:
        return "sadc-hgs-dev-pepper-2025"


def generate_record_key(content: str) -> str:
    """
    Gera chave Base62 curta (8 chars) a partir do conteúdo + PEPPER.
    Colisões praticamente impossíveis no contexto de uso.
    """
    pepper = _get_pepper()
    raw = f"{pepper}::{content[:512]}"
    digest = hashlib.sha256(raw.encode("utf-8")).digest()
    # Base62 encoding
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    num = int.from_bytes(digest[:8], "big")
    result = []
    while num:
        num, rem = divmod(num, 62)
        result.append(alphabet[rem])
    key = "".join(reversed(result or ["0"])).ljust(8, "0")[:8]
    return key


def store_record(key: str, data: dict) -> None:
    """Armazena prontuário no session_state como banco leve."""
    if "records_db" not in st.session_state:
        st.session_state["records_db"] = {}
    st.session_state["records_db"][key] = {
        "data": data,
        "ts": time.time(),
    }


def load_record(key: str) -> Optional[dict]:
    """Recupera prontuário do session_state."""
    db = st.session_state.get("records_db", {})
    entry = db.get(key)
    return entry["data"] if entry else None


def list_records() -> list[dict]:
    """Lista todos os prontuários armazenados."""
    db = st.session_state.get("records_db", {})
    result = []
    for key, entry in db.items():
        d = entry["data"]
        result.append({
            "key": key,
            "nome": d.get("identificacao", "—")[:30],
            "ts": entry["ts"],
        })
    result.sort(key=lambda x: x["ts"], reverse=True)
    return result


# ─────────────────────────────────────────────
# ROTEADOR TRIPLE-ENGINE
# ─────────────────────────────────────────────

GEMINI_MODELS = [
    "gemini-2.5-flash",
    "gemini-3-flash-preview",
    "gemini-3.1-flash-lite-preview",
]


def call_gemini(model: str, messages: list[dict], system: str) -> str:
    try:
        import google.generativeai as genai
        key = st.secrets.get("GOOGLE_API_KEY", "")
        if not key:
            return "❌ ERRO: GOOGLE_API_KEY não configurada em st.secrets."
        genai.configure(api_key=key)
        gmodel = genai.GenerativeModel(
            model_name=model,
            system_instruction=system,
        )
        # Converter para formato Gemini
        history = []
        for m in messages[:-1]:
            role = "user" if m["role"] == "user" else "model"
            history.append({"role": role, "parts": [m["content"]]})
        chat = gmodel.start_chat(history=history)
        response = chat.send_message(messages[-1]["content"])
        return response.text
    except Exception as e:
        return f"❌ ERRO Google Gemini [{model}]: {e}"


def call_ai(model: str, messages: list[dict], system: str = SYSTEM_PROMPT) -> str:
    """Chama o Google Gemini."""
    return call_gemini(model, messages, system)


# ─────────────────────────────────────────────
# PARSER DE TAGS XML
# ─────────────────────────────────────────────

def extract_tag(text: str, tag: str) -> str:
    """Extrai conteúdo de uma tag XML da resposta da IA."""
    pattern = rf"<{tag}>(.*?)</{tag}>"
    match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
    return match.group(1).strip() if match else ""


# ─────────────────────────────────────────────
# RENDERIZADOR DE PRONTUÁRIO
# ─────────────────────────────────────────────

def render_prontuario(ai_text: str) -> None:
    """Renderiza o prontuário extraindo blocos XML."""

    visao = extract_tag(ai_text, "visao_geral")
    sit = extract_tag(ai_text, "sit_box")
    hma = extract_tag(ai_text, "hma_box")
    hpp = extract_tag(ai_text, "hpp_box")
    ef = extract_tag(ai_text, "exame_fisico_box")
    ec = extract_tag(ai_text, "exames_complementares_box")
    hd = extract_tag(ai_text, "hd_box")
    meds_intra = extract_tag(ai_text, "meds_intra_box")
    exames_intra = extract_tag(ai_text, "exames_intra_box")
    encaminha = extract_tag(ai_text, "encaminhamento_box")
    receita = extract_tag(ai_text, "receita_casa_box")
    orientacoes = extract_tag(ai_text, "orientacoes_box")
    reavaliacao = extract_tag(ai_text, "reavaliacao_box")

    if not any([visao, sit, hma, hd]):
        # Resposta sem XML (dúvida clínica)
        st.info(ai_text)
        return

    if visao:
        st.info(f"🔭 **Visão Geral**\n\n{visao}")

    col1, col2 = st.columns(2)

    with col1:
        if sit:
            st.markdown(
                f"""<div style="background:#161c2d;border:1px solid #1e2a42;border-left:4px solid #3b82f6;
                border-radius:10px;padding:1rem 1.2rem;margin-bottom:.8rem;">
                <p style="margin:0;font-size:.7rem;color:#64748b;font-family:'DM Mono',monospace;
                letter-spacing:.08em;text-transform:uppercase;">SITUAÇÃO</p>
                <p style="margin:.3rem 0 0;color:#e2e8f0;font-size:.9rem;">{sit}</p>
                </div>""",
                unsafe_allow_html=True,
            )
        if hma:
            st.markdown(
                f"""<div style="background:#161c2d;border:1px solid #1e2a42;
                border-radius:10px;padding:1rem 1.2rem;margin-bottom:.8rem;">
                <p style="margin:0;font-size:.7rem;color:#64748b;font-family:'DM Mono',monospace;
                letter-spacing:.08em;text-transform:uppercase;">HMA</p>
                <p style="margin:.3rem 0 0;color:#e2e8f0;font-size:.88rem;line-height:1.6;">{hma}</p>
                </div>""",
                unsafe_allow_html=True,
            )
        if hpp:
            st.markdown(
                f"""<div style="background:#161c2d;border:1px solid #1e2a42;
                border-radius:10px;padding:1rem 1.2rem;margin-bottom:.8rem;">
                <p style="margin:0;font-size:.7rem;color:#64748b;font-family:'DM Mono',monospace;
                letter-spacing:.08em;text-transform:uppercase;">HPP / Antecedentes</p>
                <p style="margin:.3rem 0 0;color:#e2e8f0;font-size:.88rem;line-height:1.6;">{hpp}</p>
                </div>""",
                unsafe_allow_html=True,
            )

    with col2:
        if ef:
            st.markdown(
                f"""<div style="background:#161c2d;border:1px solid #1e2a42;
                border-radius:10px;padding:1rem 1.2rem;margin-bottom:.8rem;">
                <p style="margin:0;font-size:.7rem;color:#64748b;font-family:'DM Mono',monospace;
                letter-spacing:.08em;text-transform:uppercase;">Exame Físico</p>
                <p style="margin:.3rem 0 0;color:#e2e8f0;font-size:.88rem;line-height:1.6;">{ef}</p>
                </div>""",
                unsafe_allow_html=True,
            )
        if ec:
            st.markdown(
                f"""<div style="background:#161c2d;border:1px solid #1e2a42;
                border-radius:10px;padding:1rem 1.2rem;margin-bottom:.8rem;">
                <p style="margin:0;font-size:.7rem;color:#64748b;font-family:'DM Mono',monospace;
                letter-spacing:.08em;text-transform:uppercase;">Exames Complementares</p>
                <p style="margin:.3rem 0 0;color:#e2e8f0;font-size:.88rem;line-height:1.6;">{ec}</p>
                </div>""",
                unsafe_allow_html=True,
            )

    if hd:
        st.error(f"🎯 **Hipóteses Diagnósticas**\n\n{hd}")

    # Expander protegido: meds + exames intra-PA
    if meds_intra or exames_intra:
        with st.expander("⚕️ Conduta no PA — Medicações e Exames (clique para expandir)", expanded=False):
            st.markdown(
                "<p style='font-size:.72rem;color:#f59e0b;font-family:\"DM Mono\",monospace;"
                "letter-spacing:.06em;'>⚠️ CONFIRME DOSES E ALERGIAS ANTES DE ADMINISTRAR</p>",
                unsafe_allow_html=True,
            )
            if meds_intra:
                st.markdown("**💊 Medicações no PA:**")
                st.markdown(
                    f"""<div style="background:#0d1117;border:1px solid #1e2a42;border-radius:8px;
                    padding:1rem;font-family:'DM Mono',monospace;font-size:.82rem;
                    line-height:1.8;color:#e2e8f0;white-space:pre-wrap;">{meds_intra}</div>""",
                    unsafe_allow_html=True,
                )
            if exames_intra:
                st.markdown("**🔬 Exames Solicitados no PA:**")
                st.markdown(
                    f"""<div style="background:#0d1117;border:1px solid #1e2a42;border-radius:8px;
                    padding:1rem;font-family:'DM Mono',monospace;font-size:.82rem;
                    line-height:1.8;color:#e2e8f0;white-space:pre-wrap;">{exames_intra}</div>""",
                    unsafe_allow_html=True,
                )

    # Encaminhamento — cópia fácil
    if encaminha:
        st.markdown("---")
        st.markdown(
            "<p style='font-size:.72rem;color:#64748b;font-family:\"DM Mono\",monospace;"
            "letter-spacing:.06em;text-transform:uppercase;'>Resumo para Transferência / Encaminhamento</p>",
            unsafe_allow_html=True,
        )
        st.code(encaminha, language="markdown")

    # Receita e orientações
    col3, col4 = st.columns(2)
    with col3:
        if receita:
            st.success("📋 Receituário Domiciliar")
            st.code(receita, language="markdown")
    with col4:
        if orientacoes:
            st.success("📌 Orientações de Alta")
            st.code(orientacoes, language="markdown")

    # Reavaliação
    if reavaliacao:
        st.markdown("---")
        st.markdown(
            "<p style='font-size:.72rem;color:#6366f1;font-family:\"DM Mono\",monospace;"
            "letter-spacing:.06em;text-transform:uppercase;'>📊 Reavaliação</p>",
            unsafe_allow_html=True,
        )
        st.info(reavaliacao)


# ─────────────────────────────────────────────
# FORMULÁRIO DE ADMISSÃO
# ─────────────────────────────────────────────

def render_admission_form() -> Optional[dict]:
    """Renderiza o formulário de admissão e retorna os dados se submetido."""

    st.markdown(
        "<p style='font-family:\"Syne\",sans-serif;font-size:1.1rem;font-weight:700;"
        "color:#e2e8f0;margin-bottom:1rem;'>📝 Nova Avaliação</p>",
        unsafe_allow_html=True,
    )

    with st.form("admission_form", clear_on_submit=False):
        col1, col2 = st.columns([3, 1])
        with col1:
            identificacao = st.text_input("Identificação do Paciente", placeholder="Nome ou iniciais / nº atendimento")
        with col2:
            sexo = st.selectbox("Sexo", ["Masculino", "Feminino", "Outro/NI"])

        col3, col4 = st.columns([2, 2])
        with col3:
            idade = st.text_input("Idade", placeholder="Ex: 54 anos")
        with col4:
            acompanhante = st.text_input("Acompanhante", placeholder="Nome / grau de parentesco")

        hma = st.text_area("HMA – História da Moléstia Atual", height=120,
                            placeholder="Queixa principal, evolução, sintomas associados, fatores de melhora/piora...")

        hpp = st.text_area("HPP / Medicações em Uso", height=80,
                            placeholder="Doenças crônicas, cirurgias prévias, alergias, medicamentos...")

        st.markdown(
            "<p style='font-size:.72rem;color:#64748b;font-family:\"DM Mono\",monospace;"
            "letter-spacing:.06em;text-transform:uppercase;margin-top:.5rem;'>Sinais Vitais</p>",
            unsafe_allow_html=True,
        )
        vc1, vc2, vc3, vc4, vc5 = st.columns(5)
        with vc1:
            pa = st.text_input("PA (mmHg)", placeholder="120/80")
        with vc2:
            fc = st.text_input("FC (bpm)", placeholder="80")
        with vc3:
            sato2 = st.text_input("SatO2 (%)", placeholder="98")
        with vc4:
            temp = st.text_input("Temp (°C)", placeholder="36.5")
        with vc5:
            fr = st.text_input("FR (irpm)", placeholder="16")

        ef = st.text_area("Exame Físico", height=100,
                           placeholder="Estado geral, pele/mucosas, cardiovascular, respiratório, abdome, neuro...")

        exames_prev = st.text_area("Exames Prévios (resultados já disponíveis)", height=80,
                                    placeholder="ECG: ritmo sinusal, FC 88... / Rx Tórax: sem infiltrados...")

        hd_input = st.text_input("Hipótese Diagnóstica inicial do médico", placeholder="Ex: IAM sem supra / ITU baixa complicada")

        submitted = st.form_submit_button("🤖 Gerar Avaliação com IA", use_container_width=True)

    if submitted:
        return {
            "identificacao": identificacao,
            "acompanhante": acompanhante,
            "sexo": sexo,
            "idade": idade,
            "hma": hma,
            "hpp": hpp,
            "vitais": f"PA: {pa} | FC: {fc} | SatO2: {sato2}% | Temp: {temp}°C | FR: {fr}irpm",
            "exame_fisico": ef,
            "exames_previos": exames_prev,
            "hd": hd_input,
        }
    return None


def build_admission_prompt(form_data: dict) -> str:
    """Monta o prompt de admissão a partir dos dados do formulário."""
    return f"""
Realize a avaliação clínica completa deste paciente, gerando TODOS os blocos XML solicitados no seu sistema.

DADOS DE ADMISSÃO:
- Identificação: {form_data['identificacao']}
- Sexo: {form_data['sexo']} | Idade: {form_data['idade']}
- Acompanhante: {form_data['acompanhante']}

SINAIS VITAIS: {form_data['vitais']}

HMA:
{form_data['hma']}

HPP / Medicações:
{form_data['hpp']}

EXAME FÍSICO:
{form_data['exame_fisico']}

EXAMES DISPONÍVEIS / PRÉVIOS:
{form_data['exames_previos']}

HIPÓTESE DIAGNÓSTICA DO MÉDICO: {form_data['hd']}

Lembre-se: recursos do HGS José são EXTREMAMENTE limitados.
Gere TODOS os blocos XML: visao_geral, sit_box, hma_box, hpp_box, exame_fisico_box,
exames_complementares_box, hd_box, meds_intra_box, exames_intra_box,
encaminhamento_box, receita_casa_box, orientacoes_box.
"""


# ─────────────────────────────────────────────
# SIDEBAR – configuração da IA
# ─────────────────────────────────────────────

def render_sidebar() -> str:
    """Renderiza sidebar e retorna o modelo Gemini selecionado."""
    with st.sidebar:
        st.markdown(
            "<p style='font-family:\"Syne\",sans-serif;font-size:1rem;font-weight:800;"
            "color:#e2e8f0;letter-spacing:-.01em;'>⚙️ Configuração da IA</p>",
            unsafe_allow_html=True,
        )

        st.markdown(
            "<div style='display:flex;align-items:center;gap:.5rem;margin-bottom:.6rem;'>"
            "<img src='https://www.gstatic.com/lamda/images/gemini_favicon_f069958c85030456e93de685481c559f160ea06.svg' "
            "width='18' style='opacity:.8;'/>"
            "<span style='font-size:.72rem;color:#64748b;font-family:\"DM Mono\",monospace;"
            "letter-spacing:.06em;text-transform:uppercase;'>Google Gemini</span></div>",
            unsafe_allow_html=True,
        )

        model = st.selectbox(
            "Modelo",
            GEMINI_MODELS,
            key="sidebar_model",
        )

        st.markdown("---")
        st.markdown(
            "<p style='font-size:.7rem;color:#374151;font-family:\"DM Mono\",monospace;'>HGS José · Contagem/MG<br>"
            "SADC v1.0 · Uso interno</p>",
            unsafe_allow_html=True,
        )

        # Lista de prontuários na sessão
        records = list_records()
        if records:
            st.markdown("---")
            st.markdown(
                "<p style='font-size:.72rem;color:#64748b;font-family:\"DM Mono\",monospace;"
                "letter-spacing:.06em;text-transform:uppercase;'>Prontuários desta sessão</p>",
                unsafe_allow_html=True,
            )
            for r in records:
                ts_str = time.strftime("%H:%M", time.localtime(r["ts"]))
                label = f"[{ts_str}] {r['nome'][:20]}…" if len(r['nome']) > 20 else f"[{ts_str}] {r['nome']}"
                if st.button(label, key=f"btn_rec_{r['key']}"):
                    st.session_state["active_record_key"] = r["key"]
                    st.rerun()

        if st.button("➕ Novo Paciente", use_container_width=True):
            st.session_state["active_record_key"] = None
            st.session_state["chat_history"] = []
            st.rerun()

    return model


# ─────────────────────────────────────────────
# LANDING PAGE / LOGIN
# ─────────────────────────────────────────────

def render_login() -> None:
    """Renderiza a página de login."""
    st.markdown(LANDING_CSS, unsafe_allow_html=True)

    st.markdown(
        """
        <div class="lp-wrap">
          <div class="lp-card">
            <div class="lp-logo">🏥</div>
            <h1 class="lp-title">SADC</h1>
            <p class="lp-subtitle">Sistema de Apoio à Decisão Clínica<br>
            Hospital Geral São José · Contagem/MG</p>
            <div class="lp-badge">⚕ ACESSO RESTRITO · EQUIPE MÉDICA</div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Centralizar o formulário
    _, center, _ = st.columns([1, 2, 1])
    with center:
        with st.container():
            st.markdown(
                "<div style='background:rgba(22,28,45,.85);border:1px solid rgba(59,130,246,.2);"
                "border-radius:16px;padding:2rem;backdrop-filter:blur(20px);'>",
                unsafe_allow_html=True,
            )

            st.markdown(
                "<p style='text-align:center;font-family:\"Syne\",sans-serif;font-size:1.3rem;"
                "font-weight:700;color:#e2e8f0;margin-bottom:1.5rem;'>Autenticação</p>",
                unsafe_allow_html=True,
            )

            usuario = st.text_input("Usuário", placeholder="usuario.hgsj", key="login_user")
            senha = st.text_input("Senha corporativa", type="password", placeholder="••••••••", key="login_pass")

            if st.button("Entrar no sistema →", use_container_width=True, key="btn_login"):
                try:
                    valid_user = st.secrets.get("APP_USER", "plantonista")
                    valid_pass = st.secrets.get("APP_PASS", "sadc2025")
                except Exception:
                    valid_user = "plantonista"
                    valid_pass = "sadc2025"

                if usuario == valid_user and senha == valid_pass:
                    st.session_state["authenticated"] = True
                    st.rerun()
                else:
                    st.error("❌ Credenciais inválidas.")

            st.markdown("</div>", unsafe_allow_html=True)
            st.markdown(
                "<p style='text-align:center;font-size:.7rem;color:#374151;margin-top:1rem;"
                "font-family:\"DM Mono\",monospace;'>Sistema de uso exclusivo da equipe médica do HGS José</p>",
                unsafe_allow_html=True,
            )


# ─────────────────────────────────────────────
# TELA PRINCIPAL – PRONTUÁRIO + CHAT
# ─────────────────────────────────────────────

def render_main_app() -> None:
    """Tela principal após autenticação."""

    model = render_sidebar()

    # Header
    st.markdown(
        """
        <div style="display:flex;align-items:center;gap:1rem;margin-bottom:1.5rem;
        padding-bottom:1rem;border-bottom:1px solid #1e2a42;">
          <div style="background:linear-gradient(135deg,#3b82f6,#6366f1);border-radius:12px;
          width:44px;height:44px;display:flex;align-items:center;justify-content:center;
          font-size:1.4rem;flex-shrink:0;">🏥</div>
          <div>
            <p style="margin:0;font-family:'Syne',sans-serif;font-size:1.25rem;font-weight:800;
            color:#e2e8f0;letter-spacing:-.02em;">SADC — Pronto Atendimento</p>
            <p style="margin:0;font-size:.75rem;color:#64748b;font-family:'DM Mono',monospace;">
            Hospital Geral São José · Contagem/MG · Clínica Médica</p>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    active_key = st.session_state.get("active_record_key")

    # ── VISUALIZAR PRONTUÁRIO EXISTENTE ────────────────
    if active_key:
        record = load_record(active_key)
        if record:
            st.markdown(
                f"<p style='font-family:\"Syne\",sans-serif;font-size:1rem;font-weight:700;"
                f"color:#e2e8f0;'>📂 {record.get('identificacao', '—')} "
                f"<span style='color:#64748b;font-size:.8rem;font-weight:400;'>"
                f"[chave: {active_key}]</span></p>",
                unsafe_allow_html=True,
            )
            render_prontuario(record.get("ai_response", ""))
            _render_continuous_interaction(record, active_key, model)
            return

    # ── NOVO PACIENTE ──────────────────────────────────
    form_data = render_admission_form()

    if form_data:
        if not form_data.get("hma", "").strip():
            st.warning("⚠️ Preencha ao menos a HMA antes de gerar a avaliação.")
            return

        prompt = build_admission_prompt(form_data)
        messages = [{"role": "user", "content": prompt}]

        with st.spinner(f"🤖 Gerando avaliação com Gemini — {model}…"):
            ai_response = call_ai(model, messages)

        # Armazenar
        record_content = json.dumps(form_data, ensure_ascii=False)
        key = generate_record_key(record_content)
        full_record = {**form_data, "ai_response": ai_response, "messages": messages}
        store_record(key, full_record)
        st.session_state["active_record_key"] = key
        st.session_state["chat_history"] = []

        # Renderizar
        render_prontuario(ai_response)
        _render_continuous_interaction(full_record, key, model)


def _render_continuous_interaction(record: dict, record_key: str, model: str) -> None:
    """Componente de interação contínua pós-avaliação."""

    st.markdown("---")
    st.markdown(
        "<p style='font-family:\"Syne\",sans-serif;font-size:1rem;font-weight:700;"
        "color:#e2e8f0;'>💬 Interação Contínua</p>",
        unsafe_allow_html=True,
    )

    interaction_mode = st.radio(
        "Modo de interação",
        [
            "🩺 Dúvida clínica (colega médico)",
            "📝 Complemento à avaliação inicial",
            "🔄 Reavaliação do paciente",
        ],
        key=f"radio_mode_{record_key}",
        horizontal=True,
    )

    # Histórico de chat
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []

    for msg in st.session_state["chat_history"]:
        with st.chat_message(msg["role"]):
            if msg["role"] == "assistant":
                render_prontuario(msg["content"])
            else:
                st.write(msg["content"])

    user_input = st.chat_input("Digite sua mensagem…")

    if user_input:
        st.session_state["chat_history"].append({"role": "user", "content": user_input})

        # Montar contexto
        context_summary = (
            f"Prontuário atual do paciente {record.get('identificacao','—')}:\n"
            f"Vitais: {record.get('vitais','—')}\n"
            f"HMA: {record.get('hma','—')}\n"
            f"Avaliação IA prévia: {record.get('ai_response','—')[:800]}…\n"
        )

        if "Dúvida" in interaction_mode:
            mode_instruction = (
                "O médico tem uma DÚVIDA CLÍNICA. Responda como colega médico experiente, "
                "em texto livre, sem gerar XML. Seja direto e prático."
            )
        elif "Complemento" in interaction_mode:
            mode_instruction = (
                "O médico fornece uma NOVA INFORMAÇÃO para complementar a avaliação inicial. "
                "Reescreva TODOS os blocos XML pertinentes incorporando a nova informação."
            )
        else:  # Reavaliação
            mode_instruction = (
                "O médico está realizando uma REAVALIAÇÃO do paciente. "
                "Gere um novo bloco <reavaliacao_box> evoluindo o paciente com as informações fornecidas."
            )

        full_prompt = (
            f"{context_summary}\n\n"
            f"INSTRUÇÃO DE MODO: {mode_instruction}\n\n"
            f"MENSAGEM DO MÉDICO: {user_input}"
        )

        messages = [{"role": "user", "content": full_prompt}]

        with st.chat_message("assistant"):
            with st.spinner(f"🤖 Gemini ({model}) pensando…"):
                ai_resp = call_ai(model, messages)
            render_prontuario(ai_resp)

        st.session_state["chat_history"].append({"role": "assistant", "content": ai_resp})

        # Atualizar registro com nova resposta
        record["ai_response"] = ai_resp
        store_record(record_key, record)


# ─────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────

def main() -> None:
    st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False
    if "active_record_key" not in st.session_state:
        st.session_state["active_record_key"] = None
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []

    if not st.session_state["authenticated"]:
        render_login()
    else:
        render_main_app()


if __name__ == "__main__":
    main()
