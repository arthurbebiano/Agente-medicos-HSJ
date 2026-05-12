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
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROTOCOLO 01 — DOR TORÁCICA E SÍNDROME CORONÁRIA AGUDA (SCA)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

A prioridade é o tempo: ECG obrigatório nos primeiros 10 minutos de qualquer dor torácica.
Troponina quantitativa POC disponível imediatamente — colher no primeiro contacto.

IAMCSST (Infarto com Supra de ST ≥ 1mm em ≥ 2 derivações contíguas ou BRE novo):
  >>> ACIONAR VAGA ZERO PARA HEMODINÂMICA DE IMEDIATO.
  
  Oxigénio: Máscara/cateter APENAS se SpO2 < 90% ou franco desconforto respiratório.
  AAS: 300mg VO mastigado (ação rápida).
  Clopidogrel: 
    - < 75 anos: 300mg VO (ou 600mg se for direto para angioplastia primária).
    - ≥ 75 anos: 75mg VO (sem dose de carga).
  Anticoagulação (Enoxaparina é preferível à HNF no PA pela facilidade):
    - < 75 anos: 30mg IV em bolus RÁPIDO, seguido de 1mg/kg SC de 12/12h.
    - ≥ 75 anos: SEM bolus IV. Apenas 0,75mg/kg SC de 12/12h.
  Nitrato (Isossorbida 5mg SL ou Nitroglicerina IV):
    - CONTRAINDICAÇÕES ABSOLUTAS: PAS < 90 mmHg, Frequência Cardíaca < 50 ou > 100 bpm, 
      uso de inibidores da fosfodiesterase (Sildenafila nas últimas 24h ou Tadalafila em 48h),
      ou suspeita de Enfarte de Ventrículo Direito (supra de parede inferior: DII, DIII, aVF 
      -> obrigatório fazer V3R e V4R antes do nitrato).
  Morfina (2-4mg IV): 
    - EVITAR POR ROTINA. Atrasa a absorção dos antiagregantes. 
    - Usar estritamente para dor excruciante refratária ao nitrato, com estabilidade hemodinâmica.

IAMSST / NSTEMI (Sem supra, mas com troponina elevada ou alterações isquémicas):
  AAS 300mg mastigado + Clopidogrel 300mg VO.
  Enoxaparina 1mg/kg SC de 12/12h (Ajuste: se CrCl < 30, fazer 1mg/kg SC 1x ao dia / 24h).
  Troponina seriada (0h e 1-3h).
  Transferência urgente para cardiologia se troponina positiva, dor refratária, ou instabilidade clínica.
  Se troponina negativa nas coletas seriadas e ECG sem isquémia aguda: avaliar Score HEART para alta.

Dor torácica de baixo risco (Score HEART ≤ 3):
  Observação 3-6h com troponina seriada. 
  Alta com orientações e retorno ambulatorial (teste de isquémia eletivo) se resultados negativos.

ALERTA DE DIAGNÓSTICO DIFERENCIAL (Dissecção da Aorta):
  Dor torácica "rasgante" irradiada para o dorso + assimetria de pulsos ou de PA nos membros.
  NÃO DAR AAS OU ANTICOAGULANTE. Controlo rigoroso da FC e PA (Esmolol ou Metoprolol IV + Nitroprussiato).
  TRANSFERÊNCIA PRIORIDADE VAGA 0.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROTOCOLO 02 — TROMBOEMBOLIA PULMONAR (TEP) E TVP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Neste PA, a TC é SEM contraste (baixa sensibilidade para TEP). Dependemos criticamente da clínica (Score de Wells) e do Dímero-D (POC) para decidir quem tratar ou transferir.

