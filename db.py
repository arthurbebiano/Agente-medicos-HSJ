"""
Gerenciamento do banco de dados local (pacientes.json).
ID gerado via: SHA1(INICIAIS + TIMESTAMP_ms + PEPPER)[:8]
"""

import json
import os
import hashlib
import time
from typing import Optional
from datetime import datetime

DB_FILE = "pacientes.json"


# ──────────────────────────────────────────────────────────────
# PRIVADO — I/O do JSON
# ──────────────────────────────────────────────────────────────

def _load_db() -> dict:
    if not os.path.exists(DB_FILE):
        return {}
    try:
        with open(DB_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, dict) else {}
    except (json.JSONDecodeError, IOError, ValueError):
        return {}


def _save_db(data: dict) -> bool:
    try:
        with open(DB_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except IOError:
        return False


def _get_pepper() -> str:
    try:
        import streamlit as st
        return st.secrets["PEPPER"]
    except Exception:
        return "DEFAULT_PEPPER_FALLBACK_HGS_2024"


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
# CRUD
# ──────────────────────────────────────────────────────────────

def criar_paciente(nome: str, historico: list, dados_extras: Optional[dict] = None) -> str:
    """
    Cria novo prontuário e retorna o ID.

    Estrutura do registro:
    {
        "ID": {
            "nome":        str,
            "data":        str  (DD/MM/YYYY HH:MM),
            "historico":   [ {"role": str, "parts": [str]}, ... ],
            "dados_extras": dict
        }
    }
    """
    db = _load_db()

    patient_id = gerar_id(nome)
    tentativas = 0
    while patient_id in db and tentativas < 10:
        time.sleep(0.002)
        patient_id = gerar_id(nome)
        tentativas += 1

    db[patient_id] = {
        "nome": nome,
        "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "historico": historico,
        "dados_extras": dados_extras or {},
    }

    _save_db(db)
    return patient_id


def atualizar_historico(patient_id: str, historico: list) -> bool:
    """Atualiza o histórico de conversa de um prontuário existente."""
    db = _load_db()
    if patient_id not in db:
        return False
    db[patient_id]["historico"] = historico
    return _save_db(db)


def carregar_todos_pacientes() -> dict:
    """Retorna todos os prontuários."""
    return _load_db()


def carregar_paciente(patient_id: str) -> Optional[dict]:
    """Retorna um prontuário específico ou None."""
    return _load_db().get(patient_id)


def deletar_paciente(patient_id: str) -> bool:
    """Remove um prontuário do banco."""
    db = _load_db()
    if patient_id not in db:
        return False
    del db[patient_id]
    return _save_db(db)
