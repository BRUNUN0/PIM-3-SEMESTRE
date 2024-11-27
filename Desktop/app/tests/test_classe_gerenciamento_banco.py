import pytest
from unittest.mock import MagicMock
import pyodbc
from app.components.gerenciamento_banco import GerenciamentoBanco
# Supondo que sua classe seja chamada GerenciamentoBanco
# from seu_modulo import GerenciamentoBanco


@pytest.fixture
def mock_conexao(mocker):
    mock_conn = mocker.patch('pyodbc.connect')
    mock_cursor = MagicMock()
    mock_conn.return_value.cursor.return_value = mock_cursor
    return mock_conn, mock_cursor


def test_cadastro_fornecedor(mock_conexao):
    mock_conn, mock_cursor = mock_conexao
    
    # Definindo os dados para o cadastro de fornecedor
    dados = {
        'Nome': 'Fornecedor Teste',
        'Nome Fantasia': 'Fornecedor Teste Ltda',
        'CNPJ': '12.345.678/0001-90',
        'Email': 'fornecedor@teste.com',
        'Telefone': '(11) 98765-4321',
        'Rua': 'Rua Teste',
        'Número': '123',
        'Bairro': 'Bairro Teste',
        'CEP': '12345-678',
        'Cidade': 'Cidade Teste',
        'Estado': 'SP'
    }
    
    # Instanciando a classe
    banco = GerenciamentoBanco()

    # Simulando a chamada do método
    resultado, erro = banco.cadastro('fornecedor', dados)

    # Verificando o comportamento esperado
    assert resultado is True
    assert erro is None
    mock_cursor.execute.assert_called_once_with(
        '''{CALL InserirFornecedor (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)}''',
        (dados['Nome'], dados['Nome Fantasia'], dados['CNPJ'], dados['Email'], dados['Telefone'], dados['Rua'], dados['Número'], dados['Bairro'], dados['CEP'], dados['Cidade'], dados['Estado'])
    )
    mock_conn.return_value.commit.assert_called_once()


def test_cadastro_cliente(mock_conexao):
    mock_conn, mock_cursor = mock_conexao
    
    # Dados para cadastro de cliente
    dados = {
        'Nome': 'Cliente Teste',
        'Nome Fantasia': 'Cliente Teste Ltda',
        'CNPJ': '98.765.432/0001-10',
        'Email': 'cliente@teste.com',
        'Rua': 'Rua Cliente',
        'Numero': '456',
        'Bairro': 'Bairro Cliente',
        'CEP': '98765-432',
        'Cidade': 'Cidade Cliente',
        'Estado': 'SP'
    }

    banco = GerenciamentoBanco()
    
    resultado, erro = banco.cadastro('cliente', dados)

    assert resultado is True
    assert erro is None
    mock_cursor.execute.assert_called_once_with(
        '''{CALL InserirCliente (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)}''',
        (dados['Nome'], dados['Nome Fantasia'], dados['CNPJ'], dados['Email'], dados['Rua'], dados['Numero'], dados['Bairro'], dados['CEP'], dados['Cidade'], dados['Estado'])
    )
    mock_conn.return_value.commit.assert_called_once()


def test_erro_integridade(mock_conexao):
    mock_conn, mock_cursor = mock_conexao
    mock_cursor.execute.side_effect = pyodbc.IntegrityError("Erro de integridade", "SQL")

    dados = {
        'Nome': 'Fornecedor Teste',
        'Nome Fantasia': 'Fornecedor Teste Ltda',
        'CNPJ': '12.345.678/0001-90',
        'Email': 'fornecedor@teste.com',
        'Telefone': '(11) 98765-4321',
        'Rua': 'Rua Teste',
        'Número': '123',
        'Bairro': 'Bairro Teste',
        'CEP': '12345-678',
        'Cidade': 'Cidade Teste',
        'Estado': 'SP'
    }

    banco = GerenciamentoBanco()

    resultado, erro = banco.cadastro('fornecedor', dados)

    assert resultado is False
    assert erro == "Erro de integridade"  # Agora esperamos somente a mensagem de erro.
    mock_conn.return_value.rollback.assert_called_once()


def test_erro_programacao(mock_conexao):
    mock_conn, mock_cursor = mock_conexao
    mock_cursor.execute.side_effect = pyodbc.ProgrammingError("Erro de programação", "SQL")

    dados = {
        'Nome': 'Fornecedor Teste',
        'Nome Fantasia': 'Fornecedor Teste Ltda',
        'CNPJ': '12.345.678/0001-90',
        'Email': 'fornecedor@teste.com',
        'Telefone': '(11) 98765-4321',
        'Rua': 'Rua Teste',
        'Número': '123',
        'Bairro': 'Bairro Teste',
        'CEP': '12345-678',
        'Cidade': 'Cidade Teste',
        'Estado': 'SP'
    }

    banco = GerenciamentoBanco()

    resultado, erro = banco.cadastro('fornecedor', dados)

    assert resultado is False
    assert erro == "Erro de programação"  # Agora esperamos somente a mensagem de erro.
    mock_conn.return_value.rollback.assert_called_once()


def test_erro_generico(mock_conexao):
    mock_conn, mock_cursor = mock_conexao
    mock_cursor.execute.side_effect = pyodbc.Error("Erro desconhecido", "SQL")

    dados = {
        'Nome': 'Fornecedor Teste',
        'Nome Fantasia': 'Fornecedor Teste Ltda',
        'CNPJ': '12.345.678/0001-90',
        'Email': 'fornecedor@teste.com',
        'Telefone': '(11) 98765-4321',
        'Rua': 'Rua Teste',
        'Número': '123',
        'Bairro': 'Bairro Teste',
        'CEP': '12345-678',
        'Cidade': 'Cidade Teste',
        'Estado': 'SP'
    }

    banco = GerenciamentoBanco()

    resultado, erro = banco.cadastro('fornecedor', dados)

    assert resultado is False
    assert erro == "Erro desconhecido"  # Agora esperamos somente a mensagem de erro.
    mock_conn.return_value.rollback.assert_called_once()
