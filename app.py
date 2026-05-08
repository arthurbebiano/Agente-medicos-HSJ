"""
app.py
Aplicação principal SADC — Sistema de Apoio à Decisão Clínica
Hospital Geral São José — Contagem/MG
Powered by Streamlit + Google Gemini
"""

# ════════════════════════════════════════════════════════════════
# IMPORTS
# ════════════════════════════════════════════════════════════════
import re
from datetime import datetime

import streamlit as st
import google.generativeai as genai

import db
from prompt_base import get_system_prompt

# ════════════════════════════════════════════════════════════════
# 1. PAGE CONFIG — DEVE SER O PRIMEIRO COMANDO STREAMLIT
# ════════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="SADC | Hospital Geral São José",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ════════════════════════════════════════════════════════════════
# 2. SESSION STATE
# ════════════════════════════════════════════════════════════════
def _init_session():
    defaults = {
        "logged_in": False,
        "current_patient_id": None,
        "show_form": False,
        "chat_history": [],
        "parsed_response": {},
        "selected_model": None,
        "available_models": [],
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

_init_session()

# ════════════════════════════════════════════════════════════════
# 3. GEMINI — CONFIGURAÇÃO
# ════════════════════════════════════════════════════════════════
def configure_gemini() -> bool:
    try:
        api_key = st.secrets["GOOGLE_API_KEY"]
        genai.configure(api_key=api_key)
        return True
    except Exception:
        return False

# ════════════════════════════════════════════════════════════════
# 4. MODELOS — LISTAGEM E FORMATAÇÃO
# ════════════════════════════════════════════════════════════════
def get_flash_models() -> list:
    """Lista modelos Gemini Flash, filtra e ordena do mais novo ao mais antigo."""
    if st.session_state.available_models:
        return st.session_state.available_models

    SKIP = {"tts", "embed", "aqa", "bison", "vision"}

    try:
        all_models = genai.list_models()
        flash_models = []

        for m in all_models:
            name_lower = m.name.lower()
            if "flash" not in name_lower:
                continue
            if "generateContent" not in m.supported_generation_methods:
                continue
            if any(s in name_lower for s in SKIP):
                continue
            flash_models.append(m.name)

        def _sort_key(name):
            match = re.search(r"gemini-(\d+)\.(\d+)", name)
            if match:
                return (int(match.group(1)), int(match.group(2)))
            match = re.search(r"gemini-(\d+)", name)
            if match:
                return (int(match.group(1)), 0)
            return (0, 0)

        flash_models.sort(key=_sort_key, reverse=True)

        if not flash_models:
            flash_models = ["models/gemini-1.5-flash"]

        st.session_state.available_models = flash_models
        if not st.session_state.selected_model:
            st.session_state.selected_model = flash_models[0]

        return flash_models

    except Exception:
        fallback = ["models/gemini-1.5-flash"]
        st.session_state.available_models = fallback
        if not st.session_state.selected_model:
            st.session_state.selected_model = fallback[0]
        return fallback


def format_model_name(model_name: str) -> str:
    """Transforma 'models/gemini-2.5-flash-preview-05-20' → '✨ Gemini 2.5 Flash — Preview'"""
    clean = model_name.replace("models/", "")
    match = re.match(r"gemini-(\d+\.\d+)-flash(.*)", clean)
    if match:
        version = match.group(1)
        raw_suffix = match.group(2).strip("-")
        parts = [
            p.capitalize()
            for p in raw_suffix.split("-")
            if p and not re.fullmatch(r"[\d]+", p)
        ]
        suffix = " ".join(parts)
        return f"✨ Gemini {version} Flash{'  —  ' + suffix if suffix else ''}"
    return clean.replace("gemini-", "Gemini ").replace("-", " ").title()

# ════════════════════════════════════════════════════════════════
# 5. XML PARSER
# ════════════════════════════════════════════════════════════════
KNOWN_TAGS = [
    "visao_geral", "sit_box", "hma_box", "hpp_box",
    "exame_fisico_box", "hd_conduta_box",
    "encaminhamento_box", "receita_casa_box",
    "orientacoes_casa_box", "intra_hospitalar_box",
]


def parse_xml_response(text: str) -> dict:
    result = {}
    for tag in KNOWN_TAGS:
        match = re.search(rf"<{tag}>(.*?)</{tag}>", text, re.DOTALL | re.IGNORECASE)
        if match:
            result[tag] = match.group(1).strip()
    return result


def strip_xml(text: str) -> str:
    clean = re.sub(r"</?[a-zA-Z_][a-zA-Z0-9_]*\s*/?>", "", text)
    clean = re.sub(r"\n{3,}", "\n\n", clean)
    return clean.strip()

# ════════════════════════════════════════════════════════════════
# 6. GEMINI — GERAÇÃO DE RESPOSTA
# ════════════════════════════════════════════════════════════════
def generate_gemini_response(history: list, model_name: str) -> str:
    """
    Gera resposta via Gemini. O último item de `history` deve ser
    a mensagem do usuário (role="user").
    """
    if not history:
        return "❌ Histórico de mensagens vazio."
    if history[-1]["role"] != "user":
        return "❌ Erro interno: último item do histórico não é do usuário."

    try:
        system_prompt = get_system_prompt()
        clean_model = model_name.replace("models/", "")

        model_obj = genai.GenerativeModel(
            model_name=clean_model,
            system_instruction=system_prompt,
            generation_config=genai.GenerationConfig(
                temperature=0.25,
                top_p=0.95,
                max_output_tokens=8192,
            ),
        )

        # Histórico anterior + nova mensagem
        past = history[:-1]
        new_msg_parts = history[-1]["parts"]
        new_msg = new_msg_parts[0] if isinstance(new_msg_parts, list) else new_msg_parts

        gemini_history = []
        for msg in past:
            parts = msg["parts"]
            txt = parts[0] if isinstance(parts, list) else parts
            gemini_history.append({"role": msg["role"], "parts": [txt]})

        chat = model_obj.start_chat(history=gemini_history)
        response = chat.send_message(new_msg)
        return response.text

    except ValueError as e:
        return (
            f"⚠️ Resposta bloqueada pelos filtros de segurança: {e}\n"
            "Tente reformular com linguagem clínica mais precisa."
        )
    except Exception as e:
        err = str(e)
        if any(kw in err.lower() for kw in ["api_key", "invalid", "authentication"]):
            return "❌ Erro de autenticação. Verifique GOOGLE_API_KEY em secrets.toml."
        if any(kw in err.lower() for kw in ["quota", "rate", "429"]):
            return "❌ Limite de requisições atingido. Aguarde alguns segundos."
        if "not found" in err.lower() and "model" in err.lower():
            return f"❌ Modelo '{model_name}' não encontrado. Selecione outro na barra lateral."
        return f"❌ Erro inesperado: {err}"

# ════════════════════════════════════════════════════════════════
# 7. LANDING PAGE
# ════════════════════════════════════════════════════════════════
def render_landing_page():
    # ── Hero ──────────────────────────────────────────────────
    st.markdown(
        """
        <div style="
            background: linear-gradient(135deg, #0a237a 0%, #1565c0 55%, #1e88e5 100%);
            padding: 3.5rem 2rem 2.8rem;
            border-radius: 18px;
            text-align: center;
            margin-bottom: 2.5rem;
            box-shadow: 0 8px 32px rgba(13,71,161,0.35);
        ">
            <div style="font-size:4.5rem; margin-bottom:0.8rem;">🏥</div>
            <h1 style="color:#fff; font-size:3rem; font-weight:900; margin:0; letter-spacing:-1.5px;">
                SADC
            </h1>
            <h2 style="color:#90caf9; font-size:1.3rem; font-weight:400; margin:0.4rem 0 0.8rem;">
                Sistema de Apoio à Decisão Clínica
            </h2>
            <p style="color:#bbdefb; font-size:1rem; margin:0;">
                Hospital Geral São José &nbsp;·&nbsp; Contagem, MG
                &nbsp;·&nbsp; Pronto Atendimento &nbsp;·&nbsp; Powered by Google Gemini
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── Feature cards ─────────────────────────────────────────
    c1, c2, c3, c4 = st.columns(4)
    cards = [
        (c1, "🤖", "#e8f5e9", "#2e7d32", "IA Gemini Flash",
         "Raciocínio clínico contextualizado para o PA do HGS José. Protocolos integrados."),
        (c2, "⚗️", "#fff3e0", "#e65100", "Recursos Reais",
         "Adapta-se à realidade: Troponina · EAS · Gasometria · ECG · RX · TC s/contraste."),
        (c3, "📋", "#e3f2fd", "#1565c0", "Documentação Pronta",
         "Gera avaliação, encaminhamento, receituário e plano de observação em segundos."),
        (c4, "💾", "#f3e5f5", "#6a1b9a", "Histórico Local",
         "Prontuários salvos localmente. Retome atendimentos a qualquer momento."),
    ]
    for col, icon, bg, border, title, desc in cards:
        with col:
            st.markdown(
                f"""
                <div style="background:{bg}; padding:1.4rem 1.2rem; border-radius:12px;
                            border-left:4px solid {border}; min-height:160px;">
                    <div style="font-size:2rem;">{icon}</div>
                    <h4 style="color:{border}; margin:0.5rem 0 0.3rem; font-size:0.95rem;">{title}</h4>
                    <p style="color:#555; font-size:0.82rem; margin:0; line-height:1.45;">{desc}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Limitações banner ─────────────────────────────────────
    st.markdown(
        """
        <div style="background:#fff8e1; border:1px solid #ffe082;
                    border-left:5px solid #f9a825; padding:0.9rem 1.5rem;
                    border-radius:8px; margin-bottom:2rem; font-size:0.9rem;">
            <strong>⚠️ Recursos do PA — HGS José (Limitações conhecidas pelo sistema):</strong><br>
            Lab: <strong>Troponina · EAS · Gasometria</strong> (únicos disponíveis) &nbsp;|&nbsp;
            Imagem: <strong>ECG · RX · TC sem contraste</strong> (médico interpreta) &nbsp;|&nbsp;
            Equipe: <strong>1 Clínico · 1 Pediatra · 1 Cirurgião</strong> &nbsp;|&nbsp;
            Internação: <strong style="color:#c62828;">ZERO leitos</strong>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── Login ─────────────────────────────────────────────────
    st.markdown("### 🔐 Acesso Restrito ao Sistema")
    _, col_c, _ = st.columns([1, 1.4, 1])
    with col_c:
        with st.form("login_form"):
            st.markdown("**Credenciais de Acesso**")
            username_input = st.text_input("👤 Usuário", placeholder="admin")
            password_input = st.text_input("🔒 Senha", type="password", placeholder="••••••••")
            btn = st.form_submit_button("✅ Entrar no Sistema", use_container_width=True)

            if btn:
                try:
                    vu = st.secrets["auth"]["username"]
                    vp = st.secrets["auth"]["password"]
                except Exception:
                    vu, vp = "admin", "senha123"

                if username_input == vu and password_input == vp:
                    st.session_state.logged_in = True
                    st.rerun()
                else:
                    st.error("❌ Usuário ou senha inválidos.")

    # ── Footer ────────────────────────────────────────────────
    st.markdown(
        """
        <div style="text-align:center; color:#9e9e9e; margin-top:3.5rem; font-size:0.78rem;">
            SADC v1.0 &nbsp;·&nbsp; Hospital Geral São José — Contagem/MG
            &nbsp;·&nbsp; Google Gemini API<br>
            <em>⚕️ Ferramenta de apoio à decisão clínica.
            Responsabilidade médica: exclusivamente do profissional habilitado.</em>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ════════════════════════════════════════════════════════════════
# 8. SIDEBAR
# ════════════════════════════════════════════════════════════════
def render_sidebar():
    with st.sidebar:
        # ── Logo ──────────────────────────────────────────────
        st.markdown(
            """
            <div style="background:linear-gradient(135deg,#0a237a,#1976d2);
                        padding:1rem; border-radius:10px; text-align:center; margin-bottom:1rem;">
                <span style="font-size:2rem;">🏥</span>
                <h4 style="color:white; margin:0.3rem 0 0; font-size:0.9rem;">SADC — HGS José</h4>
                <p style="color:#90caf9; font-size:0.7rem; margin:0;">Contagem/MG</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # ── Modelo Gemini ─────────────────────────────────────
        st.markdown("**⚙️ Modelo Gemini**")
        models = get_flash_models()
        labels = {m: format_model_name(m) for m in models}

        cur = st.session_state.get("selected_model") or (models[0] if models else "")
        if cur not in models and models:
            cur = models[0]
        cur_idx = models.index(cur) if cur in models else 0

        selected = st.selectbox(
            "modelo",
            options=models,
            format_func=lambda x: labels.get(x, x),
            index=cur_idx,
            label_visibility="collapsed",
        )
        st.session_state.selected_model = selected

        st.markdown("---")

        # ── Novo Atendimento ──────────────────────────────────
        if st.button("➕ Novo Atendimento", use_container_width=True, type="primary"):
            st.session_state.show_form = True
            st.session_state.current_patient_id = None
            st.session_state.chat_history = []
            st.session_state.parsed_response = {}
            st.rerun()

        st.markdown("---")

        # ── Histórico ─────────────────────────────────────────
        st.markdown("**📂 Atendimentos Recentes**")
        all_patients = db.carregar_todos_pacientes()

        if not all_patients:
            st.caption("_Nenhum atendimento registrado._")
        else:
            sorted_patients = sorted(
                all_patients.items(),
                key=lambda x: x[1].get("data", ""),
                reverse=True,
            )
            for pid, pdata in sorted_patients[:20]:
                nome = pdata.get("nome", "Sem nome")
                data_at = pdata.get("data", "--/--/---- --:--")
                queixa = pdata.get("dados_extras", {}).get("queixa", "")
                is_active = st.session_state.current_patient_id == pid

                if st.button(
                    f"👤 {nome[:17]}\n🕐 {data_at}",
                    key=f"sb_{pid}",
                    use_container_width=True,
                    type="primary" if is_active else "secondary",
                    help=f"QP: {queixa[:80]}" if queixa else None,
                ):
                    # Encontra último parsed response com XML
                    parsed = {}
                    for msg in reversed(pdata.get("historico", [])):
                        if msg["role"] == "model":
                            txt = (
                                msg["parts"][0]
                                if isinstance(msg["parts"], list)
                                else msg["parts"]
                            )
                            p = parse_xml_response(txt)
                            if p:
                                parsed = p
                                break

                    st.session_state.current_patient_id = pid
                    st.session_state.chat_history = pdata.get("historico", [])
                    st.session_state.parsed_response = parsed
                    st.session_state.show_form = False
                    st.rerun()

        st.markdown("---")

        # ── Sair ──────────────────────────────────────────────
        if st.button("🚪 Sair do Sistema", use_container_width=True):
            for k in list(st.session_state.keys()):
                del st.session_state[k]
            st.rerun()

# ════════════════════════════════════════════════════════════════
# 9. TELA DE BOAS-VINDAS
# ════════════════════════════════════════════════════════════════
def render_welcome():
    st.markdown(
        """
        <div style="text-align:center; padding:3rem 2rem;">
            <div style="font-size:5rem;">🏥</div>
            <h2 style="color:#1565c0; margin-top:1rem;">Bem-vindo ao SADC</h2>
            <p style="color:#666; font-size:1.05rem;">
                Sistema de Apoio à Decisão Clínica — Hospital Geral São José
            </p>
            <p style="color:#888;">
                Clique em <strong>➕ Novo Atendimento</strong> na barra lateral para iniciar<br>
                ou selecione um atendimento anterior.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.divider()

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**✅ Recursos Disponíveis**")
        for item, det in [
            ("Troponina (quantitativa)", "~60-90min"),
            ("EAS / Urina Tipo I", "~30min"),
            ("Gasometria Arterial", "~15min — inclui K⁺, Na⁺, Lactato, Glicose"),
            ("HGT (glicemia capilar)", "Imediato"),
            ("ECG 12 derivações", "Médico interpreta"),
            ("Radiografia simples", "Tórax/Abdome — médico interpreta"),
            ("TC sem contraste", "Crânio · Tórax · Abdome/Pelve"),
        ]:
            st.markdown(f"✅ **{item}** — _{det}_")

    with c2:
        st.markdown("**❌ NÃO Disponíveis (nunca solicitar)**")
        for item in [
            "Hemograma completo",
            "Função renal isolada (Cr, Ureia)",
            "Coagulograma (TP, INR, TTPA)",
            "Enzimas hepáticas (TGO, TGP, GGT)",
            "Eletrólitos isolados (apenas na Gasometria)",
            "TC com contraste / Angiotomografia",
            "Ultrassonografia / Ecocardiograma",
        ]:
            st.markdown(f"❌ ~~{item}~~")

    st.markdown(
        """
        <div style="background:#fff3e0; border-left:5px solid #f57c00;
                    padding:0.9rem 1.5rem; border-radius:8px; margin-top:1rem; font-size:0.9rem;">
            <strong>⚠️ Equipe:</strong> 1 Clínico Geral · 1 Pediatra · 1 Cirurgião Geral<br>
            <strong>⚠️ Internação:</strong> Capacidade ZERO — Estabilizar + Alta ou Transferência
        </div>
        """,
        unsafe_allow_html=True,
    )

# ════════════════════════════════════════════════════════════════
# 10. FORMULÁRIO — NOVO ATENDIMENTO
# ════════════════════════════════════════════════════════════════
def render_form():
    st.markdown(
        """
        <div style="background:linear-gradient(90deg,#0a237a,#1976d2);
                    padding:1.5rem 2rem; border-radius:12px; margin-bottom:1.5rem;">
            <h2 style="color:white; margin:0; font-size:1.6rem;">📋 Novo Atendimento</h2>
            <p style="color:#90caf9; margin:0.3rem 0 0; font-size:0.88rem;">
                Preencha os dados — a IA gerará a avaliação clínica estruturada
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.form("patient_form"):

        # ── IDENTIFICAÇÃO ──────────────────────────────────────
        st.markdown("#### 👤 Identificação do Paciente")
        fc1, fc2, fc3 = st.columns([3, 2, 1.5])
        with fc1:
            nome = st.text_input("Nome Completo *", placeholder="Maria Aparecida dos Santos")
        with fc2:
            idade = st.text_input("Idade *", placeholder="58 anos / 8 meses / 3 dias")
        with fc3:
            sexo = st.selectbox("Sexo *", ["Feminino", "Masculino", "Não Informado"])

        st.divider()

        # ── ACOMPANHANTE ───────────────────────────────────────
        st.markdown("#### 👥 Acompanhante")
        ac1, ac2 = st.columns([1.5, 2.5])
        with ac1:
            tem_acompanhante = st.radio("Acompanhado?", ["Sim", "Não"], horizontal=True)
        with ac2:
            acompanhante_nome = st.text_input(
                "Nome do acompanhante",
                placeholder="Mãe, cônjuge, cuidador, etc.",
                disabled=(tem_acompanhante == "Não"),
            ) if tem_acompanhante == "Sim" else ""

        st.divider()

        # ── AVALIAÇÃO CLÍNICA ──────────────────────────────────
        st.markdown("#### 🩺 Avaliação Clínica — HMA Detalhada")
        hma = st.text_area(
            "História da Moléstia Atual (HMA) — COMPLETA *",
            placeholder=(
                "Descreva DETALHADAMENTE:\n\n"
                "• QUANDO começou (data/hora) e como começou (súbito/gradual)?\n"
                "• CARACTERES DO SINTOMA: qualidade exata, intensidade (0-10), localização, irradia para onde?\n"
                "• PIORA COM: esforço, posição, movimento, alimentação? MELHORA COM: repouso, medicação, posição?\n"
                "• SINTOMAS ASSOCIADOS: febre, suor, náusea, vômito, tosse, falta de ar, tontura, fraqueza?\n"
                "• DURAÇÃO E PADRÃO: contínuo ou episódios? Frequência? Mudanças ao longo do tempo?\n"
                "• O QUE JÁ TOMOU e como respondeu?\n"
                "• CONTEXTO: exposição a doentes, viagens, imobilização, cirurgias recentes?"
            ),
            height=200,
        )

        hpp = st.text_area(
            "HPP / Medicações em Uso / Alergias / Hábitos",
            placeholder=(
                "• DOENÇAS PRÉVIAS: HAS, DM, problemas cardíacos, renais, pulmonares, imunossupressão?\n"
                "• MEDICAMENTOS ATUAIS: nome, dose, frequência\n"
                "• ALERGIAS: a qual medicamento? Que tipo de reação?\n"
                "• CIRURGIAS/INTERNAÇÕES: datas e motivos\n"
                "• HÁBITOS: tabagismo (quantos/dia), álcool (frequência), drogas ilícitas?\n"
                "• HISTÓRIA SEXUAL: parceiros, métodos contraceptivos (se relevante para este caso)"
            ),
            height=130,
        )

        st.divider()

        # ── SINAIS VITAIS ──────────────────────────────────────
        st.markdown("#### 📊 Sinais Vitais")
        sv = st.columns(7)
        labels_sv = ["PA (mmHg)", "FC (bpm)", "FR (irpm)", "T° (°C)", "SpO2 (%)", "HGT (mg/dL)", "Peso (kg)"]
        placeholders_sv = ["120/80", "72", "16", "36.5", "98", "95", "70"]
        sv_keys = ["sv_pa", "sv_fc", "sv_fr", "sv_temp", "sv_spo2", "sv_hgt", "sv_peso"]
        sv_vals = {}
        for col, lbl, ph, key in zip(sv, labels_sv, placeholders_sv, sv_keys):
            with col:
                sv_vals[key] = st.text_input(lbl, placeholder=ph)

        st.divider()

        # ── EXAME FÍSICO ───────────────────────────────────────
        st.markdown("#### 🔍 Exame Físico")
        st.caption(
            "Descreva achados sistematizados: estado geral, consciência, ausculta cardíaca/pulmonar, "
            "abdome, MMII, sinais neurológicos. A IA vai gerar o exame físico ESPERADO para este caso."
        )
        exame_fisico = st.text_area(
            "Achados do Exame Físico Realizado",
            placeholder=(
                "Ex:\n"
                "Estado geral: Bom, lúcido, corado, orientado, hidratado, afebril\n"
                "Cardiovascular: Ritmo regular, sem sopros, TEC < 2s\n"
                "Respiratório: Sons normais, eupneico, sem desconforto\n"
                "Abdome: Normotenso, indolor, RHA presentes\n"
                "Neurológico: Glasgow 15, pupilas normais, sem deficits\n"
                "MMII: Sem edema, pulsos presentes, simétricos"
            ),
            height=120,
        )

        st.divider()

        # ── EXAMES ────────────────────────────────────────────
        st.markdown("#### 🧪 Exames Realizados")
        st.caption(
            "⚠️ Disponíveis neste PA: Troponina · EAS · Gasometria Arterial · "
            "HGT · ECG · Radiografia · TC sem contraste"
        )
        exames = st.text_area(
            "Resultados dos Exames",
            placeholder=(
                "Ex:\n"
                "ECG: Ritmo sinusal, FC 88bpm, sem supra/infra ST.\n"
                "Troponina: 0,01 ng/mL (Ref < 0,04)\n"
                "Gasometria: pH 7,38 | pCO2 40 | pO2 82 | HCO3 24 | BE 0 | "
                "K+ 4,0 | Na+ 138 | Cl- 102 | Lactato 1,2 | Glicose 105 | Hb/Ht 14,0/42%\n"
                "EAS: Transparente, negativo para proteína e glicose, sem piúria\n"
                "RX Tórax: Sem consolidações, índice cardiotorácico dentro do normal."
            ),
            height=120,
        )

        info_extra = st.text_area(
            "Contexto / Informações Adicionais",
            placeholder=(
                "Informações epidemiológicas ou clínicas que contextualizam o caso:\n"
                "Ex: Gestante 28 semanas. Contato com tuberculose há 2 semanas. "
                "Morador de rua. Veio sozinho. Quadro semelhante há 3 meses."
            ),
            height=80,
        )

        st.divider()

        _, mid, _ = st.columns([1, 2, 1])
        with mid:
            submitted = st.form_submit_button(
                "🚀 Gerar Avaliação Clínica com IA",
                use_container_width=True,
                type="primary",
            )

    # ── PÓS-SUBMISSÃO (fora do form) ──────────────────────────
    if submitted:
        errors = []
        if not nome.strip():
            errors.append("Nome do paciente")
        if not idade.strip():
            errors.append("Idade")
        if not hma.strip():
            errors.append("HMA")

        if errors:
            st.error(f"⚠️ Campos obrigatórios ausentes: {', '.join(errors)}")
            return

        vitais_str = (
            f"PA: {sv_vals['sv_pa'] or 'NI'} mmHg | "
            f"FC: {sv_vals['sv_fc'] or 'NI'} bpm | "
            f"FR: {sv_vals['sv_fr'] or 'NI'} irpm | "
            f"T°: {sv_vals['sv_temp'] or 'NI'} °C | "
            f"SpO2: {sv_vals['sv_spo2'] or 'NI'} % | "
            f"HGT: {sv_vals['sv_hgt'] or 'NI'} mg/dL | "
            f"Peso: {sv_vals['sv_peso'] or 'NI'} kg"
        )

        acompanhante_info = (
            f"Sim — {acompanhante_nome}" if tem_acompanhante == "Sim"
            else "Não — paciente veio sozinho"
        )

        prompt_text = f"""NOVO ATENDIMENTO — PA CLÍNICA MÉDICA — HOSPITAL GERAL SÃO JOSÉ

═══════════════════════════════════════════
IDENTIFICAÇÃO
═══════════════════════════════════════════
Nome:        {nome.strip()}
Idade:       {idade.strip()}
Sexo:        {sexo}
Acompanhante: {acompanhante_info}

═══════════════════════════════════════════
HISTÓRIA DA MOLÉSTIA ATUAL (HMA)
═══════════════════════════════════════════
{hma.strip()}

═══════════════════════════════════════════
HPP / MEDICAÇÕES / ALERGIAS / HÁBITOS
═══════════════════════════════════════════
{hpp.strip() or "Não informado"}

═══════════════════════════════════════════
SINAIS VITAIS
═══════════════════════════════════════════
{vitais_str}

═══════════════════════════════════════════
EXAME FÍSICO (REALIZADO)
═══════════════════════════════════════════
{exame_fisico.strip() or "Não realizado / Não informado"}

═══════════════════════════════════════════
EXAMES REALIZADOS E RESULTADOS
═══════════════════════════════════════════
{exames.strip() or "Nenhum exame realizado neste momento"}

═══════════════════════════════════════════
CONTEXTO / INFORMAÇÕES ADICIONAIS
═══════════════════════════════════════════
{info_extra.strip() or "Nenhuma informação adicional"}

INSTRUÇÕES PARA A IA:
──────────────────────────────────────────
1. Complete a HISTÓRIA CLÍNICA com o máximo de detalhe (HMA_BOX)
2. Gere um EXAME FÍSICO ESPERADO para este caso (esperado_section dentro de exame_fisico_box)
3. Realize avaliação clínica COMPLETA no formato XML definido
4. Adapte TODA conduta às limitações específicas deste PA
5. A HMA NO PRONTUÁRIO DEVE SER EXPANDIDA E ESTRUTURADA (OPQRST + sintomas associados)
"""

        with st.spinner("🤖 Processando avaliação clínica... Aguarde."):
            history = [{"role": "user", "parts": [prompt_text]}]
            model_name = st.session_state.get("selected_model") or "models/gemini-1.5-flash"
            ai_response = generate_gemini_response(history, model_name)

            if ai_response.startswith("❌") or ai_response.startswith("⚠️"):
                st.error(ai_response)
                return

            history.append({"role": "model", "parts": [ai_response]})

            dados_extras = {
                "idade": idade.strip(),
                "sexo": sexo,
                "acompanhante": acompanhante_info,
                "vitais_iniciais": vitais_str,
            }
            pid = db.criar_paciente(nome.strip(), history, dados_extras)

            st.session_state.current_patient_id = pid
            st.session_state.chat_history = history
            st.session_state.parsed_response = parse_xml_response(ai_response)
            st.session_state.show_form = False

        st.rerun()

# ════════════════════════════════════════════════════════════════
# 11. VISÃO DO PACIENTE — EXPANDERS + CHAT
# ════════════════════════════════════════════════════════════════
def _copy_area(content: str, height: int = 160):
    """Renderiza área de texto pronta para cópia."""
    st.caption("📋 Cópia rápida ↓  (clique · Ctrl+A · Ctrl+C)")
    st.text_area("", value=content, height=height, label_visibility="collapsed")


def render_patient_view():
    pid = st.session_state.current_patient_id
    pdata = db.carregar_paciente(pid)

    if not pdata:
        st.error("❌ Prontuário não encontrado. Recarregue ou selecione outro atendimento.")
        return

    nome = pdata.get("nome", "Paciente")
    data_at = pdata.get("data", "")
    extras = pdata.get("dados_extras", {})
    parsed = st.session_state.parsed_response

    # ── Cabeçalho do paciente ─────────────────────────────────
    h1, h2 = st.columns([3, 1])
    with h1:
        st.markdown(
            f"""
            <div style="background:linear-gradient(90deg,#0a237a,#1565c0);
                        padding:1rem 1.5rem; border-radius:10px;">
                <h3 style="color:white; margin:0; font-size:1.3rem;">👤 {nome}</h3>
                <p style="color:#90caf9; margin:0.2rem 0 0; font-size:0.83rem;">
                    🕐 {data_at} &nbsp;|&nbsp;
                    {extras.get('idade','?')} &nbsp;|&nbsp;
                    {extras.get('sexo','?')} &nbsp;|&nbsp;
                    <span style="font-family:monospace; background:rgba(255,255,255,0.15);
                    padding:1px 5px; border-radius:3px; font-size:0.78rem;">ID: {pid}</span>
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with h2:
        qp = extras.get("queixa", "")
        if qp:
            st.info(f"**QP:** {qp[:90]}{'...' if len(qp) > 90 else ''}")

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Visão Geral ───────────────────────────────────────────
    if "visao_geral" in parsed:
        st.markdown(
            """
            <div style="background:#e8f5e9; border-left:5px solid #2e7d32;
                        padding:0.75rem 1.2rem; border-radius:8px; margin-bottom:0.5rem;">
                <strong style="color:#1b5e20; font-size:0.9rem;">📊 VISÃO GERAL DO CASO</strong>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(parsed["visao_geral"])
        st.divider()

    # ════════════════════════════════════════════════════════
    # EXPANDERS — DOCUMENTAÇÃO ESTRUTURADA
    # ════════════════════════════════════════════════════════
    st.markdown("### 📋 Documentação Estruturada")

    # ─── EXPANDER 1: Avaliação Inicial ───────────────────────
    with st.expander("📄 **1. Avaliação Inicial Completa**", expanded=True):
        t1, t2, t3, t4, t5 = st.tabs([
            "🚨 Situação",
            "📖 HMA",
            "📚 HPP",
            "🔍 Exame Físico",
            "🎯 HD & Conduta",
        ])
        tab_data = [
            (t1, "sit_box"),
            (t2, "hma_box"),
            (t3, "hpp_box"),
            (t4, "exame_fisico_box"),
            (t5, "hd_conduta_box"),
        ]
        for tab, tag in tab_data:
            with tab:
                content = parsed.get(tag, "_Conteúdo não gerado para esta seção._")
                st.markdown(content)
                st.divider()
                _copy_area(content, height=130)

    # ─── EXPANDER 2: Encaminhamento ──────────────────────────
    with st.expander("🚑 **2. Encaminhamento / Transferência (Vaga Zero)**"):
        content = parsed.get("encaminhamento_box", "_Não gerado._")
        na_keywords = ["alta domiciliar", "não necessária", "não indicad", "n/a"]
        is_na = any(kw in content[:150].lower() for kw in na_keywords)

        if is_na:
            st.success("✅ Transferência não indicada para este caso.")
        st.markdown(content)
        if not is_na and content != "_Não gerado._":
            st.divider()
            _copy_area(content, height=280)

    # ─── EXPANDER 3: Alta Domiciliar ─────────────────────────
    with st.expander("🏠 **3. Alta Domiciliar — Receituário & Orientações**"):
        col_rx, col_ori = st.columns(2)

        with col_rx:
            st.markdown("##### 💊 Receituário Médico")
            c_rx = parsed.get("receita_casa_box", "_Não gerado._")
            is_na_rx = any(kw in c_rx[:80].lower() for kw in ["não aplicável", "n/a"])
            if is_na_rx:
                st.info("Alta domiciliar não indicada — receituário não aplicável.")
            st.markdown(c_rx)
            if not is_na_rx and c_rx != "_Não gerado._":
                st.divider()
                _copy_area(c_rx, height=180)

        with col_ori:
            st.markdown("##### 📝 Orientações ao Paciente")
            c_ori = parsed.get("orientacoes_casa_box", "_Não gerado._")
            is_na_ori = any(kw in c_ori[:80].lower() for kw in ["não aplicável", "n/a"])
            if is_na_ori:
                st.info("Alta não indicada — orientações não aplicáveis.")
            st.markdown(c_ori)
            if not is_na_ori and c_ori != "_Não gerado._":
                st.divider()
                _copy_area(c_ori, height=180)

    # ─── EXPANDER 4: Intra-hospitalar (SOMENTE LEITURA) ──────
    with st.expander("🏥 **4. Plano Intra-Hospitalar / Observação**"):
        st.warning(
            "⚠️ **Somente Leitura — Sem cópia rápida** — "
            "Verifique cada medicação e exame antes de prescrever. "
            "Responsabilidade: médico plantonista.",
            icon="⚠️",
        )
        c_ih = parsed.get("intra_hospitalar_box", "_Não gerado._")
        na_ih = any(
            kw in c_ih[:130].lower()
            for kw in ["alta ou transferência", "não necessária", "n/a"]
        )
        if na_ih:
            st.success("✅ Internação/Observação não indicada neste caso.")
        st.markdown(c_ih)
        # ← Sem _copy_area() nesta seção (conforme requisito)

    st.divider()

    # ════════════════════════════════════════════════════════
    # HISTÓRICO DO CHAT
    # ════════════════════════════════════════════════════════
    st.markdown("### 💬 Histórico do Atendimento")

    for i, msg in enumerate(st.session_state.chat_history):
        role = msg["role"]
        parts = msg["parts"]
        txt = parts[0] if isinstance(parts, list) else parts

        if role == "user":
            with st.chat_message("user", avatar="👨‍⚕️"):
                if i == 0:
                    with st.expander("📋 Ver dados do formulário inicial"):
                        st.text(txt)
                    st.caption("_Avaliação inicial solicitada — detalhes acima nos cards_")
                else:
                    # Formata label da interação
                    if txt.startswith("[DÚVIDA"):
                        clean_txt = txt.replace("[DÚVIDA CLÍNICA]", "").strip()
                        st.markdown(f"💬 **Dúvida:** {clean_txt}")
                    elif txt.startswith("[COMPLEMENTO"):
                        line = txt.split("\n")[2] if len(txt.split("\n")) > 2 else txt
                        st.markdown(f"📝 **Complemento:** {line[:200]}")
                    elif txt.startswith("[REAVALIAÇÃO"):
                        line = txt.split("\n")[2] if len(txt.split("\n")) > 2 else txt
                        st.markdown(f"🔄 **Reavaliação:** {line[:200]}")
                    else:
                        st.markdown(txt)

        elif role == "model":
            with st.chat_message("assistant", avatar="🤖"):
                if i == 1:
                    # Primeira resposta: mostrar resumo
                    st.caption("_Avaliação inicial gerada — detalhes nos cards acima_")
                    vg = parsed.get("visao_geral", "")
                    if vg:
                        preview = vg[:400]
                        st.markdown(f"**Resumo:** {preview}{'...' if len(vg) > 400 else ''}")
                    else:
                        clean = strip_xml(txt)
                        st.markdown(clean[:500] + "..." if len(clean) > 500 else clean)
                else:
                    has_xml = any(f"<{tag}>" in txt for tag in KNOWN_TAGS)
                    if has_xml:
                        st.caption("_Prontuário atualizado — verifique os cards acima_")
                        clean = strip_xml(txt)
                        st.markdown(clean[:600] + "..." if len(clean) > 600 else clean)
                    else:
                        st.markdown(txt)

    st.divider()

    # ════════════════════════════════════════════════════════
    # CONTROLES DE INTERAÇÃO
    # ════════════════════════════════════════════════════════
    st.markdown("### ➕ Continuar Atendimento")

    ic1, ic2 = st.columns([2.5, 1])
    with ic1:
        interaction_type = st.radio(
            "Tipo de interação:",
            options=[
                "💬 Dúvida Clínica",
                "📝 Complemento à Avaliação Inicial",
                "🔄 Reavaliação do Paciente",
            ],
            horizontal=True,
            label_visibility="collapsed",
            key="radio_interaction",
        )
    with ic2:
        if "Dúvida" in interaction_type:
            st.info("Resposta direta", icon="💬")
        elif "Complemento" in interaction_type:
            st.warning("Atualiza os cards", icon="📝")
        else:
            st.error("Reavaliação completa", icon="🔄")

    # ── Chat input (sticky no rodapé) ─────────────────────────
    user_input = st.chat_input(
        "Digite sua dúvida, nova informação ou evolução do paciente...",
        key="chat_main_input",
    )

    if user_input:
        if "Dúvida" in interaction_type:
            full_msg = f"[DÚVIDA CLÍNICA]\n\n{user_input}"
            updates_cards = False
        elif "Complemento" in interaction_type:
            full_msg = (
                f"[COMPLEMENTO À AVALIAÇÃO]\n\n"
                f"Novas informações obtidas durante o atendimento:\n"
                f"{user_input}\n\n"
                f"Por favor, integre ao prontuário e atualize no formato XML completo."
            )
            updates_cards = True
        else:
            full_msg = (
                f"[REAVALIAÇÃO DO PACIENTE]\n\n"
                f"Evolução clínica do paciente:\n"
                f"{user_input}\n\n"
                f"Por favor, realize reavaliação completa com base nesta evolução "
                f"e atualize o prontuário no formato XML."
            )
            updates_cards = True

        st.session_state.chat_history.append({"role": "user", "parts": [full_msg]})

        with st.spinner("🤖 Gerando resposta..."):
            model_name = st.session_state.get("selected_model") or "models/gemini-1.5-flash"
            ai_resp = generate_gemini_response(st.session_state.chat_history, model_name)

        if ai_resp.startswith("❌") or ai_resp.startswith("⚠️"):
            st.error(ai_resp)
            st.session_state.chat_history.pop()
        else:
            st.session_state.chat_history.append({"role": "model", "parts": [ai_resp]})

            if updates_cards:
                new_parsed = parse_xml_response(ai_resp)
                if new_parsed:
                    st.session_state.parsed_response = new_parsed

            db.atualizar_historico(pid, st.session_state.chat_history)
            st.rerun()

# ════════════════════════════════════════════════════════════════
# 12. ENTRY POINT
# ════════════════════════════════════════════════════════════════
def main():
    configure_gemini()

    if not st.session_state.logged_in:
        render_landing_page()
        return

    # Sidebar sempre visível após login
    render_sidebar()

    # Conteúdo principal
    if st.session_state.show_form:
        render_form()
    elif st.session_state.current_patient_id:
        render_patient_view()
    else:
        render_welcome()


main()