PASSO 1: AVALIAR O RISCO CLÍNICO PARA TEP (Score de Wells)
  Sinais clínicos de TVP (edema assimétrico, dor à palpação): +3
  TEP mais provável que diagnóstico alternativo: +3
  Frequência Cardíaca > 100 bpm: +1,5
  Imobilização (> 3 dias) ou cirurgia nas últimas 4 semanas: +1,5
  TVP ou TEP prévia documentada: +1,5
  Hemoptise: +1
  Neoplasia ativa (em tratamento ou nos últimos 6 meses): +1

PASSO 2: A REGRA "PERC" (Para casos com baixa suspeição inicial - "gestalt" negativa)
  Se o paciente tiver risco muito baixo e for NEGATIVO para TODOS os 8 critérios abaixo, o TEP está excluído (NÃO PEÇA Dímero-D):
  - Idade ≥ 50 anos; FC ≥ 100; SpO2 < 95%; Hemoptise; Estrogénios/Anticoncecionais; TVP/TEP prévia; Cirurgia/Trauma recente; Edema unilateral.

PASSO 3: CONDUTA BASEADA NO WELLS
  Wells ≤ 4 (Baixa/Moderada Probabilidade): SOLICITAR DÍMERO-D POC.
    Dímero-D Negativo: TEP excluído. Investigar outras causas (muscular, ansiedade, refluxo).
    Dímero-D Positivo: Necessita de AngioTC. Como a TC local não tem contraste, iniciar anticoagulação empírica (Enoxaparina 1mg/kg SC) e TRANSFERIR.

  Wells > 4 (Alta Probabilidade): O DÍMERO-D NÃO É ÚTIL.
    O resultado do Dímero-D (mesmo se falso-negativo) não anula o risco clínico.
    Conduta imediata: Anticoagulação empírica (Enoxaparina 1mg/kg SC 12/12h) e TRANSFERÊNCIA IMEDIATA para hospital com AngioTC.

PASSO 4: TEP MACIÇO (Instabilidade Hemodinâmica)
  Definição: TEP suspeito + PAS < 90 mmHg ou queda > 40 mmHg.
  É uma emergência de altíssima mortalidade. 
  Conduta: Suporte hemodinâmico com Noradrenalina (se choque). Se forte suspeita clínica ou sinais de disfunção de Ventrículo Direito no Ecocardiograma (se disponível POC), e sem contraindicações absolutas: ponderar TROMBÓLISE SISTÉMICA (Alteplase 100mg IV em 2 horas) antes ou durante a transferência (Vaga Zero).

SCORE DE WELLS PARA TVP (Trombose Venosa Profunda):
  Neoplasia ativa (+1); Paresia/imobilização de membro inferior (+1); Acamado > 3 dias ou cirurgia major recente (+1); Dor em trajeto venoso profundo (+1); Edema de toda a perna (+1); Edema de gémeos > 3cm que a perna oposta (+1); Edema depressível unilateral (+1); Veias superficiais colaterais visíveis (+1); Diagnóstico alternativo tão ou mais provável (-2).

  Score ≤ 1 (Baixa probabilidade) -> Dímero-D. 
    Se negativo = TVP excluída. Se positivo = Transferir para Eco-Doppler.
  Score ≥ 2 (Alta probabilidade) -> Anticoagulação empírica + Transferir para Eco-Doppler venoso.

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

A princípio, encaminhar paciente para serviço com assistência obstétrica.

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

Dengue Grupo B (Sem sinais de alarme, MAS com sangramento de pele, comorbidades ou gestante):
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
PROTOCOLO 08 — SÍNDROME GRIPAL (INFLUENZA E COVID-19)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

A Síndrome Gripal é caracterizada por quadro febril de início súbito, acompanhado de tosse ou dor de garganta, e pelo menos um dos seguintes sintomas: cefaleia, mialgia ou artralgia.

TESTES RÁPIDOS: Realizar teste para COVID-19 e Influenza (swab) se disponíveis, prioritariamente em pacientes de risco ou com SRAG. NÃO atrasar a decisão clínica ou o início de tratamento empírico em casos graves aguardando resultados.

