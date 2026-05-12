"""
protocolos.py
Base de conhecimento clínico-institucional do PA.
Hospital Geral São José — Contagem/MG
"""

PROTOCOLOS_TEXTO = """
╔══════════════════════════════════════════════════════════════════════╗
║  CONTEXTO REAL DA UNIDADE — HOSPITAL GERAL SÃO JOSÉ                  ║
║  Pronto Atendimento — Clínica Médica — Contagem/MG                   ║
╚══════════════════════════════════════════════════════════════════════╝

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
  Morfina 2-4mg IV se dor ≥ 8/10 e PAS > 90mmHg.
  Oxigênio máscara se SpO2 < 94%.
  Nitrato 0,4mg SL se PAS > 90mmHg, repetir 3x a cada 5min.
  AAS 300mg VO mastigado.
  Clopidogrel 300mg VO.
  HNF bolus 60 UI/kg IV (máx 4000 UI) + infusão 12 UI/kg/h.
  ACIONAR VAGA ZERO PARA HEMODINÂMICA DE IMEDIATO.

IAMSST / NSTEMI (troponina elevada ou ECG com alterações isquêmicas):
  AAS 200mg + Clopidogrel 300mg VO.
  Enoxaparina 1mg/kg SC.
  Troponina seriada 0h e 3h.
  Transferência urgente se troponina positiva ou ECG alterado.
  Se troponina negativa em 2 coletas e ECG normal: alta com
  encaminhamento urgente para cardiologia.

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
    TC de tórax SEM contraste tem baixa sensibilidade para TEP direta.
    Se forte suspeita clínica com dímero positivo: anticoagulação empírica
    + transferência para TC com contraste ou cintilografia.

  Wells > 4 (alta probabilidade): Dímero-D não é útil aqui.
    Anticoagulação empírica imediata: Enoxaparina 1mg/kg SC.
    Transferência para confirmação por imagem adequada.
    Se instabilidade hemodinâmica (TEP maciça): trombólise sistêmica
    conforme protocolo antes de transferir.

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

Edema Agudo de Pulmão:
  Posição ortostática ou semissentado. Oxigênio ≥ 10L/min máscara.
  Furosemida 40-80mg IV lento. Dobrar a dose se já usa furosemida oral.
  Nitrato SL 0,4mg se PAS > 100mmHg, repetir 3x a cada 5min.
  Morfina 2-4mg IV se dor associada, sem hipotensão e sem DPOC.
  ECG e Troponina para afastar SCA como causa.
  Gasometria para avaliar gravidade e resposta.
  Transferência para UTI se: IOT iminente, choque cardiogênico, refratariedade.

Exacerbação de DPOC ou asma grave:
  Oxigênio controlado: 1-2L/min cateter nasal, meta SpO2 88-92% no DPOC.
  Salbutamol 5mg + Ipratrópio 0,5mg nebulização, repetir 3x a cada 20min.
  Dexametasona 10mg IV ou Metilprednisolona 125mg IV.
  Se componente infeccioso bacteriano e o paciente for internar ou transferir:
    Ceftriaxona 1-2g IV (apenas se internação/transferência confirmada).
  Aminofilina 5mg/kg IV em 30min se refratário às nebulizações.
  Gasometria se SpO2 < 92% após primeira nebulização.
  Transferência se pCO2 > 55, pH < 7,30 ou nível de consciência alterado.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROTOCOLO 04 — HIPERTENSÃO ARTERIAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Urgência hipertensiva (PA elevada sem lesão de órgão-alvo):
  Captopril 25mg SL ou VO, repetir em 30min se necessário.
  Clonidina 0,1mg VO a cada 1h, máximo 0,6mg. Não usar em bradicardia ou BAV.
  Meta: redução gradual em 24-48h. Não forçar queda rápida.
  Observação 4-6h. Alta com ajuste da medicação habitual.

Emergência hipertensiva (PA elevada com lesão de órgão-alvo confirmada):
  Nitroprussiato de Sódio: 50mg em 250mL SG5% = 200 mcg/mL.
    Proteger da luz com papel alumínio no frasco e equipo.
    Iniciar 0,5 mcg/kg/min em bomba de infusão, titular até 10 mcg/kg/min.
    Monitorar PA a cada 5min. Máximo 72h de uso.
  Hidralazina IV se sem bomba disponível: 10-20mg IV lento a cada 20-30min.
  Meta: redução máxima de 25% da PAM na primeira hora.
  Transferência para UTI se encefalopatia ou instabilidade hemodinâmica.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROTOCOLO 05 — AVC AGUDO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TC de crânio sem contraste é a prioridade absoluta para afastar hemorragia.
O plantonista interpreta a TC. Para hemorragia o diagnóstico é visual e claro.
Para isquemia nas primeiras horas a TC pode ser normal — clínica + tempo decidem.

  ABC, oxigênio se SpO2 < 94%. Decúbito 30 graus. HGT imediato.
  Hipoglicemia corrigida com SG50% 50mL IV antes de qualquer outra conduta.
  ECG para identificar FA como causa.
  PA: não reduzir se < 220/120 sem trombólise.
    Se candidato a rt-PA: meta < 185/110 antes de iniciar.
  Temperatura: paracetamol se febre (temperatura prejudica neurônios isquêmicos).
  Troponina: se suspeita de embolia cardiogênica.
  Janela para trombólise: até 4,5h do início dos sintomas.
    Transferência urgente para centro de AVC com a janela mantida aberta.
  AVC hemorrágico confirmado na TC: meta PA < 140/90 com Hidralazina IV
    ou Nitroprussiato. Transferência urgente para neurocirurgia.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROTOCOLO 06 — GRAVIDEZ, BETA-hCG E EMERGÊNCIAS OBSTÉTRICAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Beta-hCG rápido é obrigatório em toda mulher com potencial gestacional
(dos 10 aos 50 anos) que apresente qualquer dos seguintes:
  dor abdominal ou pélvica, sangramento vaginal, síncope ou hipotensão
  sem causa clara, náuseas e vômitos sem diagnóstico definido.

Beta-hCG positivo com dor abdominal ou pélvica: gravidez ectópica até
prova em contrário. Avalie instabilidade hemodinâmica imediatamente.
  Se instável: acionar cirurgião, dois acessos venosos calibrosos,
    SF 0,9% em bolus, TC de abdome e pelve sem contraste (pode evidenciar
    hematoma pélvico ou massa anexial), transferência urgente para hospital
    com ginecologia e cirurgia de emergência.
  Se estável: TC abdome/pelve sem contraste, manter observação,
    transferência assim que confirmada suspeita de ectópica.

Beta-hCG positivo sem dor, paciente estável:
  Considerar gravidez inicial, ameaça de aborto, mola hidatiforme.
  Orientações sobre sinais de alarme. Retorno imediato com ginecologia.
  Alta segura se sem sangramento ativo e sinais vitais normais.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROTOCOLO 07 — DENGUE E ARBOVIROSES (COM NS1 DISPONÍVEL)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NS1 indicado: febre com até 5 dias de evolução e quadro sugestivo
(mialgia intensa, cefaleia retroorbitária, exantema, artralgia, prostração).

NS1 positivo = Dengue confirmada. Classificar:

Dengue sem sinais de alarme: hidratação oral supervisionada, paracetamol
para febre e dor, alta com orientações detalhadas e retorno à UBS.
Não usar AAS nem AINE — risco de sangramento.

Dengue com sinais de alarme (qualquer dos seguintes: dor abdominal intensa
e contínua, vômitos persistentes, acúmulo de líquidos em cavidades, sangramento
de mucosas, hipotensão postural, letargia ou agitação, hepatomegalia, hematócrito
elevado com queda de plaquetas): ancorar em observação.
  Enquanto aguarda hemograma externo: SF 0,9% 10-20mL/kg conforme tolerância.
  Paracetamol. Hidratação venosa se vômitos. Reavaliação clínica a cada 2h.
  Hemograma externo é ESSENCIAL aqui (plaquetopenia e hemoconcentração).

Dengue grave (choque, sangramento grave, disfunção orgânica): suporte
hemodinâmico, transferência imediata.

NS1 negativo nos primeiros 5 dias não exclui dengue. Se quadro sugestivo
e NS1 negativo, tratar como dengue provável, coletar sorologia (IgM/IgG)
para confirmação posterior e orientar retorno se piora.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROTOCOLO 08 — INFLUENZA E SÍNDROME GRIPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Teste rápido para Influenza A e B disponível. Indicar em:
  quadro gripal típico em época de circulação do vírus, ou qualquer paciente
  de grupo de risco com febre e síndrome respiratória aguda.

Teste positivo em paciente de grupo de risco (idosos, gestantes,
imunodeprimidos, cardiopatas, pneumopatas, obesos mórbidos):
  Oseltamivir 75mg VO 12/12h por 5 dias. Iniciar em até 48h do início.
  Paracetamol para febre e mialgia.
  Se SpO2 < 93% ou FR > 24: radiografia de tórax para afastar pneumonia.
  Avaliar internação ou transferência se saturaçao cair, dispneia ou
  comprometimento radiológico bilateral.

Teste positivo em paciente sem grupo de risco e sem critérios de gravidade:
  Tratamento sintomático. Oseltamivir pode ser considerado mas não é obrigatório.
  Alta com orientações. Retorno se piora.

Teste negativo não exclui influenza nos primeiros dias.
Se quadro muito sugestivo e paciente de alto risco: tratar empiricamente.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROTOCOLO 09 — ANAFILAXIA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Adrenalina é sempre a primeira medicação. Sem exceção.
Adrenalina 1:1000, 0,3-0,5mg IM na coxa anterolateral. Repetir a cada 5-10min.
Nunca atrasar adrenalina para usar anti-histamínico primeiro.

Hipotensão: decúbito dorsal com MMII elevados.
Broncoespasmo predominante: semissentado 45 graus.
Oxigênio 10-15L/min máscara. SF 0,9% 500-1000mL IV rápido se hipotensão.
Salbutamol nebulização se broncoespasmo persistente após adrenalina.
Difenidramina 25-50mg IV lento + Ranitidina 50mg IV lento (complementar).
Metilprednisolona 125mg IV ou Dexametasona 10mg IV.

Observação mínima de 6-8h pelo risco de reação bifásica.
Alta somente com sintomas totalmente resolvidos.
Prescrever adrenalina IM para casa e orientar uso.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROTOCOLO 10 — CRISE CONVULSIVA E STATUS EPILEPTICUS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Fase 1 (0-5min): decúbito lateral, via aérea, oxigênio, acesso venoso.
  HGT imediato. Se < 60 mg/dL: SG50% 50mL IV antes de qualquer outra conduta.

Fase 2 (5-20min): benzodiazepínico.
  Diazepam 10-20mg IV na velocidade de 2mg/min. Risco de apneia — ter ambu.
  Sem acesso venoso: Diazepam 10mg retal ou Midazolam 10mg IM.

Fase 3 (20-40min): antiepiléptico de segunda linha.
  Fenitoína 18-20mg/kg IV, velocidade máxima 50mg/min (preferir 25mg/min).
  Diluir obrigatoriamente em SF 0,9%. Precipita em SG. Monitorar cardíaco.

Fase 4 (status refratário acima de 40min):
  Fenobarbital 20mg/kg IV. Preparar para IOT. Transferência urgente para UTI.

Investigar sempre: HGT, EAS (se suspeita de foco infeccioso), TC de crânio.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROTOCOLO 11 — CETOACIDOSE DIABÉTICA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Diagnóstico pela gasometria: HGT > 250 + pH < 7,30 + HCO3 < 18.

Hidratação: SF 0,9% 1000mL na primeira hora, 500mL/h nas 2-4h seguintes.
  Trocar para SG5% quando HGT < 250mg/dL.

Insulina regular: não iniciar se K+ < 3,5 na gasometria.
  Bolus 0,1 UI/kg IV, depois infusão 0,1 UI/kg/h.
  Diluição da infusão: 50 UI de Insulina Regular em 50mL de SF = 1 UI/mL.
  Meta: queda de 50-100mg/dL/hora no HGT.

Reposição de potássio pela gasometria:
  K+ < 3,0: 40mEq/h, adiar insulina.
  K+ 3,0-3,5: 40mEq/h, iniciar insulina junto.
  K+ 3,5-5,0: 20-40mEq na solução de hidratação.
  K+ > 5,5: não repor, reavaliar em 2h.
  KCl 19,1% — ampola de 10mL = 25mEq.

Bicarbonato: apenas se pH < 6,9. 100mEq em 400mL AD em 2h.
Monitorar gasometria a cada 2-3h e HGT horário.
Transferência se pH < 7,0, K+ instável, Glasgow < 14 ou sem melhora em 4h.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROTOCOLO 12 — SEPSE E CHOQUE SÉPTICO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

qSOFA para triagem: FR ≥ 22irpm, alteração do nível de consciência, PAS ≤ 100mmHg.
Confirmar disfunção orgânica pelo Lactato na gasometria (Lactato ≥ 2 mmol/L).

Hemograma é exame externo e demorará horas. Não espere por ele para iniciar
o tratamento. A decisão de tratar sepse é clínica + gasometria, não laboratorial.

Bundle na primeira hora:
  Gasometria para lactato e estado metabólico basal.
  Acesso venoso calibroso.
  Antibiótico empírico em até 1h (coletar antes, mas não atrasar por coleta):
    Foco pulmonar: Ceftriaxona 2g IV + Azitromicina 500mg IV.
      (Ceftriaxona aqui é permitida pois é caso de internação/transferência)
    Foco urinário: Ceftriaxona 2g IV (Ciprofloxacino 400mg IV se risco ESBL).
    Foco abdominal: Ceftriaxona 1g IV + Metronidazol 500mg IV.
    Sem foco definido: Ceftriaxona 2g IV + Metronidazol 500mg IV.
  Ressuscitação volêmica: 30mL/kg SF0,9% ou Ringer Lactato em 3h.
  EAS para avaliar foco urinário.
  Hemograma, PCR e outros externos são solicitados para acompanhamento,
    mas o tratamento já deve estar em curso quando chegarem.

Choque séptico (PAS < 90 após 30mL/kg + Lactato > 4):
  Norepinefrina 0,01-3 mcg/kg/min IV em bomba. Meta PAM ≥ 65mmHg.
  Diluição: 4mg em 250mL SG5% = 16 mcg/mL.
  Transferência para UTI urgente.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROTOCOLO 13 — DOR ABDOMINAL AGUDA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Beta-hCG obrigatório em toda mulher com potencial gestacional antes de
qualquer outra conduta — ver Protocolo 06.

Acionar cirurgião se: rigidez abdominal, peritonismo, Blumberg positivo,
dor intensa em fossa ilíaca direita, massas pulsáteis, trauma.

Analgesia: nunca negar. Analgesia não mascara abdome cirúrgico de forma clinicamente
relevante nas doses terapêuticas habituais.
  Dipirona 1g IV em 100mL SF em 15min.
  Cetoprofeno 100mg IV se sem contraindicações renais ou hemostáticas.
  Buscopan 20mg IV + Dipirona para cólicas.
  Tramadol 100mg IV em 100mL SF em 30min para dor moderada a intensa.
  Morfina 2-4mg IV para dor intensa quando diagnóstico cirúrgico foi avaliado.

Sobre os exames disponíveis para dor abdominal:
  EAS: identifica ITU, nefrolitíase com hematúria, glicosúria.
  TC abdome sem contraste: excelente para nefrolitíase e pneumoperitônio.
    Para apendicite, a sensibilidade do TC sem contraste é inferior ao com contraste.
    Para pancreatite aguda: TC sem contraste pode mostrar edema pancreático e
    coleções, mas subestima necrose. Amilase e Lipase são externos e demoram.
  Hemograma e PCR: externos, demoram horas. Ancore o paciente, trate o sintoma,
    aguarde o resultado para decidir internação ou alta.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROTOCOLO 14 — ARRITMIAS CARDÍACAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Com instabilidade (PAS < 90, síncope, EAP ou dor torácica associada):
  Cardioversão elétrica sincronizada imediata.
  FA ou Flutter: 100-200J bifásico. TSV: 50-100J. TV com pulso: 100-200J.
  FV ou TV sem pulso: desfibrilação 200J + ACLS.

Taquiarritmia estável:
  TSV: manobra de Valsalva modificada primeiro. Adenosina 6mg IV bolus rápido
    com flush imediato de 20mL SF. Segunda dose 12mg. Terceira dose 12mg.
    Se falhar: Metoprolol 2,5-5mg IV lento (1mg/min).
  FA com RVR acima de 110bpm: Metoprolol 5mg IV (0,5mg/min, máx 3 doses de 5mg).
    Se FA recente < 48h ou FE reduzida: Amiodarona 300mg IV em 20-30min.
  TV monomórfica estável: Amiodarona 150mg IV em 10min, depois 1mg/min por 6h.

Bradicardia sintomática: Atropina 0,5mg IV, repetir a cada 3-5min até 3mg.
  Se refratária: Dopamina 2-10 mcg/kg/min. Transferência para marcapasso.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROTOCOLO 15 — IST E INFECÇÕES GENITURINÁRIAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Infecção do Trato Urinário baixa (cistite):
  EAS fita: nitritos positivos e esterase leucocitária positiva em mulher
  sintomática já é suficiente para diagnóstico e início do tratamento.
  Sem microscopia disponível aqui. O diagnóstico é clínico + fita reativa.
  Nitrofurantoína 100mg VO 6/6h por 5 dias ou SMX/TMP 800/160mg VO 12/12h por 3-7 dias.
  Ciprofloxacino 500mg VO 12/12h por 3-7 dias (preferir se pielonefrite).

Pielonefrite leve a moderada (sem sepse):
  EAS com leucocitúria, nitritos, proteinúria discreta.
  Ciprofloxacino 500mg VO 12/12h por 10-14 dias se tolerando VO.
  Analgesia: Dipirona ou Paracetamol. AINE com cautela.
  Se vômitos: manter em observação, hidratação IV, reavaliar VO em 2-4h.
  Hemograma e PCR externos úteis para confirmar gravidade, mas não bloqueiam
  o início do tratamento.

Gonorreia:
  Ceftriaxona 1g IV ou IM dose única.
  Azitromicina 1g VO dose única concomitante.
  Esta é uma das indicações aceitas de Ceftriaxona sem internação neste PA.

ITU de repetição, ITU em gestante ou suspeita de germe resistente:
  Ancorar em observação. Aguardar urinocultura (externa) para ajuste.
  Iniciar tratamento empírico enquanto aguarda.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROTOCOLO PEDIÁTRICO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Pediatra disponível — acionar para todos os casos pediátricos triados.
Se pediatra ausente naquele plantão, condutas básicas:

Febre: Paracetamol 10-15mg/kg/dose VO a cada 6h, máximo 75mg/kg/dia.
  Ibuprofeno 5-10mg/kg/dose VO a cada 8h (acima de 6 meses), máximo 40mg/kg/dia.
  Dipirona 10-15mg/kg/dose VO ou IV.
  Nunca usar AAS em menores de 12 anos.

Desidratação leve a moderada: TRO com SRO, 50-100mL/kg em 4h.
Desidratação grave com sinais de choque: Ringer Lactato 20mL/kg IV em bolus, repetir.

Broncoespasmo: Salbutamol 0,15mg/kg nebulização (mínimo 1,25mg, máximo 5mg)
  a cada 20min por 3 vezes. Ipratrópio 0,25-0,5mg nas primeiras 3 doses.
  Prednisolona 1-2mg/kg VO.

Holliday-Segar: < 10kg: 100mL/kg/dia. 10-20kg: 1000mL + 50mL/kg por kg acima de 10.
  > 20kg: 1500mL + 20mL/kg por kg acima de 20.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FARMÁCIA DO PA — MEDICAMENTOS DISPONÍVEIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Analgésicos e antitérmicos: Dipirona, Paracetamol, Ibuprofeno, Cetoprofeno,
Tenoxicam, Tramadol, Morfina, AAS.

Antibióticos IV: Ceftriaxona, Ampicilina+Sulbactam, Metronidazol,
Ciprofloxacino, Vancomicina, Clindamicina, Azitromicina.

Antibióticos VO: Amoxicilina, Amox+Clavulanato, Azitromicina, Ciprofloxacino,
SMX/TMP, Nitrofurantoína, Doxiciclina, Aciclovir.

Cardiovasculares IV: Adrenalina, Norepinefrina, Dopamina, Amiodarona,
Adenosina, Atropina, Digoxina, Enalaprilato, Nitroprussiato, Furosemida, Hidralazina.

Cardiovasculares VO: AAS, Captopril, Enalapril, Atenolol, Metoprolol,
Furosemida, Espironolactona, Nifedipino retard, Clonidina, Nitrato SL e spray.

Anticoagulantes: Enoxaparina (seringas 20 a 100mg), HNF.

Neurológico: Diazepam, Midazolam, Fenitoína, Fenobarbital, Haloperidol, Clonazepam.

Endocrinologia: Insulina Regular, Insulina NPH, SG50% ampola, Glucagon kit.

Alérgico e inflamatório: Difenidramina, Prometazina, Dexametasona,
Metilprednisolona, Adrenalina 1:1000.

Gastro e antiemético: Ondansetrona, Metoclopramida, Pantoprazol IV,
Omeprazol VO, Ranitidina, Buscopan, Domperidona.

Broncodilatadores: Salbutamol NBZ, Ipratrópio NBZ, Aminofilina IV, Fenoterol NBZ.

Antiviral: Oseltamivir 75mg.

Soluções: SF0,9% todos os volumes, SG5%, SG10%, SG50%, Ringer Lactato, KCl, NaHCO3, AD.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CRITÉRIOS DE TRANSFERÊNCIA IMEDIATA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Transferir sem hesitar quando houver: IAMCSST, choque cardiogênico,
choque séptico refratário, AVC em janela terapêutica ou hemorrágico,
TEP de alto risco, status epilepticus refratário, CAD grave com pH < 7,0,
necessidade de IOT e ventilação mecânica, suspeita de gravidez ectópica rota,
necessidade de cirurgia de emergência que ultrapasse a capacidade local,
qualquer condição que exija UTI ou monitorização intensiva prolongada.
"""
