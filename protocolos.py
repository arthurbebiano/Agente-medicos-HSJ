"""
protocolos.py
Base de conhecimento clínico-institucional do PA.
Hospital Geral São José — Contagem/MG
"""

PROTOCOLOS_TEXTO = """
╔═══════════════════════════════════════════════════╗
║  CONTEXTO REAL DA UNIDADE — HOSPITAL GERAL SÃO JOSÉ        ║
║  Pronto Atendimento — Clínica Médica — Contagem/MG         ║
╚═══════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EQUIPE MÉDICA DISPONÍVEL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Clínico Geral: UM médico, sozinho, responsável por TODOS os casos de
clínica médica do PA simultaneamente. É quem usa este sistema.

Cirurgião Geral: Disponível presencialmente para casos triados para cirurgia
(abdome agudo, trauma, procedimentos). Pode estar ausente em alguns plantões
por falta de cobertura. Nunca assuma disponibilidade garantida.

Pediatra: Disponível presencialmente para atendimentos pediátricos triados.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EXAMES DISPONÍVEIS — DOIS NÍVEIS MUITO DIFERENTES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NÍVEL 1 — POINT OF CARE (RESULTADO EM MINUTOS, NA SALA DE EMERGÊNCIA):

  Gasometria arterial ou venosa — inclui obrigatoriamente:
    pH, pCO2, pO2, HCO3, BE, SatO2, Lactato, Glicose,
    Sódio (Na+), Potássio (K+), Cálcio iônico (Ca2+),
    Hemoglobina (Hb) e Hematócrito (Ht)

  Troponina quantitativa
  Dímero-D quantitativo
  EAS / Urina rotina — ATENÇÃO: apenas fita reativa (bioquímica).
    NÃO inclui sedimento urinário nem microscopia.
    Disponível: proteína, glicose, cetonas, sangue, nitritos,
    esterase leucocitária, urobilinogênio, bilirrubina, pH urinário.

  Testes Rápidos (qualitativo, resultado imediato):
    Beta-hCG
    Dengue NS1
    Influenza A e B
    Outros virais variados conforme disponibilidade no estoque

NÍVEL 2 — LABORATÓRIO EXTERNO (RESULTADO EM HORAS — 3 a 8h):

  Hemograma completo
  PCR (Proteína C-Reativa)
  Ureia e Creatinina
  Eletrólitos completos (quando necessário além da gasometria)
  TGO, TGP, GamaGT, Fosfatase Alcalina, Bilirrubinas totais e frações
  Amilase e Lipase
  Coagulograma (TP/INR, TTPA)
  Qualquer outro exame laboratorial de sangue de rotina

  IMPACTO CLÍNICO CRÍTICO: Pacientes cuja alta ou internação depende
  desses resultados precisam permanecer em observação, recebendo
  tratamento empírico e sintomático, até a liberação dos laudos.
  Isso é uma realidade operacional deste PA, não uma falha de conduta.

IMAGEM — INTERPRETAÇÃO PELO PRÓPRIO PLANTONISTA:

  ECG 12 derivações: laudado pelo médico plantonista na hora
  Radiografia simples (Tórax, Abdome): laudada pelo médico plantonista
  Tomografia Computadorizada: EXCLUSIVAMENTE SEM CONTRASTE.
    Laudo do radiologista é muito demorado. À noite, não há radiologista.
    A interpretação da TC bruta é feita exclusivamente pelo plantonista
    ou em avaliação conjunta com o cirurgião geral (quando disponível).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RACIOCÍNIO COM RECURSOS ESCALONADOS — PRINCÍPIO FUNDAMENTAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Para cada caso, raciocine em três horizontes de tempo:

  AGORA (minutos): O que você decide com gasometria, troponina, dímero-D,
  EAS fita, testes rápidos, ECG, RX e exame clínico. A maioria das decisões
  urgentes pode e deve ser tomada com esses recursos.

  EM 1 A 3 HORAS: Resultados dos POCT já disponíveis. Reavalie a hipótese,
  ajuste a conduta e documente a reavaliação.

  EM 3 A 8 HORAS: Laboratório externo disponível. Casos que genuinamente
  precisam de hemograma, PCR ou enzimas para decisão de alta ou internação
  devem ser ancorados na observação com tratamento empírico enquanto aguardam.
  Não há vergonha nisso. É o fluxo correto desta unidade.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROTOCOLO 01 — DOR TORÁCICA E SÍNDROME CORONARIANA AGUDA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ECG obrigatório nos primeiros 10 minutos de qualquer dor torácica.
Troponina disponível imediatamente — coletar no primeiro contato.

IAMCSST (supra ST ≥ 1mm em ≥ 2 derivações contíguas ou BRE novo):
  Oxigênio máscara/cateter APENAS se SpO2 < 90%.
  Morfina 2-4mg IV se dor refratária e PAS > 90mmHg (evitar se possível, reduz absorção de antiplaquetários).
  Nitrato 0,4mg SL se PAS > 90mmHg, repetir 3x a cada 5min (evitar se infarto de VD ou uso de sildenafila).
  AAS 300mg VO mastigado.
  Clopidogrel 300mg VO (ou 600mg se for submetido a angioplastia primária imediata e idade < 75).
  HNF bolus 60 UI/kg IV (máx 4000 UI) + infusão 12 UI/kg/h.
  ACIONAR VAGA ZERO PARA HEMODINÂMICA DE IMEDIATO.

IAMSST / NSTEMI (troponina elevada ou ECG com alterações isquêmicas):
  AAS 300mg mastigado + Clopidogrel 300mg VO.
  Enoxaparina 1mg/kg SC de 12/12h.
  Troponina seriada 0h e 3h.
  Transferência urgente se troponina positiva, dor refratária ou instabilidade.
  Se troponina negativa em 2 coletas e ECG sem isquemia aguda: alta com
  encaminhamento urgente para cardiologia ambulatorial.

Dor torácica de baixo risco (HEART score ≤ 3):
  Observação 3-6h, troponina seriada.
  Alta com orientações e retorno ambulatorial se troponinas negativas.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROTOCOLO 02 — TROMBOEMBOLIA PULMONAR E TVP (COM DÍMERO-D DISPONÍVEL)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Score de Wells para TEP — calcule sempre que suspeitar:
  Sinais clínicos de TVP: +3
  TEP mais provável que diagnóstico alternativo: +3
  FC > 100bpm: +1,5
  Imobilização ou cirurgia nas últimas 4 semanas: +1,5
  TVP ou TEP prévia documentada: +1,5
  Hemoptise: +1
  Neoplasia ativa (em tratamento ou nos últimos 6 meses): +1

  Wells ≤ 4 (baixa probabilidade): Solicitar Dímero-D.
    Dímero-D negativo → TEP improvável → investigar diagnóstico alternativo.
    Dímero-D positivo → investigação adicional necessária.
    TC de tórax SEM contraste tem baixa sensibilidade para TEP.
    Se forte suspeita clínica com dímero positivo: anticoagulação empírica
    + transferência para TC com contraste (AngioTC) ou cintilografia.

  Wells > 4 (alta probabilidade): Dímero-D não é útil aqui.
    Anticoagulação empírica imediata: Enoxaparina 1mg/kg SC de 12/12h.
    Transferência para confirmação por imagem adequada.
    Se instabilidade hemodinâmica (TEP maciça/PAS < 90): suporte hemodinâmico,
    trombólise sistêmica se disponível e sem contraindicações antes de transferir.

Score de Wells para TVP:
  Neoplasia ativa: +1
  Paralisia, paresia ou imobilização recente de MMII: +1
  Acamado > 3 dias ou cirurgia nas últimas 12 semanas: +1
  Dor localizada ao longo do trajeto venoso profundo: +1
  Edema de toda a perna: +1
  Edema de panturrilha > 3cm comparado ao contralateral: +1
  Edema depressível apenas no membro sintomático: +1
  Colaterais venosas superficiais (não varicosas): +1
  Diagnóstico alternativo pelo menos tão provável: -2

  Score ≤ 1: baixa probabilidade → Dímero-D.
    Dímero-D negativo → TVP improvável.
    Dímero-D positivo → US doppler (não disponível aqui) → transferência.
  Score ≥ 2: probabilidade moderada a alta → anticoagular empiricamente +
    transferência para US doppler venoso.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROTOCOLO 03 — DISPNEIA AGUDA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Gasometria e ECG são os exames centrais na dispneia.

Edema Agudo de Pulmão (Cardiogênico):
  Posição ortostática ou semissentado. Oxigênio meta SpO2 > 90%.
  VNI (CPAP ou BiPAP) se disponível é a medida mais impactante.
  Nitrato SL 0,4mg se PAS > 100mmHg, repetir 3x a cada 5min. Considerar Nitroglicerina IV se grave.
  Furosemida 40-80mg IV lento (ou dobrar a dose oral habitual do paciente).
  Morfina: ATUALMENTE CONTRAINDICADA de rotina. Uso de extrema exceção.
  ECG e Troponina para afastar SCA como causa.
  Gasometria para avaliar gravidade. Transferência para UTI se refratário ou IOT.

Exacerbação de DPOC ou asma grave:
  Oxigênio controlado: 1-2L/min cateter nasal, meta SpO2 88-92% no DPOC; >90% asma.
  Salbutamol 5mg + Ipratrópio 0,5mg nebulização, repetir 3x a cada 20min.
  Dexametasona 10mg IV ou Metilprednisolona 125mg IV (ou Prednisona 40-50mg VO).
  Asma grave refratária: Sulfato de Magnésio 2g IV em 20min.
  AMINOFILINA É PROSCRITA na exacerbação aguda (alta toxicidade, sem benefício).
  Se DPOC com 2 dos 3 (aumento dispneia, volume do escarro, purulência) ou VNI/IOT:
    Ceftriaxona 1-2g IV + Azitromicina (apenas se for internar/transferir) ou Amoxicilina-Clavulanato VO se alta.
  Transferência se pCO2 > 55 com acidose (pH < 7,30), alteração de consciência ou falha na terapia.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROTOCOLO 04 — HIPERTENSÃO ARTERIAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Urgência hipertensiva (PA > 180/120 sem lesão de órgão-alvo aguda):
  Captopril 25mg SL ou VO, repetir em 30-60min se necessário.
  Clonidina 0,1mg VO (ação mais lenta). Não usar em bradicardia.
  Meta: redução gradual nas próximas 24-48h. NÃO forçar queda rápida no PA.
  Observação. Alta com ajuste da medicação habitual e retorno ambulatorial.

Emergência hipertensiva (PA elevada com lesão de órgão-alvo aguda confirmada):
  Nitroprussiato de Sódio: 50mg em 250mL SG5% = 200 mcg/mL.
    Proteger da luz com papel alumínio no frasco e equipo.
    Iniciar 0,5 mcg/kg/min em bomba de infusão, titular até atingir a meta.
  Meta geral: redução máxima de 20-25% da PAM na primeira hora, depois 160/100 em 2-6h.
  (Exceções: Dissecção de Aorta exige alvo PAS < 120 imediato; AVCi tem alvos permissivos).
  Transferência imediata para UTI.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROTOCOLO 05 — AVC AGUDO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TC de crânio sem contraste é a prioridade absoluta (afastar sangramento).
Plantonista avalia TC: Sangramento é hiperdenso (branco). Isquemia inicial pode ser tomograficamente normal.

  ABC, oxigênio apenas se SpO2 < 94%. Cabeceira a 0-15 graus se isquêmico sem HIC, 30 graus se hemorrágico.
  HGT imediato. Hipoglicemia simula AVC → SG50% 50mL IV imediatamente se < 60 mg/dL.
  ECG para FA.
  PA no AVC Isquêmico: NÃO reduzir a menos que PAS > 220 ou PAD > 120.
    Se candidato a trombólise (rt-PA): reduzir para < 185/110 antes de infundir.
  Antitérmico se febre (temperatura > 37,5 piora desfecho neurológico).
  Janela para trombólise: até 4,5h do ictus (ou do último horário visto bem).
    Transferência VAGA ZERO para centro de AVC mantendo a janela aberta.
  AVC Hemorrágico (TC confirmada): Meta PA PAS 140-180 com Nitroprussiato IV. Transferência para neurocirurgia/UTI.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROTOCOLO 06 — GRAVIDEZ, BETA-hCG E EMERGÊNCIAS OBSTÉTRICAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Beta-hCG rápido obrigatório em toda mulher em idade fértil com:
  Dor abdominal/pélvica inexplicada, sangramento vaginal, síncope/hipotensão.

Beta-hCG positivo com dor abdominal/pélvica (Suspeita de Ectópica):
  Se instável hemodinamicamente: Choque hemorrágico. 2 acessos calibrosos,
    Ringer/SF0,9% em bolus, acionar cirurgião geral do PA, TC de abdome/pelve sem
    contraste rápida (busca de hemoperitônio). Transferência VAGA ZERO gineco/cirurgia.
  Se estável: TC abdome/pelve sem contraste (avalia massa anexial ou líquido livre),
    manter em observação estrita e providenciar transferência para ginecologia.

Beta-hCG positivo sem dor, sem instabilidade (ex: sangramento leve):
  Ameaça de abortamento, abortamento em curso.
  Alta com orientações de sinais de alarme se sangramento cessar. Seguimento ambulatorial/USG eletivo.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROTOCOLO 07 — DENGUE E ARBOVIROSES (COM NS1 DISPONÍVEL)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NS1 indicado: febre ≤ 5 dias com quadro suspeito (mialgia, cefaleia retro-orbitária).

Dengue Grupo A (Sem sinais de alarme, sem comorbidades/risco):
  Hidratação VO generosa (adultos 60ml/kg/dia, sendo 1/3 SRO).
  Paracetamol ou Dipirona. NUNCA AAS ou AINEs. Alta para UBS.

Dengue Grupo B (Sem sinais de alarme, MAS com sangramento de pele/comorbidades/gestante):
  Hemograma obrigatório. Hidratação VO ou IV supervisionada enquanto aguarda.

Dengue Grupo C (Com sinais de alarme):
  Sinais: Dor abdominal intensa, vômitos persistentes, letargia, sangramento de mucosas,
  aumento de hematócrito com queda de plaquetas, hipotensão postural.
  Conduta IMEDIATA: Hidratação IV Ringer/SF0,9% 10 mL/kg em 1 hora.
  Reavaliar clínica e repetir hemograma (externo). Se não melhorar, repetir fase de expansão.
  Ancorar paciente em observação estrita.

Dengue Grupo D (Dengue Grave/Choque):
  Hidratação IV Ringer/SF0,9% 20 mL/kg em até 20 minutos. Repetir se necessário.
  Acionar transferência para UTI urgente.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROTOCOLO 08 — INFLUENZA E SÍNDROME GRIPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Teste rápido para Influenza (swab) se disponível para pacientes de risco.

Pacientes de Risco (Idosos > 60, crianças < 5, gestantes, puérperas, imunodeprimidos,
cardiopatas, pneumopatas, obesidade IMC > 40) OU com SRAG (Síndrome Respiratória Aguda Grave):
  Oseltamivir 75mg VO 12/12h por 5 dias. MAIOR benefício se iniciado nas primeiras 48h.
  NÃO aguardar resultado de teste para iniciar Oseltamivir se alta suspeição e paciente grave/risco.
  Tratamento de suporte. Avaliar Gasometria e RX se SRAG (SpO2 < 93%, taquipneia).

Pacientes fora do grupo de risco sem sinais de gravidade:
  Tratamento puramente sintomático. Alta com orientações.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROTOCOLO 09 — ANAFILAXIA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Adrenalina (Epinefrina) é a PRIMEIRA e mais importante medicação.
  Dose: 0,3 a 0,5 mg IM no vasto lateral da coxa. Repetir a cada 5-15 min se sem resposta.
  NÃO atrasar adrenalina aguardando anti-histamínicos ou corticoides.

Hipotensão/Choque: Decúbito dorsal, elevação de MMII. Ressuscitação volêmica rápida IV (SF0,9%).
Broncoespasmo: Salbutamol nebulização (após adrenalina IM).
Terapias de 2ª linha (complementares, não salvam a vida isoladamente):
  Difenidramina 25-50mg IV/IM ou Prometazina.
  Metilprednisolona 125mg IV ou Dexametasona 10mg IV (previne reação bifásica, ação lenta).

Observação: mínimo de 6-8 horas após reversão, devido ao risco de anafilaxia bifásica.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROTOCOLO 10 — CRISE CONVULSIVA E STATUS EPILEPTICUS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Fase 1 (0-5min): Proteção via aérea, decúbito lateral, oxigênio.
  HGT imediato: se hipoglicemia (<60), fazer SG50% 50mL IV.

Fase 2 (5-20min - Abortar crise): Benzodiazepínico.
  Diazepam 10mg IV (velocidade máx 2-5mg/min) ou Midazolam 10mg IM (se sem acesso).
  Pode repetir após 5 minutos. Atenção ao risco de depressão respiratória.

Fase 3 (20-40min - Prevenção de nova crise/Status):
  Fenitoína 20mg/kg IV. DILUIR APENAS EM SF 0,9% (precipita em glicosado).
  Velocidade MÁXIMA de 50mg/min (ideal 25mg/min) para evitar arritmia e hipotensão.

Fase 4 (Status refratário > 40min):
  Fenobarbital 20mg/kg IV (velocidade 50-100mg/min).
  Preparar IOT e acionar UTI imediata.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROTOCOLO 11 — CETOACIDOSE DIABÉTICA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Diagnóstico (Gasometria + POC): HGT > 250 + pH < 7,30 + HCO3 < 18 + Cetonúria(fita).

1. Hidratação (Pilar Inicial): SF 0,9% 1000mL a 1500mL na 1ª hora.
   Depois 250-500mL/h. Trocar para SG5% (ou 50/50) quando HGT atingir 200-250 mg/dL.

2. Potássio (Avaliar Gasometria ANTES da Insulina):
   K+ < 3,3 mEq/L: NÃO iniciar insulina. Fazer reposição (20-40mEq/h) até K > 3,3.
   K+ 3,3 a 5,2 mEq/L: Repor K+ (20-30mEq/L de soro) JUNTO com insulina.
   K+ > 5,2 mEq/L: Iniciar insulina, aguardar para repor K+.

3. Insulina Regular (Após garantir K > 3,3):
   Bomba de infusão: 0,1 UI/kg em bolus IV seguido de 0,1 UI/kg/hora contínuo.
   (Diluição padrão: 50 UI Regular em 50mL SF = 1 UI/mL).
   Meta de queda: 50 a 70 mg/dL por hora no HGT.

4. Bicarbonato: APENAS se pH < 6,9 (100 mEq em 400mL AD + 20mEq KCl em 2h).
Transferência urgente para UTI em casos graves (pH < 7,0, rebaixamento).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROTOCOLO 12 — SEPSE E CHOQUE SÉPTICO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Triagem rápida: NEWS ou qSOFA (FR ≥ 22, Glasgow < 15, PAS ≤ 100).
Disfunção confirmada por Lactato ≥ 2 mmol/L na gasometria.
NÃO AGUARDAR HEMOGRAMA/PCR PARA INICIAR TRATAMENTO.

Pacote da 1ª Hora:
  1. Coletar Gasometria (Lactato).
  2. Coletar culturas (Hemocultura se disponível, EAS se foco urinário).
  3. Antibioticoterapia Empírica Ampla IMEDIATA (Não atrasar se falha na cultura):
     Foco Pulmonar: Ceftriaxona 2g IV + Azitromicina 500mg IV.
     Foco Urinário: Ceftriaxona 2g IV (ou Ciprofloxacino se anafilaxia).
     Foco Abdominal: Ceftriaxona 1g IV + Metronidazol 500mg IV.
     Foco Indefinido: Ceftriaxona 2g IV + Metronidazol (cobrir gram-negativos, anaeróbios).
  4. Ressuscitação Volêmica: 30 mL/kg de Cristaloides (SF0,9% ou Ringer) nas primeiras 3h se hipotensão ou lactato elevado.

Choque Séptico: PAS < 90 ou PAM < 65 APÓS expansão inicial de 30mL/kg.
  Iniciar Vasopressor: Norepinefrina (0,01 a 3 mcg/kg/min).
  Meta: PAM ≥ 65 mmHg. Transferência Imediata UTI.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROTOCOLO 13 — DOR ABDOMINAL AGUDA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Beta-hCG Fita obrigatório para mulheres em idade fértil (Protocolo 06).

Avaliação Cirúrgica:
  Acionar cirurgião presencial para abdome em tábua, descompressão brusca positiva, dor em FID típica, suspeita de isquemia mesentérica.

Analgesia: NÃO mascara o diagnóstico cirúrgico em níveis clinicamente relevantes. O paciente tem direito ao alívio.
  Leve/Moderada: Dipirona 1g IV; Buscopan Composto IV.
  Forte: Tramadol 50-100mg IV (diluído, infusão lenta). Morfina para casos intensos avaliados.

Exames complementares baseados na disponibilidade:
  EAS Fita para afastar ITU ou sugerir litíase (sangue).
  TC Abdome Sem Contraste: Útil para identificar pneumoperitônio, litíase ureteral e quadros obstrutivos evidentes. Tem limitação para apendicite inicial e isquemia.
  Ancorar paciente no PA se o laudo do hemograma (horas) for estritamente necessário para decidir conduta clínica (ex: desvio à esquerda em suspeita de apendicite sem TC clara).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROTOCOLO 14 — ARRITMIAS CARDÍACAS (ABORDAGEM AVANÇADA ACLS)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PASSO 1: IDENTIFICAR INSTABILIDADE HEMODINÂMICA (Apenas 1 critério basta)
  1. Hipotensão (PAS < 90 ou queda abrupta)
  2. Alteração aguda do nível de consciência
  3. Dor torácica isquêmica (angina) refratária
  4. Insuficiência Cardíaca Aguda (Edema Agudo de Pulmão)
  5. Sinais de choque (sudorese, palidez, má perfusão, lactato elevado)

>>> SE INSTÁVEL: CARDIOVERSÃO ELÉTRICA SINCRONIZADA (CVE) IMEDIATA
  - Analgesia/Sedação Breve (se o paciente estiver consciente e a PA permitir):
    Fazer Midazolam 3-5mg IV lento + Fentanil ou Morfina 2mg IV.
  - Ligar o botão "SYNC" ou "Sincronizar" no desfibrilador. Reconhecer a "bandeira" sobre cada QRS.
  - FA (Fibrilação Atrial): 120-200J (bifásico).
  - Flutter / TSV (Taquicardia Supraventricular): 50-100J.
  - TV Monomórfica (Taquicardia Ventricular): 100J.
  - TV Polimórfica (Torsades de Pointes) ou FV: NÃO SINCRONIZAR. Desfibrilação direta 200J.

>>> SE ESTÁVEL: AVALIAR QRS E REGULARIDADE PELO ECG/MONITOR

1. TAQUICARDIA DE QRS ESTREITO E REGULAR (Ex: TSV, TRN)
  - 1ª Linha: Manobra Vagal. A mais eficaz é a Valsalva Modificada: pedir ao paciente para soprar uma seringa de 10mL por 15 segundos para mover o êmbolo e, imediatamente a seguir, deitá-lo elevando passivamente suas pernas a 45 graus.
  - 2ª Linha: Adenosina. Exige técnica correta. Usar acesso venoso calibroso (proximal, ex: antecubital) conectado a uma torneirinha de 3 vias.
    Dose: 6mg em bolus EXTREMAMENTE RÁPIDO (1 a 2 segundos) empurrado imediatamente por um flush de 20mL de SF 0,9%. Elevar o membro após a injeção.
    Se não reverter em 1-2 minutos: Fazer Adenosina 12mg IV na mesma técnica.
  - 3ª Linha (refratários ou contraindicação à Adenosina): Metoprolol 5mg IV lento (1mg/min). Pode repetir a cada 5min até 15mg.

2. TAQUICARDIA DE QRS ESTREITO E IRREGULAR (Ex: FA, Flutter com BAV variável)
  - Foco absoluto no Pronto Atendimento: CONTROLE DA FREQUÊNCIA (Meta FC < 110 bpm).
  - Controle de Frequência (Se PA normal ou alta): Metoprolol 5mg IV lento. Pode repetir a cada 5 minutos (Máximo de 3 doses / 15mg).
  - Controle de Frequência (Se PA limítrofe ou Disfunção de VE/IC conhecida): Digoxina 0,5mg IV (fazer meia ampola, aguardar, se necessário mais 0,25 a cada 6h, até máx 1mg) OU Amiodarona 300mg IV em 1 hora.
  - Controle de Ritmo (Reversão Química para Ritmo Sinusal): Só deve ser feita no PA se houver CERTEZA ABSOLUTA de que os sintomas começaram há < 48h. Droga: Amiodarona (150mg IV em 10min). Na dúvida temporal, apenas controle a frequência e encaminhe.
  - Anticoagulação: Avaliar CHADS2-VASc para decisão de longo prazo, mas focar na estabilização ágil no PA.

3. TAQUICARDIA DE QRS LARGO E REGULAR (Ex: TV Monomórfica)
  - REGRAS DE OURO: Toda Taquicardia de QRS Largo é Taquicardia Ventricular (TV) até prova em contrário (especialmente em pacientes idosos ou coronariopatas). NUNCA faça verapamil, diltiazem ou adenosina na dúvida diagnóstica se houver história de cardiopatia estrutural.
  - Conduta: Amiodarona 150mg IV. Diluir em 100mL de SG5% e infundir em 10 minutos (10 mL/min).
  - Pode repetir a dose de 150mg em 10 minutos se não houver reversão.
  - Se houver reversão, manter infusão contínua: 1mg/min por 6 horas.
  - Em caso de falha da Amiodarona: CVE Eletiva (sedar e chocar com 100J).

4. TAQUICARDIA DE QRS LARGO E IRREGULAR
  - Pode tratar-se de uma FA com aberrância de condução (BRE prévio) ou uma FA pré-excitada (paciente com Síndrome de Wolff-Parkinson-White).
  - ALERTA MÁXIMO: NUNCA administre bloqueadores do nó AV (Adenosina, Metoprolol, Digoxina, Verapamil) se suspeitar de FA com WPW. Bloquear o nó AV força toda a condução elétrica a descer pela via acessória, degenerando rapidamente para Fibrilação Ventricular e PCR. Tratamento seguro: Amiodarona IV ou CVE.
  - Se o traçado for padrão Torsades de Pointes (TV Polimórfica com histórico de intervalo QT longo): Administrar Sulfato de Magnésio 2g IV. Diluir em 50-100mL de SG5% e correr em 15 minutos.

5. BRADIARRITMIAS SINTOMÁTICAS (FC < 50 bpm)
  - Sintomas: síncope, pré-síncope, angina, dispneia intensa ou hipotensão.
  - 1ª Linha: Atropina 1mg IV em bolus Rápido (Atenção: A dose do ACLS 2020 mudou de 0,5mg para 1mg). Pode repetir a cada 3 a 5 min até dose máxima de 3mg (3 ampolas).
    *CUIDADO: A Atropina costuma ser ineficaz em transplantados cardíacos e falha frequentemente nos BAV de 2º Grau Mobitz II e BAV Total (BAVT). Nestes casos, não retarde o início da terapia de 2ª linha.
  - 2ª Linha (Drogas Vasoativas como ponte para o Marcapasso):
    Dopamina: Infusão de 5 a 20 mcg/kg/min (titular pela PA e FC).
    Adrenalina: Infusão de 2 a 10 mcg/min. Macete de preparo: 1 ampola (1mg) em 250mL de SG5% ou SF 0,9% = concentração de 4 mcg/mL. Iniciar em 30 mL/h e titular.
  - 3ª Linha (Definitiva dentro do PA): Marcapasso Transcutâneo (MPTC).
    - O MPTC causa contrações musculares torácicas severas. Exige sedação/analgesia contínua (ex: Fentanil ou Midazolam + Morfina), exceto se o paciente estiver profundamente torporoso/comatoso.
    - Ligar o modo Marcapasso no monitor/desfibrilador. Ajustar a FC alvo para 60-70 bpm.
    - Aumentar a corrente (mA) até haver "captura" (uma espícula reta seguida imediatamente por um QRS largo e onda T invertida, associada a um pulso central palpável compatível com a FC do monitor). Geralmente captura entre 50 e 90 mA. Fixar a corrente de manutenção 2 mA acima do limiar de captura.
    - Acionar transferência urgente (Vaga Zero) para implante de Marcapasso Transvenoso/Definitivo.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROTOCOLO 15 — IST E INFECÇÕES GENITURINÁRIAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Infecção do Trato Urinário Baixa (Cistite Não Complicada em Mulher):
  Diagnóstico: Eminentemente clínico. EAS fita (nitritos/esterase)
  reservado para casos de dúvida clínica. Sem microscopia disponível aqui.
  Primeira Linha: Fosfomicina trometamol 3g VO dose única OU
  Nitrofurantoína 100mg VO 6/6h por 5 dias.
  ATENÇÃO: NÃO usar SMX/TMP empiricamente (alta resistência no Brasil).
  ATENÇÃO: NÃO usar Ciprofloxacino para cistite (reservar para pielonefrite).

Pielonefrite Aguda Não Complicada (Sem sepse, tolerando VO):
  Ciprofloxacino 500mg VO 12/12h por 7 dias.
  Avaliar 1ª dose IV no PA. Hidratação e observação se vômitos até tolerar VO.

Gonorreia e Clamídia (Cervicite/Uretrite):
  Ceftriaxona 500mg IM dose única (liberado sem internação neste cenário) +
  Azitromicina 1g VO dose única (ou Doxiciclina 100mg 12/12h 7 dias).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROTOCOLO PEDIÁTRICO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Pediatra disponível — acionar para TODOS os casos pediátricos triados.
Se pediatra ausente naquele plantão, condutas básicas de retaguarda:

Febre: Paracetamol 10-15mg/kg/dose VO a cada 6h.
  Ibuprofeno 5-10mg/kg/dose VO a cada 8h (acima de 6 meses).
  Dipirona 10-15mg/kg/dose VO ou IV. NUNCA AAS em crianças (Sd. de Reye).

Desidratação leve/moderada: Terapia de Reidratação Oral (SRO).
Desidratação grave/Choque: Bolus de SF0,9% ou Ringer 20 mL/kg IV rápido.

Broncoespasmo (Asma): Salbutamol 1 gota/3kg (ou spray com espaçador 4-8 jatos) a cada 20min.
  Corticoide: Prednisolona 1-2mg/kg VO (máx 40mg).

Manutenção venosa (Holliday-Segar):
  < 10kg: 100 mL/kg/dia.
  10-20kg: 1000 mL + 50 mL/kg (para cada kg acima de 10).
  > 20kg: 1500 mL + 20 mL/kg (para cada kg acima de 20).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FARMÁCIA DO PA — MEDICAMENTOS DISPONÍVEIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Analgésicos/Antitérmicos: Dipirona, Paracetamol, Ibuprofeno, Cetoprofeno,
Tenoxicam, Tramadol, Morfina, AAS.

Antibióticos Injetáveis: Penicilina Benzatina, Ceftriaxona (para gonorreia ou pacientes em esquema de transferência), Azitromicina IV, Metronidazol IV.

Cardiovasculares IV: Adrenalina, Norepinefrina, Dopamina, Amiodarona,
Adenosina, Atropina, Nitroprussiato, Furosemida, Metoprolol, Digoxina.

Cardiovasculares VO: AAS, Clopidogrel, Captopril, Metoprolol, Furosemida, Clonidina, Nitrato SL.

Anticoagulantes: Enoxaparina SC, HNF.

Neurológico: Diazepam, Midazolam, Fenitoína, Fenobarbital, Haloperidol.

Endocrinologia: Insulina Regular, Insulina NPH, SG50%, SG10%.

Alérgico/Respiratório: Difenidramina, Prometazina, Dexametasona,
Metilprednisolona, Salbutamol, Ipratrópio, Sulfato de Magnésio.

Gastro: Ondansetrona, Metoclopramida, Pantoprazol, Omeprazol, Buscopan.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CRITÉRIOS DE TRANSFERÊNCIA IMEDIATA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Transferir SEM hesitar via regulação (Vaga Zero quando aplicável):
IAMCSST, Choque cardiogênico, Choque séptico refratário a fluidos,
AVC em janela para trombólise ou AVC hemorrágico, TEP com instabilidade,
Status epilepticus refratário, CAD grave com pH < 7,0, Necessidade de
Intubação Orotraqueal, Abdome Agudo Cirúrgico, Gravidez Ectópica Rota,
Bloqueio Atrioventricular de Alto Grau, Taquicardias instáveis e MPTC.
"""
