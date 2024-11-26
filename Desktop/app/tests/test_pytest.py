import pytest
import flet as ft
from unittest.mock import Mock, patch
from app.components.detalhes import Detalhes
from flet import app, Page, Text


#Tag padrões que utilizaremos para rodar testes: BancoDeDados | Seguranca | Usabilidade 


@pytest.fixture
def detalhes_instance():
    # Cria uma instância da classe Detalhes
    detalhes = Detalhes(None, None)
    return detalhes

@pytest.mark.Seguranca
def test_hash_password_sha256():
    detalhes = Detalhes(None, None)  # Cria um objeto Detalhes

    # Senhas de teste
    senhas = ["senha123", "senhaforte", "123456"]

    # Gera os hashes
    hashes = [detalhes.hash_password_sha256(senha) for senha in senhas]

    # Verifica se todos os hashes são diferentes
    assert len(set(hashes)) == len(senhas)

    # Verifica se o hash da primeira senha é gerado consistentemente
    primeiro_hash = detalhes.hash_password_sha256(senhas[0])
    assert primeiro_hash == hashes[0]

    # Verifica o comprimento do hash (SHA-256 tem 64 caracteres hexadecimais)
    assert len(hashes[0]) == 64


@pytest.mark.BancoDeDados
def test_conectar():
    ...