====================================================================
1. MANEJO SINTOMÁTICO E SUPORTE UNIVERSAL (PARA TODOS OS CASOS)
====================================================================
- Antitérmicos e Analgésicos: Dipirona ou Paracetamol.
- Hidratação: Ingestão hídrica generosa oral.
- LAVAGEM NASAL COM SORO FISIOLÓGICO: 
  * Medida não farmacológica FUNDAMENTAL para alívio sintomático, redução do gotejamento pós-nasal (que piora a tosse) e prevenção de sinusite/otite bacterianas secundárias.
  * Prescrever ativamente: Orientar o paciente (ou cuidadores) a realizar lavagens de alto volume usando seringa de 20mL ou garrafinhas próprias (ex: NoseWash), com a cabeça levemente inclinada para a frente, várias vezes ao dia. Evitar pressão excessiva.
- Isolamento: Orientar afastamento laboral/escolar e medidas de etiqueta respiratória.

====================================================================
2. ANTIVIRAL PARA INFLUENZA: OSELTAMIVIR (Tamiflu)
====================================================================
Indicação: Iniciar de forma empírica e PRECOCE (ideal < 48h) para os seguintes grupos, com ou sem teste:

A. Pacientes com SRAG (Síndrome Respiratória Aguda Grave):
   - Dispneia, desconforto respiratório ou SpO2 < 93% em ar ambiente.
   
B. Pacientes com Fatores de Risco (mesmo se Síndrome Gripal leve):
   - Idosos (≥ 60 anos) e Crianças < 5 anos.
   - Gestantes e puérperas (até 2 semanas).
   - Imunossuprimidos e portadores de comorbidades crônicas (Pneumopatias, Cardiopatias, Nefropatias, Hepatopatias, Neurológicas).
   - Obesos mórbidos (IMC ≥ 40).

Dose: Adultos: 75 mg VO 12/12h por 5 dias. (Ajustar para crianças por peso e em insuficiência renal grave).

====================================================================
3. ANTIVIRAL PARA COVID-19: NIRMATRELVIR + RITONAVIR (NMV/r)
====================================================================
Indicação Estrita (Conforme Nota Técnica local de BH): 
O uso NÃO é para pacientes internados por COVID-19 grave. É uma medicação ambulatorial para EVITAR a progressão.

Critérios (TODOS devem ser preenchidos):
1. Diagnóstico CONFIRMADO de COVID-19 (Teste Rápido Antígeno ou RT-PCR positivo).
2. Sintomas LEVES a MODERADOS (paciente NÃO necessita de oxigênio suplementar).
3. Início dos sintomas há, no máximo, 5 DIAS.
4. Paciente pertence a um grupo de ALTO RISCO:
   - Imunossuprimidos com idade ≥ 18 anos.
   - Pessoas com idade ≥ 65 anos.

Atenção: A dispensação exige preenchimento de formulário específico da Secretaria de Saúde e verificação rigorosa de INTERAÇÕES MEDICAMENTOSAS (o Ritonavir é um potente inibidor do CYP3A4, contraindicando o uso com amiodarona, sinvastatina, colchicina, clopidogrel, entre muitos outros).

====================================================================
4. PACIENTES FORA DOS GRUPOS DE RISCO
====================================================================
- Oseltamivir e Nirmatrelvir/Ritonavir NÃO estão indicados de rotina para quadros leves em pacientes sem fatores de risco.
- Alta com medidas do item 1 (Sintomáticos + Lavagem Nasal) e orientações claras de retorno se sinais de alarme (falta de ar, piora da febre após o 3º dia).

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

A sepse é uma emergência médica tempo-dependente. A cada hora de atraso no antibiótico, a mortalidade aumenta cerca de 8%. 
Neste PA, o seu "laboratório de sepse" nas primeiras 3 horas é EXCLUSIVAMENTE a clínica, a gasometria (Lactato) e o EAS fita. NÃO AGUARDE o hemograma ou PCR externos para iniciar a intervenção.

