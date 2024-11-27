from unittest.mock import MagicMock
import pytest
from hashlib import sha256
from app.components.funcionario import Funcionario
from app.components.gerenciamento_banco import GerenciamentoBanco as gbd
from app.components.validacao import Validacao  # Substitua 'app.components' pelo caminho correto do seu módulo

# Teste do método validar_cpf
def test_validar_cpf_valido():
    validacao = Validacao()
    
    # CPF válido
    cpf_valido = "123.456.789-09"
    resultado = validacao.validar_cpf(cpf_valido)
    assert resultado is True

def test_validar_cpf_invalido():
    validacao = Validacao()
    
    # CPF inválido
    cpf_invalido = "123.456.789-00"
    resultado = validacao.validar_cpf(cpf_invalido)
    assert resultado is False

# Teste do método valid_Login
def test_valid_login_sucesso():
    validacao = Validacao()

    # Mock para o banco de dados e o funcionário
    banco_mock = MagicMock()
    funcionario_mock = MagicMock()

    # Dados simulados
    cpf = "443.039.698-18"
    senha = "2507"
    senha_cripto = sha256(senha.encode('utf-8')).hexdigest()

    # Configurar o mock para retornar dados válidos
    funcionario_mock.obter_funcionario_login.return_value = [senha_cripto, cpf, 1, "João", "Administrador"]
    
    # Configurar o mock para o método salvar_sessao
    funcionario_mock.salvar_sessao = MagicMock()

    # Teste de login válido
    resultado = validacao.valid_Login(cpf, senha)
    
    # Verificar se o login foi bem-sucedido
    assert resultado is True
    
    # Verificar se o método salvar_sessao foi chamado uma vez com os parâmetros corretos
    funcionario_mock.salvar_sessao.assert_called_once_with({
        "id": 1,
        "cpf": cpf,
        "nome": "João",
        "cargo": "Administrador"
    })



def test_valid_login_falha():
    validacao = Validacao()

    # Mock para o banco de dados e o funcionário
    banco_mock = MagicMock()
    funcionario_mock = MagicMock()
    
    # Dados simulados
    cpf = "123.456.789-09"
    senha = "senha123"
    senha_cripto = sha256(senha.encode('utf-8')).hexdigest()
    funcionario_mock.obter_funcionario_login.return_value = [senha_cripto, cpf, 1, "João", "Administrador"]

    # Teste de login inválido (senha errada)
    resultado = validacao.valid_Login(cpf, "senhaErrada")
    assert resultado is False

# Teste do método verificar_usuario_logado
def test_verificar_usuario_logado_sucesso():
    validacao = Validacao()

    # Mock para o funcionário e página
    funcionario_mock = MagicMock()
    page_mock = MagicMock()

    # Simular sessão ativa
    funcionario_mock.obter_sessao.return_value = {"id": 1, "cpf": "123.456.789-09", "nome": "João", "cargo": "Administrador"}
    
    # Teste se o usuário está logado
    resultado = validacao.verificar_usuario_logado(funcionario_mock, page_mock)
    assert resultado is True

def test_verificar_usuario_logado_erro():
    validacao = Validacao()

    # Mock para o funcionário e página
    funcionario_mock = MagicMock()
    page_mock = MagicMock()

    # Simular sessão não ativa
    funcionario_mock.obter_sessao.return_value = None
    
    # Teste se o usuário não está logado e é redirecionado
    resultado = validacao.verificar_usuario_logado(funcionario_mock, page_mock)
    assert resultado is False
    page_mock.go.assert_called_once_with('/login')

# Teste do método Logout
def test_logout():
    validacao = Validacao()

    # Mock para o funcionário e página
    funcionario_mock = MagicMock()
    page_mock = MagicMock()

    # Simular logout
    Validacao.Logout(page_mock, funcionario_mock)
    
    # Verificar se a sessão foi limpa e se redirecionou para o login
    funcionario_mock.limpar_sessao.assert_called_once()
    page_mock.go.assert_called_once_with('/login')
