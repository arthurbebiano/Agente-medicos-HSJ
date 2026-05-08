"""
protocolos.py
Protocolos institucionais, medicações disponíveis e recursos do PA.
Hospital Geral São José — Contagem/MG
"""

PROTOCOLOS_TEXTO = """
╔══════════════════════════════════════════════════════════════════════╗
║  PROTOCOLOS INSTITUCIONAIS — HOSPITAL GERAL SÃO JOSÉ — CONTAGEM/MG  ║
║  Pronto Atendimento de Clínica Médica                                ║
╚══════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[A] MAPA COMPLETO DE RECURSOS — O QUE EXISTE E O QUE NÃO EXISTE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

EXAMES LABORATORIAIS (TOTAL: 3 — NENHUM OUTRO DISPONÍVEL):
  1. Troponina I ou T (quantitativa)           → Resultado ~60-90min
  2. EAS / Urina Tipo I                        → Resultado ~30min
  3. Gasometria Arterial                       → Resultado ~15min
     Parâmetros: pH, pCO2, pO2, HCO3, BE, SatO2, Lactato,
                 Glicose, K+, Na+, Cl-, Hb, Hematócrito

GLICEMIA CAPILAR: HGT (imediato — disponível à beira-leito)

IMAGEM E MONITORIZAÇÃO (MÉDICO INTERPRETA SOZINHO):
  4. ECG 12 derivações
  5. Radiografia simples (Tórax PA/Perfil, Abdome)
  6. TC sem contraste (Crânio, Tórax, Abdome/Pelve)

⚠️ NÃO EXISTEM NESTE SERVIÇO — NUNCA SUGERIR:
  ✗ Hemograma completo (leucócitos, plaquetas, Hb completa)
  ✗ Função renal isolada (Creatinina, Ureia, Clearance)
  ✗ Coagulograma (TP, INR, TTPA, D-dímero)
  ✗ Bioquímica hepática (TGO, TGP, GGT, FA, Bilirrubinas)
  ✗ Eletrólitos isolados (APENAS via Gasometria)
  ✗ Proteína C-Reativa / VHS / Ferritina / Procalcitonina
  ✗ CK / CK-MB isolados / BNP / NT-proBNP
  ✗ Hormônios (TSH, T4L, Cortisol, βHCG quantitativo)
  ✗ Culturas (Hemocultura, Urocultura específica)
  ✗ TC com contraste / Angiotomografia
  ✗ Ultrassonografia / Ecocardiograma / Doppler
  ✗ Ressonância Magnética

CAPACIDADE OPERACIONAL:
  Equipe:     1 Clínico Geral | 1 Pediatra | 1 Cirurgião Geral (24h)
  Internação: CAPACIDADE ZERO
  Missão:     ESTABILIZAR → ALTA SEGURA ou TRANSFERÊNCIA

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[B] PROTOCOLO 01 — DOR TORÁCICA / SÍNDROME CORONARIANA AGUDA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TRIAGEM: ECG em ≤ 10min da chegada — OBRIGATÓRIO EM QUALQUER DOR TORÁCICA

IAMCSST (Supradesnivelamento ST ≥ 1mm em ≥ 2 derivações contíguas, ou BRE novo):
  MONA IMEDIATO:
  • Morfina 2-4mg IV lento (se dor ≥ 8/10 e PAS > 90mmHg)
  • Oxigênio 2-4L/min máscara (se SpO2 < 94%)
  • Nitrato 0,4mg SL (se PAS > 90mmHg) — repetir 3x a cada 5min
  • AAS 300mg VO mastigado
  ANTIAGREGAÇÃO: Clopidogrel 300mg VO (dose de ataque)
  ANTICOAGULAÇÃO: HNF Bolus 60 UI/kg IV (máx 4000 UI) + Infusão 12 UI/kg/h
  → ACIONAR VAGA ZERO PARA HEMODINÂMICA IMEDIATAMENTE

IAMSST / NSTEMI:
  • AAS 200mg + Clopidogrel 300mg VO
  • Enoxaparina 1mg/kg SC (ou HNF IV se alteração renal na gasometria)
  • Troponina 0h e 3h seriada
  • Troponina+ ou ECG alterado: TRANSFERÊNCIA URGENTE (2-4h)
  • Troponina negativa + ECG normal: Alta com encaminhamento urgente cardiologia

DOR TORÁCICA BAIXO RISCO (HEART Score ≤ 3, sem fatores de alarme):
  • Observação 3-6h + Troponina seriada
  • AAS 100mg VO
  • Alta com orientações + retorno em ambulatório

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[C] PROTOCOLO 02 — DISPNEIA AGUDA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

EDEMA AGUDO DE PULMÃO (EAP):
  1. Posição ortostática (45-90°), O2 ≥ 10L/min máscara
  2. Furosemida 40-80mg IV lento (2-5min) — se usa furosemida oral: dobrar dose
  3. Nitrato SL 0,4mg (se PAS > 100mmHg) — repetir 3x a 5min
  4. Morfina 2-4mg IV (se dor, sem hipotensão, sem DPOC)
  5. Nitroprussiato IV se refratário (ver Protocolo HAS)
  6. ECG + Troponina (excluir SCA como causa)
  7. RX Tórax, Gasometria se SpO2 < 90%
  → TRANSFERÊNCIA UTI: IOT iminente, choque cardiogênico, refratariedade

EXACERBAÇÃO DPOC / ASMA GRAVE:
  1. O2 CONTROLADO 1-2L/min cateter nasal (meta SpO2 88-92% no DPOC)
  2. Salbutamol 5mg + Ipratrópio 0,5mg NBZ — repetir 3x a cada 20min
  3. Dexametasona 10mg IV ou Metilprednisolona 125mg IV
  4. Se bacteriana: Ceftriaxona 1-2g IV
  5. Aminofilina 5mg/kg IV em 30min → 0,5mg/kg/h manutenção
  6. Gasometria se SpO2 < 92% após 1ª nebulização
  → TRANSFERÊNCIA: pCO2 > 55mmHg, pH < 7,30, rebaixamento consciência

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[D] PROTOCOLO 03 — HIPERTENSÃO ARTERIAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

URGÊNCIA HIPERTENSIVA (PA elevada SEM lesão de órgão-alvo):
  • Captopril 25mg SL ou VO → repetir em 30min se necessário
  • Clonidina 0,1mg VO a cada 1h (máx 0,6mg) — NÃO usar em bradi/BAV
  • Meta: Redução ≤ 25% nas primeiras 24-48h
  • Observação 4-6h → Alta com ajuste da medicação habitual

EMERGÊNCIA HIPERTENSIVA (PA elevada COM lesão de órgão-alvo):
  Nitroprussiato de Sódio (PRIMEIRA ESCOLHA):
  • Diluição: 50mg em 250mL SG5% = 200 mcg/mL
  • ⚠️ PROTEGER DA LUZ (papel alumínio no frasco e equipo)
  • Dose: iniciar 0,5 mcg/kg/min → titular até 10 mcg/kg/min
  • Infusão: BOMBA DE INFUSÃO obrigatória
  • Monitorar PA a cada 5min
  • Máximo 72h de uso (risco de toxicidade por tiocianato)

  Hidralazina IV (se sem bomba):
  • 10-20mg IV lento a cada 20-30min até controle
  • Início ação 10-20min; Duração 2-4h

  Meta Geral: Reduzir PAM em no máximo 25% na 1ª hora
  → TRANSFERÊNCIA UTI: encefalopatia, instabilidade hemodinâmica

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[E] PROTOCOLO 04 — AVC AGUDO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

AVALIAÇÃO SAMU DO AVC: Sorriso | Abraço | Mensagem (assimetria)
PRIORIDADE: TC CRÂNIO SEM CONTRASTE — URGÊNCIA MÁXIMA

  1. ABC — via aérea, O2 (se SpO2 < 94%)
  2. Decúbito 30°, acesso venoso, HGT
  3. Tratar hipoglicemia (< 60 mg/dL): SG50% 50mL IV
  4. ECG (fibrilação atrial como causa?)
  5. TC CRÂNIO SEM CONTRASTE (disponível) → AFASTAR HEMORRAGIA
  6. PA: NÃO reduzir se < 220/120 (exceto se candidato a rt-PA: meta < 185/110)
  7. Temperatura: Paracetamol se febre (febre piora prognóstico neurológico)
  8. Troponina se suspeita de causa cardioembólica

  Janela para trombólise (rt-PA): ≤ 4,5h do início
  → TRANSFERÊNCIA URGENTE para Centro de AVC (manter janela aberta)

  AVC Hemorrágico (confirmado na TC):
  • Meta PA < 140/90 mmHg (Hidralazina IV ou Nitroprussiato)
  • → TRANSFERÊNCIA URGENTE para Neurocirurgia

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[F] PROTOCOLO 05 — ANAFILAXIA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚡ ADRENALINA É SEMPRE A PRIMEIRA MEDICAÇÃO — SEM EXCEÇÕES

  Adrenalina 1:1000 → 0,3-0,5mg IM (coxa anterolateral)
  Pode repetir a cada 5-10min (máx 3 doses)
  ⚠️ NUNCA atrasar adrenalina para usar anti-histamínico!

  POSIÇÃO:
  • Hipotensão: Decúbito dorsal + MMII elevados
  • Broncoespasmo: Semi-sentado 45°

  SUPORTE:
  • O2 10-15L/min máscara
  • SF 0,9% 500-1000mL IV rápido (se hipotensão)
  • Salbutamol NBZ se broncoespasmo persistente

  MEDICAÇÕES COMPLEMENTARES (após adrenalina):
  • Difenidramina 25-50mg IV lento (Anti-H1)
  • Ranitidina 50mg IV lento (Anti-H2 — potencializa H1)
  • Metilprednisolona 125mg IV (ou Dexametasona 10mg IV)

  OBSERVAÇÃO OBRIGATÓRIA: mínimo 6-8h (risco de reação bifásica em 1-8h)
  Alta: adrenalina IM para casa + orientação de uso + pulseira de alergia

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[G] PROTOCOLO 06 — CRISE CONVULSIVA / STATUS EPILEPTICUS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FASE 1 (0-5min): Decúbito lateral | O2 máscara | Acesso venoso
  HGT: Se < 60 → SG50% 50mL IV IMEDIATO

FASE 2 (5-20min): BENZODIAZEPÍNICO
  • Diazepam 10-20mg IV (2mg/min) — ⚠️ RISCO DE APNEIA — ter ambu na mão
  • Sem acesso: Diazepam 10mg retal | Midazolam 10mg IM

FASE 3 (20-40min): ANTIEPILÉPTICO
  • Fenitoína 18-20mg/kg IV — máx 50mg/min (preferir 25mg/min)
    - Diluir EM SF 0,9% (precipita em SG!)
    - MONITORAÇÃO CARDÍACA CONTÍNUA (arritmia)

FASE 4 (>40min — Status Refratário):
  • Fenobarbital 20mg/kg IV (50-100mg/min)
  • → IOT + TRANSFERÊNCIA UTI URGENTE

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[H] PROTOCOLO 07 — CETOACIDOSE DIABÉTICA (CAD)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DIAGNÓSTICO PELA GASOMETRIA: HGT > 250 + pH < 7,30 + HCO3 < 18

HIDRATAÇÃO:
  • 1ª hora: SF 0,9% 1000mL em 60min
  • 2ª-4ª hora: SF 0,9% 500mL/h
  • Quando HGT < 250: trocar para SG5% 250mL/h

INSULINA REGULAR:
  ⚠️ NÃO INICIAR se K+ < 3,5 na gasometria
  • Bolus: 0,1 UI/kg IV
  • Infusão: 0,1 UI/kg/h (Diluição: 50 UI Ins. Regular em 50mL SF = 1UI/mL)
  • Meta: Redução de 50-100mg/dL/hora no HGT

REPOSIÇÃO DE POTÁSSIO (pela gasometria):
  • K+ < 3,0:   40mEq KCl/h + ADIAR insulina
  • K+ 3,0-3,5: 40mEq KCl/h + iniciar insulina concomitante
  • K+ 3,5-5,0: 20-40mEq KCl na solução de hidratação
  • K+ > 5,5:   Não repor; Reavaliação em 2h
  (KCl 19,1% — ampola 10mL = 25mEq)

BICARBONATO: APENAS se pH < 6,9
  • 100mEq NaHCO3 8,4% em 400mL AD → infundir em 2h

MONITORIZAÇÃO: Gasometria a cada 2-3h | HGT horário
→ TRANSFERÊNCIA UTI: pH < 7,0 | K+ instável | Sem melhora em 4h | Glasgow < 14

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[I] PROTOCOLO 08 — SEPSE E CHOQUE SÉPTICO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RECONHECIMENTO — qSOFA ≥ 2:
  • FR ≥ 22irpm  |  Alteração mental (Glasgow)  |  PAS ≤ 100mmHg
  Confirmar disfunção orgânica: LACTATO ≥ 2 na Gasometria

BUNDLE 1ª HORA:
  1. HGT + Gasometria (lactato inicial)
  2. Acesso venoso calibroso | Coleta antes dos antibióticos
  3. ANTIBIÓTICO EMPÍRICO EM ATÉ 1H:
     - Foco Pulmonar: Ceftriaxona 2g IV + Azitromicina 500mg IV
     - Foco Urinário: Ceftriaxona 2g IV (ou Cipro 400mg IV se risco ESBL)
     - Foco Abdominal: Ceftriaxona 1g IV + Metronidazol 500mg IV
     - Sem Foco: Ceftriaxona 2g IV + Metronidazol 500mg IV
  4. Ressuscitação: 30mL/kg SF0,9% ou RL em 3h (≈2000mL para 70kg)
  5. EAS (identificar foco urinário)

CHOQUE SÉPTICO (PAS < 90 após volume + Lactato > 4):
  Norepinefrina 0,01-3mcg/kg/min IV
  • Diluição: 4mg em 250mL SG5% = 16mcg/mL
  • Meta PAM ≥ 65mmHg
  → TRANSFERÊNCIA UTI URGÊNCIA MÁXIMA

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[J] PROTOCOLO 09 — DOR ABDOMINAL AGUDA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SEMPRE ACIONAR CIRURGIÃO se: rigidez, peritonismo, Blumberg+, abdome agudo

ANALGESIA (NUNCA negar analgesia — não mascarar piora):
  • Dipirona 1g IV em 100mL SF → infundir em 15min
  • Cetoprofeno 100mg IV (se sem contraindicações renais/hemostasia)
  • Buscopan 20mg IV + Dipirona (se cólica)
  • Tramadol 100mg IV diluído em 100mL SF → 30min
  • Morfina 2-4mg IV (dor intensa, cirurgia excluída)

CÓLICA NEFRÉTICA:
  • Dipirona 1g + Buscopan 20mg IV
  • Cetoprofeno 100mg IV ou Tenoxicam 40mg IV
  • Hidratação SF0,9% 500mL IV
  • EAS (confirmar hematúria micro/macroscópica)
  • TC abdome s/contraste (tamanho do cálculo, local)
  • Alta: Analgésico VO + Tamsulosina 0,4mg/dia (se < 10mm) + retorno urologia

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[K] PROTOCOLO 10 — ARRITMIAS CARDÍACAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

COM INSTABILIDADE (PAS < 90, síncope, EAP, dor torácica):
  → CARDIOVERSÃO ELÉTRICA SINCRONIZADA IMEDIATA
  FA/Flutter: 100-200J bifásico | TSV: 50-100J | TV c/ pulso: 100-200J
  FV/TV sem pulso: DESFIBRILAÇÃO 200J + ACLS

TAQUIARRITMIA ESTÁVEL:
  TSV:
  1. Manobra de Valsalva modificada (deitado + elevação MMII pós-manobra)
  2. Adenosina 6mg IV bolus rápido + flush 20mL SF → 12mg → 12mg
  3. Metoprolol 2,5-5mg IV lento (1mg/min) se falhar adenosina

  FA com RVR (FC > 110):
  1. Metoprolol 5mg IV (0,5mg/min, máx 3 doses de 5mg)
  2. Amiodarona 300mg IV em 20-30min (FA recente < 48h ou FE reduzida)

  TV monomórfica estável:
  Amiodarona 150mg IV em 10min → 1mg/min por 6h → 0,5mg/min

BRADICARDIA SINTOMÁTICA:
  1. Atropina 0,5mg IV a cada 3-5min (máx 3mg)
  2. Dopamina 2-10mcg/kg/min IV (200mg em 250mL SG5%)
  3. → TRANSFERÊNCIA para implante de marcapasso

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[L] PROTOCOLO PEDIÁTRICO (Pediatra deve ser acionado)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FEBRE:
  • Paracetamol 10-15mg/kg/dose VO a cada 6h (máx 75mg/kg/dia)
  • Ibuprofeno 5-10mg/kg/dose VO a cada 8h (> 6 meses; máx 40mg/kg/dia)
  • Dipirona 10-15mg/kg/dose VO/IV (avaliar individualmente)
  ✗ NÃO usar AAS em < 12 anos (risco Síndrome de Reye)

DESIDRATAÇÃO:
  Leve-Moderada: TRO com SRO 50-100mL/kg em 4h
  Grave (> 10% ou sinais de choque): RL 20mL/kg IV em bolus → repetir

BRONCOESPASMO:
  Salbutamol 0,15mg/kg (mín 1,25mg; máx 5mg) NBZ a cada 20min (3x)
  Ipratrópio 0,25-0,5mg NBZ (primeiras 3 doses)
  Prednisolona 1-2mg/kg VO (máx 40mg)

HOLLIDAY-SEGAR (manutenção EV):
  < 10kg:  100mL/kg/dia
  10-20kg: 1000mL + 50mL/kg para cada kg > 10kg
  > 20kg:  1500mL + 20mL/kg para cada kg > 20kg

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[M] FARMÁCIA DO PA — MEDICAMENTOS DISPONÍVEIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ANALGÉSICOS/ANTITÉRMICOS: Dipirona 500mg/mL amp | Paracetamol 200mg/mL gt /
  750mg comp | Ibuprofeno 600mg comp | Cetoprofeno 100mg amp/comp |
  Tramadol 50mg/mL amp | Morfina 10mg/mL amp | AAS 100/500mg comp |
  Tenoxicam 40mg amp

ANTIBIÓTICOS IV: Ceftriaxona 1g/2g amp | Ampicilina+Sulbactam 3g amp |
  Metronidazol 500mg/100mL fr | Ciprofloxacino 200mg/100mL fr |
  Vancomicina 500mg amp | Clindamicina 600mg amp | Azitromicina 500mg amp

ANTIBIÓTICOS VO: Amoxicilina 500mg | Amox+Clavulanato 875/125mg |
  Azitromicina 500mg | Ciprofloxacino 500mg | SMX/TMP 400/80mg |
  Nitrofurantoína 100mg

CARDIOVASCULARES IV: Adrenalina 1mg/mL amp | Norepinefrina 4mg/4mL amp |
  Dopamina 50mg/mL amp | Amiodarona 150mg/3mL amp | Adenosina 6mg/2mL amp |
  Atropina 0,5mg/mL amp | Digoxina 0,5mg/2mL amp | Enalaprilato 1,25mg/mL amp |
  Nitroprussiato 50mg amp | Furosemida 10mg/mL amp | Hidralazina 20mg amp

CARDIOVASCULARES VO: AAS 100mg | Captopril 25mg | Enalapril 10mg |
  Atenolol 50mg | Metoprolol 25mg/50mg | Furosemida 40mg |
  Espironolactona 25/50mg | Nifedipino retard 30mg | Clonidina 0,1mg |
  Isossorbida SL 5mg | Nitrato Spray 0,4mg

ANTICOAGULANTES: Enoxaparina 20/40/60/80/100mg seringas | HNF 5000UI/mL amp

NEUROLÓGICO: Diazepam 5mg/mL amp | Midazolam 5mg/mL amp |
  Fenitoína 50mg/mL amp | Fenobarbital 100mg/mL amp |
  Haloperidol 5mg/mL amp | Clonazepam gotas

ENDOCRINOLOGIA: Insulina Regular IV/SC | Insulina NPH SC |
  SG50% amp 10mL | Glucagon kit | Glibenclamida | Metformina

ALÉRGICO/INFLAMATÓRIO: Adrenalina 1:1000 | Difenidramina 25mg/mL amp |
  Prometazina 25mg/mL amp | Dexametasona 4mg/mL amp |
  Metilprednisolona 125/500mg fr

GASTRO/ANTIEMÉTICO: Ondansetrona 4mg/2mL amp | Metoclopramida 10mg/2mL amp |
  Pantoprazol 40mg amp | Omeprazol 20mg comp | Ranitidina 50mg amp |
  Butilescopolamina 20mg amp | Domperidona 10mg comp

BRONCODILATADORES: Salbutamol 5mg/mL NBZ | Ipratrópio 0,25mg/mL NBZ |
  Aminofilina 240mg/10mL amp | Fenoterol NBZ

SOLUÇÕES: SF0,9% 100/250/500/1000mL | SG5% 100/250/500mL | SG10% 500mL |
  RL 500/1000mL | SG50% 250mL | KCl 19,1% amp | NaHCO3 8,4% amp | AD 10mL

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[N] CRITÉRIOS ABSOLUTOS DE TRANSFERÊNCIA (Acionar Vaga Zero / SUS Fácil)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  • IAMCSST / IAMSST instável → Hemodinâmica
  • Choque cardiogênico / Choque séptico → UTI
  • AVC isquêmico em janela / AVC hemorrágico → Centro AVC / Neurocirurgia
  • Status epilepticus refratário → UTI Neurológica
  • CAD grave (pH < 7,0, K+ instável) → UTI
  • IOT / VM necessária → UTI
  • Cirurgia de emergência → Hospital Cirúrgico referência
  • Instabilidade hemodinâmica refratária → UTI
  • Qualquer condição que exija monitorização intensiva > 12h
"""