PASSO 1: RECONHECIMENTO (O ALARME CLÍNICO)
  Suspeita de Infecção + Sinais de Disfunção Orgânica = SEPSE.
  - Sinais Rápidos (qSOFA/NEWS): FR ≥ 22 irpm, Glasgow < 15, PAS ≤ 100 mmHg.
  - Sinais de Hipoperfusão (Exame Físico): Tempo de enchimento capilar > 3 segundos, pele mosqueada/fria, oligúria, taquicardia inexplicada.
  - O MARCADOR PADRÃO-OURO NO PA: Lactato na gasometria.
    Lactato > 2 mmol/L = Disfunção (Sepse).
    Lactato > 4 mmol/L = Gravidade Extrema (Risco altíssimo de Choque Criptogênico).

PASSO 2: O "PACOTE DA PRIMEIRA HORA" (ADAPTADO À REALIDADE LOCAL)
  Aja simultaneamente nos primeiros 60 minutos da admissão:

  1. COLETA DE EXAMES ESSENCIAIS: Gasometria (lactato, acidose metabólica), EAS fita (se suspeita urinária).
  2. HEMOCULTURAS: Solicite a coleta de 2 pares ANTES do antibiótico. 
     REGRA DE OURO LOCAL: Se a coleta das culturas for demorar mais de 45 minutos (ex: acesso difícil, sobrecarga da enfermagem), NÃO ATRASAR A DOSE. Faça o antibiótico imediatamente, a vida tem precedência sobre a cultura.
  3. RESSUSCITAÇÃO VOLÊMICA: 30 mL/kg de Cristaloides nas primeiras 3 horas.
     - Dê preferência ao Ringer Lactato (o excesso de SF 0,9% causa acidose hiperclorêmica, que confunde a sua reavaliação gasométrica).
     - Se o paciente for nefropata ou cardiopata grave, faça alíquotas de 250-500 mL e reavalie os pulmões (estertores) a cada infusão. A sepse mata mais rápido que a congestão pulmonar aguda.
  4. ANTIBIOTICOTERAPIA EMPÍRICA (Amplo Espectro IV Imediato):
     - Foco Pulmonar (Pneumonia Grave): Ceftriaxona 2g IV + Azitromicina 500mg IV.
     - Foco Urinário: Ceftriaxona 2g IV (Ciprofloxacino 400mg IV apenas em caso de anafilaxia a betalactâmicos ou histórico de ESBL).
     - Foco Abdominal (Perfuração, Colecistite grave): Ceftriaxona 1g IV + Metronidazol 500mg IV.
     - Foco Cutâneo/Partes Moles (Erisipela bolhosa, fasceíte): Cefazolina 1g IV de 8/8h + Clindamicina 600mg IV de 6/6h. Se suspeita de MRSA: Vancomicina IV.
     - FOCO INDEFINIDO COM CHOQUE: Ceftriaxona 2g IV + Metronidazol 500mg IV (cobre Gram-negativos e anaeróbios).

PASSO 3: MANEJO DO CHOQUE SÉPTICO
  Definição: Necessidade de vasopressor para manter PAM ≥ 65 mmHg E Lactato > 2 mmol/L, APÓS a expansão volêmica adequada.
  - DROGA DE ESCOLHA: Norepinefrina 0,01 a 3 mcg/kg/min IV.
  - Diluição Padrão: 4 ampolas (16mg) em 250mL de SG5% = 64 mcg/mL. Iniciar a 5-10 mL/h em bomba de infusão.
  - MACETE DE PA: Não espere terminar os 30 mL/kg de Ringer para ligar a Nora se o paciente estiver profundamente chocado (PAS < 70, bradipsiquismo). Ligue a Nora de forma precoce EM ACESSO PERIFÉRICO CALIBROSO (antecubital) até que seja possível passar um Acesso Venoso Central. É seguro por algumas horas e salva o cérebro/rins.
  - Corticoide: Se o choque for REFRATÁRIO (exigindo doses crescentes de Nora apesar do volume), inicie Hidrocortisona 200 mg/dia (50 mg IV 6/6h).

