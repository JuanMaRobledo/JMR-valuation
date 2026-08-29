import os

import pytest

from jmr_valuation.io.env import load_dotenv
from jmr_valuation.io.fiscal_ai_client import FiscalAIClient, FiscalAIError


def test_client_raises_clear_error_without_api_key(monkeypatch):
    monkeypatch.delenv("FISCAL_AI_API_KEY", raising=False)
    # anula la carga de .env real del proyecto para que el test no dependa de
    # si existe (o no) un .env con una clave real en la maquina que lo corre.
    monkeypatch.setattr("jmr_valuation.io.fiscal_ai_client.load_dotenv", lambda: None)
    with pytest.raises(FiscalAIError, match="Falta la API key"):
        FiscalAIClient()


def test_client_accepts_explicit_api_key():
    client = FiscalAIClient(api_key="test-key-123")
    assert client.api_key == "test-key-123"


def test_load_dotenv_sets_environment_variables(tmp_path, monkeypatch):
    env_file = tmp_path / ".env"
    env_file.write_text('FISCAL_AI_API_KEY=abc123\nOTHER_VAR="quoted value"\n# comentario\n')
    monkeypatch.delenv("FISCAL_AI_API_KEY", raising=False)
    monkeypatch.delenv("OTHER_VAR", raising=False)

    load_dotenv(env_file)

    assert os.environ["FISCAL_AI_API_KEY"] == "abc123"
    assert os.environ["OTHER_VAR"] == "quoted value"


def test_load_dotenv_does_not_override_existing_env_var(tmp_path, monkeypatch):
    env_file = tmp_path / ".env"
    env_file.write_text("FISCAL_AI_API_KEY=from_file\n")
    monkeypatch.setenv("FISCAL_AI_API_KEY", "from_shell")

    load_dotenv(env_file)

    assert os.environ["FISCAL_AI_API_KEY"] == "from_shell"


def test_load_dotenv_missing_file_is_a_noop(tmp_path):
    load_dotenv(tmp_path / "does_not_exist.env")  # no debe explotar
