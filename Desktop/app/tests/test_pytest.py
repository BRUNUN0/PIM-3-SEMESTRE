import pyodbc
import pytest
import flet as ft
from app.components.gerenciamento_banco import GerenciamentoBanco, Excluir
from unittest.mock import Mock, patch
from app.components.detalhes import Detalhes
from flet import app, Page, Text


# ========= Testes =========


@pytest.fixture
def gbd():
    gbd = GerenciamentoBanco()
    # Configura um banco de dados de teste


@pytest.fixture
def detalhes_instance():
    # Cria uma instância da classe Detalhes
    detalhes = Detalhes(None, None)
    return detalhes


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


@pytest.mark.parametrize("tipo_cadastro, dados, resultado_esperado, mensagem_esperada", [
    ('fornecedor', {'Nome': 'Soluções Hidropônicas TesteFCN','Nome Fantasia': 'SolHidro Teste','CNPJ': '34567890001155', 'Email': 'suporte@Teste.com.br', 'Telefone' : '(31) 9876-5432', 'Rua': 'Avenida Afonso Pena', 'Número': '1500','Bairro': 'Centro', 'CEP': '30130000','Cidade': 'Belo Horizonte','Estado' :'MG'}, True, None),
    ('cliente', {'Nome': 'Hidroponia TesteFCN','Nome Fantasia': 'Hidroponia Teste', 'CNPJ':'34567890001155' , 'Email': 'atendimento@Teste.com.br', 'Rua':  'Rua das Palmeiras', 'Numero': '404', 'Bairro': 'Bairro Tropicar' , 'CEP':  '34567000', 'Cidade': 'Curitiba', 'Estado': 'RJJ' }, True, None),
    # ... outros casos de teste
])
def test_cadastro(gbd, tipo_cadastro, dados, resultado_esperado, mensagem_esperada):
    gbd = Excluir()
    resultado, mensagem = gbd.cadastro(tipo_cadastro, dados)
    gbd.excluir_func_cli(cnpj = '34567890001155')
    assert resultado == resultado_esperado
    assert mensagem == mensagem_esperada


