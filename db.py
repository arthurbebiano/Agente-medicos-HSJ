"""
db.py
Gerenciamento do banco de dados com Firebase Realtime Database.
ID gerado via: SHA1(INICIAIS + TIMESTAMP_ms + PEPPER)[:8]
"""

import json
import hashlib
import time
from typing import Optional
from datetime import datetime

try:
    import firebase_admin
    from firebase_admin import credentials, db
    FIREBASE_AVAILABLE = True
except ImportError:
    FIREBASE_AVAILABLE = False


# ──────────────────────────────────────────────────────────────
# INICIALIZAÇÃO FIREBASE
# ──────────────────────────────────────────────────────────────

_firebase_initialized = False


def _init_firebase() -> bool:
    """Inicializa Firebase uma única vez."""
    global _firebase_initialized
    if _firebase_initialized or not FIREBASE_AVAILABLE:
        return _firebase_initialized

    try:
        import streamlit as st

        firebase_config = dict(st.secrets.get("firebase", {}))
        if not firebase_config:
            return False

        # Verificar se já inicializado
        if not firebase_admin.get_app():
            cred = credentials.Certificate(firebase_config)
            firebase_admin.initialize_app(
                cred,
                {"databaseURL": "https://agente-medicos-hfr.firebaseio.com"},
            )
        _firebase_initialized = True
        return True

    except Exception as e:
        print(f"⚠️ Firebase inicialização falhou: {e}")
        return False


# ──────────────────────────────────────────────────────────────
# HELPER — PEPPER
# ──────────────────────────────────────────────────────────────


def _get_pepper() -> str:
    try:
        import streamlit as st

        return st.secrets.get("PEPPER", "DEFAULT_PEPPER_HGS_2024")
    except Exception:
        return "DEFAULT_PEPPER_HGS_2024"


# ──────────────────────────────────────────────────────────────
# GERAÇÃO DE ID ÚNICO COM PEPPER
# ──────────────────────────────────────────────────────────────


def gerar_id(nome: str) -> str:
    """
    Gera um ID único e rastreável.
    Formato: INICIAIS-HASH8CHARS
    Ex:     MAS-3F9A1B2C
    """
    pepper = _get_pepper()

    palavras = [p for p in nome.strip().split() if p]
    iniciais = "".join(p[0].upper() for p in palavras)[:4] if palavras else "XX"

    timestamp_ms = str(int(time.time() * 1000))
    raw = f"{iniciais}{timestamp_ms}{pepper}"
    hash_hex = hashlib.sha1(raw.encode("utf-8")).hexdigest()[:8].upper()

    return f"{iniciais}-{hash_hex}"


# ──────────────────────────────────────────────────────────────
# CRUD — COM FALLBACK LOCAL (JSON)
# ──────────────────────────────────────────────────────────────


def criar_paciente(nome: str, historico: list, dados_extras: Optional[dict] = None) -> str:
    """
    Cria novo prontuário e retorna o ID.
    Tenta Firebase primeiro; fallback para JSON local.
    """
    patient_id = gerar_id(nome)
    tentativas = 0

    record = {
        "nome": nome,
        "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "historico": historico,
        "dados_extras": dados_extras or {},
    }

    # ── Tentar Firebase ──────────────────────────────────────
    if _init_firebase():
        try:
            ref = db.reference(f"pacientes/{patient_id}")
            ref.set(record)
            return patient_id
        except Exception as e:
            print(f"⚠️ Firebase write falhou: {e}. Usando JSON local...")

    # ── Fallback JSON local ──────────────────────────────────
    import os

    DB_FILE = "pacientes.json"
    data = {}

    if os.path.exists(DB_FILE):
        try:
            with open(DB_FILE, "r", encoding="utf-8") as f:
                data = json.load(f) or {}
        except Exception:
            data = {}

    # Evitar colisão de ID
    while patient_id in data and tentativas < 10:
        time.sleep(0.002)
        patient_id = gerar_id(nome)
        tentativas += 1

    data[patient_id] = record

    try:
        with open(DB_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"⚠️ Falha ao salvar JSON local: {e}")

    return patient_id


def atualizar_historico(patient_id: str, historico: list) -> bool:
    """
    Atualiza o histórico de conversa de um prontuário existente.
    Firebase primeiro; fallback JSON.
    """
    # ── Tentar Firebase ──────────────────────────────────────
    if _init_firebase():
        try:
            ref = db.reference(f"pacientes/{patient_id}/historico")
            ref.set(historico)
            return True
        except Exception as e:
            print(f"⚠️ Firebase update falhou: {e}. Usando JSON local...")

    # ── Fallback JSON local ──────────────────────────────────
    import os

    DB_FILE = "pacientes.json"
    data = {}

    if os.path.exists(DB_FILE):
        try:
            with open(DB_FILE, "r", encoding="utf-8") as f:
                data = json.load(f) or {}
        except Exception:
            data = {}

    if patient_id not in data:
        return False

    data[patient_id]["historico"] = historico

    try:
        with open(DB_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"⚠️ Falha ao atualizar JSON local: {e}")
        return False


def carregar_todos_pacientes() -> dict:
    """
    Retorna todos os prontuários.
    Tenta Firebase primeiro; fallback JSON.
    """
    # ── Tentar Firebase ──────────────────────────────────────
    if _init_firebase():
        try:
            ref = db.reference("pacientes")
            data = ref.get().val()
            return data if isinstance(data, dict) else {}
        except Exception as e:
            print(f"⚠️ Firebase read falhou: {e}. Usando JSON local...")

    # ── Fallback JSON local ──────────────────────────────────
    import os

    DB_FILE = "pacientes.json"
    if not os.path.exists(DB_FILE):
        return {}

    try:
        with open(DB_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def carregar_paciente(patient_id: str) -> Optional[dict]:
    """
    Retorna um prontuário específico ou None.
    Firebase primeiro; fallback JSON.
    """
    # ── Tentar Firebase ──────────────────────────────────────
    if _init_firebase():
        try:
            ref = db.reference(f"pacientes/{patient_id}")
            data = ref.get().val()
            return data if isinstance(data, dict) else None
        except Exception as e:
            print(f"⚠️ Firebase read falhou: {e}. Usando JSON local...")

    # ── Fallback JSON local ──────────────────────────────────
    all_data = carregar_todos_pacientes()
    return all_data.get(patient_id)


def deletar_paciente(patient_id: str) -> bool:
    """
    Remove um prontuário do banco.
    Firebase primeiro; fallback JSON.
    """
    # ── Tentar Firebase ──────────────────────────────────────
    if _init_firebase():
        try:
            ref = db.reference(f"pacientes/{patient_id}")
            ref.delete()
            return True
        except Exception as e:
            print(f"⚠️ Firebase delete falhou: {e}. Usando JSON local...")

    # ── Fallback JSON local ──────────────────────────────────
    import os

    DB_FILE = "pacientes.json"
    data = {}

    if os.path.exists(DB_FILE):
        try:
            with open(DB_FILE, "r", encoding="utf-8") as f:
                data = json.load(f) or {}
        except Exception:
            data = {}

    if patient_id not in data:
        return False

    del data[patient_id]

    try:
        with open(DB_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"⚠️ Falha ao deletar no JSON local: {e}")
        return False
