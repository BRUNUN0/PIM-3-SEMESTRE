import pytest
from unittest import mock
from datetime import datetime
from app.components.gerenciamento_banco import Cadastro  # Supondo que a classe Cadastro esteja nesse arquivo

@pytest.fixture
def mock_page():
    # Mock da página do Flet
    mock_page = mock.MagicMock()
    mock_page.update = mock.MagicMock()
    mock_page.overlay.append = mock.MagicMock()
    mock_page.dialog = None
    return mock_page


@pytest.fixture
def cadastro(mock_page):
    return Cadastro(mock_page)


def test_abrir_cadastro(cadastro, mock_page):
    # Mock da resposta do Flet para abrir o dialog
    with mock.patch.object(cadastro.page, 'overlay') as mock_overlay, \
         mock.patch.object(cadastro.page, 'update') as mock_update:
        cadastro.abrir_cadastro("fornecedor")

        # Verificar se o dialog foi aberto
        assert cadastro.dialog is not None
        mock_overlay.append.assert_called_once()
        mock_update.assert_called_once()


def test_campos_do_cadastro(cadastro):
    # Testar se os campos para o cadastro de fornecedor estão corretos
    cadastro.abrir_cadastro("fornecedor")
    
    campos_esperados = [
        "Nome", "Nome Fantasia", "CNPJ", "Email", "Telefone",  # Informações Básicas
        "Rua", "Número", "Bairro", "CEP", "Cidade", "Estado"   # Endereço
    ]
    
    # Verificar se todos os campos esperados estão presentes
    for campo in campos_esperados:
        assert campo in cadastro.campos_relevantes


def test_abrir_datepicker(cadastro, mock_page):
    # Testar a função que abre o DatePicker
    with mock.patch.object(cadastro.page, 'dialog') as mock_dialog:
        # Simular que o botão de calendário foi clicado
        mock_button = mock.MagicMock()
        mock_button.on_click = mock.MagicMock()

        # Simular a chamada do evento para abrir o DatePicker
        cadastro.abrir_datepicker(None, mock.MagicMock())
        
        # Verificar se o DatePicker foi aberto
        mock_dialog.open = True
        cadastro.page.update.assert_called_once()


def test_on_date_selected(cadastro):
    # Testar a função on_date_selected
    campo_destino_mock = mock.MagicMock()
    evento_mock = mock.MagicMock()
    evento_mock.data = '2024-11-27T00:00:00Z'
    
    cadastro.on_date_selected(evento_mock, campo_destino_mock)
    
    # Verificar se o valor do campo destino foi atualizado corretamente
    campo_destino_mock.value = '27-11-2024'
    assert campo_destino_mock.value == '27-11-2024'


def test_salvar_dados(cadastro, mock_page):
    # Testar o método de salvar dados com campos obrigatórios
    cadastro.inputs = {
        "Nome": mock.MagicMock(value="Fornecedor X"),
        "CNPJ": mock.MagicMock(value="12345678000199"),
        "Email": mock.MagicMock(value="fornecedor@example.com")
    }
    cadastro.campos_relevantes = ["Nome", "CNPJ", "Email"]
    
    with mock.patch.object(cadastro.page, 'update') as mock_update:
        cadastro._salvar_dados(None)
        
        # Verificar se a atualização da página foi chamada após salvar os dados
        mock_update.assert_called_once()

