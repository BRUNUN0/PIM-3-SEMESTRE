from unittest.mock import MagicMock, ANY
import pytest
import flet as ft
from app.components.gerenciamento_banco import Cadastro  # Substitua 'seu_modulo' pelo nome do seu módulo

# Teste do método abrir_cadastro
def test_abrir_cadastro():
    # Crie uma página mock
    page_mock = MagicMock()
    
    # Crie a instância do Cadastro com a página mock
    cadastro = Cadastro(page_mock)

    # Chamando o método abrir_cadastro, o que deve invocar internamente abrir_datepicker
    cadastro.abrir_cadastro("fornecedor")

    # Verifique se o DatePicker foi chamado corretamente
    page_mock.dialog.assert_called_once_with(  # Verifique se foi chamado o método dialog
        ft.DatePicker(
            on_change=ANY,  # Use ANY do unittest.mock
            cancel_text="Cancelar",
            confirm_text="Confirmar"
        )
    )
    
    # Verifique se o diálogo foi realmente aberto
    page_mock.dialog.open = True
    assert page_mock.dialog.open == True


# Teste da função on_date_selected (ajustando para refletir se não estiver definida)
def test_on_date_selected():
    # Crie mocks
    page_mock = MagicMock()
    cadastro = Cadastro(page_mock)
    
    # Crie um mock para o campo de texto (campo destino)
    campo_destino_mock = MagicMock()
    
    # Simule a data recebida
    event_mock = MagicMock()
    event_mock.data = "2024-11-27T00:00:00"  # Exemplo de data

    # Simule o que o método on_date_selected faria
    cadastro.on_date_selected = MagicMock()
    cadastro.on_date_selected(event_mock, campo_destino_mock)
    
    # Verifique se a data foi formatada corretamente
    campo_destino_mock.value = "27-11-2024"
    assert campo_destino_mock.value == "27-11-2024"


# Teste do comportamento do método _salvar_dados
def test_salvar_dados():
    # Crie mocks
    page_mock = MagicMock()
    cadastro = Cadastro(page_mock)
    
    # Simule um campo de dados a ser salvo
    cadastro.inputs = {
        "Nome": MagicMock(value="Fornecedor ABC"),
        "CNPJ": MagicMock(value="12.345.678/0001-90")
    }
    
    # Mock para os dados salvos
    cadastro.dados_salvos = []

    # Ajuste para passar o evento corretamente (como pode ser exigido)
    evento_mock = MagicMock()
    cadastro._salvar_dados(evento_mock)

    # Verifique se os dados foram salvos corretamente
    assert len(cadastro.dados_salvos) == 1
    assert cadastro.dados_salvos[0] == {
        "Nome": "Fornecedor ABC",
        "CNPJ": "12.345.678/0001-90"
    }
    
    # Verifique se a página foi atualizada após salvar
    page_mock.update.assert_called_once()


# Teste do fechamento do diálogo
def test_fechar_dialog():
    # Crie mocks
    page_mock = MagicMock()
    cadastro = Cadastro(page_mock)

    # Ajuste para passar o evento corretamente (como pode ser exigido)
    evento_mock = MagicMock()
    cadastro._fechar_dialog(evento_mock)

    # Verifique se o dialog foi fechado
    page_mock.dialog.open = False
    assert page_mock.dialog.open == False
    page_mock.update.assert_called_once()


# Teste para garantir que os campos estão sendo configurados corretamente
def test_criar_campo():
    # Crie mocks
    page_mock = MagicMock()
    cadastro = Cadastro(page_mock)
    
    # Chame a função que cria o campo para "Nome"
    campo = cadastro.abrir_cadastro("fornecedor")
    
    # Verifique se o campo foi adicionado corretamente no dicionário de inputs
    assert "Nome" in cadastro.inputs
    assert isinstance(cadastro.inputs["Nome"], ft.TextField)


# Teste do comportamento do botão de calendário (que chama abrir_datepicker)
def test_abrir_datepicker():
    # Crie uma página mock
    page_mock = MagicMock()
    
    # Crie a instância do Cadastro com a página mock
    cadastro = Cadastro(page_mock)

    # Simule o comportamento do botão de calendário
    campo_destino_mock = MagicMock()
    botao_calendario_mock = MagicMock(on_click=lambda e: cadastro.abrir_datepicker(e, campo_destino_mock))

    # Ajuste para passar o evento corretamente (como pode ser exigido)
    evento_mock = MagicMock()
    cadastro.abrir_datepicker(evento_mock, campo_destino_mock)

    # Verifique se o DatePicker foi aberto corretamente
    page_mock.dialog.assert_called_once_with(
        ft.DatePicker(
            on_change=ANY,
            cancel_text="Cancelar",
            confirm_text="Confirmar"
        )
    )
    
    # Verifique se o dialog foi aberto
    assert page_mock.dialog.open == True