PASSO 4: REAVALIAÇÃO E TRANSFERÊNCIA
  - Meta de 2 a 3 horas: Reavaliar o enchimento capilar (deve estar < 3 seg) e coletar nova Gasometria. O objetivo é o "Clearance de Lactato" (queda de pelo menos 10-20% em relação ao lactato inicial).
  - Controle de Foco: Se a suspeita for abscesso, obstrução biliar, isquemia mesentérica ou litíase ureteral obstrutiva infectada, o antibiótico não resolverá sozinho. O cirurgião precisa atuar nas primeiras 6 a 12h.
  - Ancoragem: Pacientes em sepse grave/choque devem ser prontamente inseridos no sistema de regulação (Vaga Zero para UTI), mantendo todo o suporte de hemodinâmica e antibióticos rodando sem interrupção no PA.
  
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROTOCOLO 13 — DOR ABDOMINAL AGUDA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PASSO 1: TRIAGEM DE SINAIS DE ALARME (RED FLAGS)
A prioridade no PA não é o diagnóstico exato imediato, mas identificar o "Abdome Cirúrgico" ou catástrofes vasculares:
  1. Instabilidade hemodinâmica (Hipotensão, taquicardia inexplicada, sudorese).
  2. Sinais de Peritonite (Abdome em tábua, dor à percussão, descompressão brusca dolorosa/Blumberg).
  3. Dor súbita, excruciante e de forte intensidade no início (sugere perfuração de víscera, ruptura de aneurisma, isquemia mesentérica).
  4. Dor desproporcional ao exame físico (Abdome inocente à palpação, mas paciente urrando de dor = Isquemia Mesentérica até prova em contrário, especialmente em idosos/fibriladores).
  >>> CONDUTA SE ALARME: 2 acessos calibrosos, expansão com Ringer/SF, analgesia agressiva, dieta zero, solicitar avaliação IMEDIATA do cirurgião presencial ou regulação via VAGA ZERO.

PASSO 2: A REGRA DA IDADE FÉRTIL
  - Toda paciente do sexo feminino entre 10 e 50 anos DEVE realizar o teste rápido de Beta-hCG, independentemente da data da última menstruação ou negação de atividade sexual. Faça isso ANTES de liberar analgesia pesada, raio-X ou TC (Ver Protocolo 06).

PASSO 3: ANALGESIA RACIONAL (O MITO CAIU)
  - MITO: "Não pode dar analgésico forte antes do cirurgião ver porque mascara o quadro."
  - VERDADE: A literatura mundial (ATLS, Cochrane) prova que analgesia (mesmo opioides) não mascara os sinais de irritação peritoneal e melhora a cooperação do paciente no exame físico.
  - Dor Cólica Leve/Moderada: Dipirona 1g IV + Escopolamina (Buscopan) 20mg IV.
  - Dor Inflamatória (Suspeita de cólica nefrética/biliar): Cetoprofeno 100mg IV (O AINE tem resposta superior ao opioide na cólica nefrética, desde que não haja contraindicação renal ou sangramento).
  - Dor Intensa: Tramadol 50-100mg IV (diluir em 100mL de SF e correr em 20 min para evitar náuseas) + Ondansetrona 8mg IV.
  - Dor Excruciante/Refratária: Morfina 2 a 4mg IV lenta.

PASSO 4: RACIOCÍNIO TOPOGRÁFICO E EXAMES DISPONÍVEIS

  A. DOR EM FOSSA ILÍACA DIREITA (Suspeita de Apendicite)
    - Clínica: Dor periumbilical que migra para FID, anorexia, febre baixa. Blumberg (+).
    - Exames no PA: TC de Abdome SEM Contraste tem menor sensibilidade para apendicite inicial, mas pode evidenciar apêndice espessado (> 6mm), fecalito ou borramento da gordura periapendicular. Hemograma (que demora horas) pode ajudar com leucocitose + desvio.
    - Conduta: Se muito típico, o diagnóstico é clínico. Deixe o paciente ancorado (dieta zero, hidratado e medicado) aguardando o cirurgião presencial.

  B. DOR EM HIPOCÔNDRIO DIREITO (Suspeita Biliar)
    - Clínica: Dor pós-prandial (gordura), contínua, sinal de Murphy (+), náuseas.
    - Exames no PA: A TC sem contraste é PÉSSIMA para ver cálculo biliar (muitos são radiotransparentes), mas pode ver gás na parede, distensão da vesícula ou líquido perivesicular. Hemograma e enzimas demoram horas.
    - Conduta: Analgesia + Antiespasmódico. Se dor prolongada (>6h), febre ou Murphy claro: suspeitar de Colecistite Aguda. Dieta zero, inicie Ceftriaxona 1g IV + Metronidazol 500mg IV e acione o cirurgião.

  C. DOR EM FOSSA ILÍACA ESQUERDA (Suspeita de Diverticulite)
    - Clínica: Paciente > 50 anos, dor contínua em FIE, mudança de hábito intestinal, febre.
    - Exames no PA: A TC de Abdome SEM Contraste é EXCELENTE e é o PADRÃO-OURO aqui. Avalie espessamento de parede do cólon sigmoide, divertículos e presença de pneumoperitônio ou abscesso.
    - Conduta: Sem abscesso ou perfuração na TC (Hinchey 1): Ciprofloxacino + Metronidazol (pode ser VO para casa se tolerar dieta e sem instabilidade). Com complicações na TC: Dieta zero, antibiótico IV e acionar cirurgião.

  D. DOR EPIGÁSTRICA COM IRRADIAÇÃO PARA O DORSO (Suspeita de Pancreatite / Úlcera)
    - ATENÇÃO: Faça um ECG para todo idoso ou diabético com queixa "epigástrica". Pode ser IAM de parede inferior.
    - Pancreatite: Requer 2 de 3 critérios (clínica típica; Amilase/Lipase > 3x limite; Imagem). A Amilase/Lipase demoram 3-8h e a TC sem contraste subestima a gravidade nas primeiras 48h.
    - Conduta de PA: Se alta suspeita clínica, não espere a Lipase. Inicie a pedra angular do tratamento: RESSUSCITAÇÃO VOLÊMICA AGRESSIVA (Ringer Lactato 250 a 500 mL/h nas primeiras 12-24h se o coração aguentar) + Analgesia forte (Opioide). Ancore o paciente até a chegada dos exames.

  E. DOR LOMBAR/FLANCO IRRADIANDO PARA GENITÁLIA (Cólica Nefrética)
    - Clínica: Inquietação (paciente não acha posição), dor lancinante, hematúria na fita reagente (EAS).
    - Exames no PA: TC SEM Contraste é o PADRÃO-OURO absoluto para cálculo renal.
    - Conduta: AINE (Cetoprofeno IV) é o melhor analgésico. Associar resgate com opioide. Se não houver sinais de ITU associada (febre, leucocitúria no EAS fita), tratar sintomas e pode ter alta com encaminhamento à urologia ambulatorial. Se cálculo obstrutivo + febre (Pielonefrite Obstrutiva): Urgência Urológica -> Ceftriaxona 2g IV + Transferência.

PASSO 5: RX DE ROTINA DE ABDOME
  - SÓ solicite se: 1) Suspeita de Obstrução Intestinal (busca de níveis hidroaéreos e distensão de alças); 2) Suspeita de Perfuração (RX de Tórax em ortostatismo ou Abdome incluindo cúpula frênica buscando pneumoperitônio); 3) Pesquisa de corpo estranho radiopaco. Fora destas 3 indicações, o RX de abdome não tem validade diagnóstica significativa.

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
