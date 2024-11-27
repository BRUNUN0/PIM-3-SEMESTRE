import pytest
from unittest.mock import MagicMock, patch
from app.components.gerenciamento_banco import GerenciamentoBanco
from app.components.producao import Producao

# Mocking da classe GerenciamentoBanco
@pytest.fixture
def mock_banco():
    # Mock do GerenciamentoBanco
    banco_mock = MagicMock(spec=GerenciamentoBanco)
    
    # Criar o mock do cursor
    cursor_mock = MagicMock()
    
    # Associar o mock do cursor ao banco mockado
    banco_mock.cursor = cursor_mock
    banco_mock.conectar.return_value = None
    banco_mock.fechar_conexao.return_value = None
    
    return banco_mock

# Teste para o método obter_producao
def test_obter_producao(mock_banco):
    # Configuração do mock para o cursor
    mock_banco.cursor.fetchall.return_value = [
        (1, "Plantio 1", "Tomate", 100, "url1"),
        (2, "Plantio 2", "Alface", 200, "url2")
    ]
    
    producao = Producao(mock_banco)  # Criando uma instância da classe Producao com o mock
    resultado = producao.obter_producao()  # Chamando o método

    # Verificar se a consulta foi feita corretamente
    mock_banco.cursor.execute.assert_called_once_with('''SELECT
                        p.id_plantio,
                        p.Plantio,
                        p.Nome,
                        p.Quantidade,
                        mp.URL
                    FROM Producao p
                    JOIN Materia_Prima mp ON p.fk_id_materia = mp.id_materia
                    WHERE p.Data_Fim IS NULL;''')
    
    # Verificar o retorno
    assert len(resultado) == 2  # Esperamos 2 registros de produção
    assert resultado[0][1] == "Plantio 1"  # O nome do plantio deve ser "Plantio 1"
    assert resultado[1][4] == "url2"  # A URL do plantio 2 deve ser "url2"

# Teste para o método obter_detalhes_plantio
def test_obter_detalhes_plantio(mock_banco):
    # Configuração do mock para o cursor
    mock_banco.cursor.fetchone.return_value = (1, "Teste Plantio 1", "08/11/2024", "Cebolinha", 10)

    producao = Producao(mock_banco)
    resultado = producao.obter_detalhes_plantio(1)

    # Verificar se a consulta foi feita corretamente, ignorando espaços e quebras de linha
    mock_banco.cursor.execute.assert_called_once_with('''SELECT
                    id_plantio,
                    Plantio,
                    FORMAT(Data_Inicio, 'dd/MM/yyyy') AS Data_Inicio,
                    Nome,
                    Quantidade
                FROM 
                    Producao
                WHERE id_plantio = 1''')
    
    # Verificar o resultado
    assert resultado == (1, "Teste Plantio 1", "08/11/2024", "Cebolinha", 10)



# Teste para o método grafico_qnt_prod_mes
def test_grafico_qnt_prod_mes(mock_banco):
    # Configuração do mock para o cursor
    mock_banco.cursor.fetchall.return_value = [
        ("Jan", 300),
        ("Feb", 400),
    ]
    
    producao = Producao(mock_banco)
    resultado = producao.grafico_qnt_prod_mes()

    # Verificar se a consulta foi feita corretamente
    mock_banco.cursor.execute.assert_called_once_with('''SELECT 
                            FORMAT(Data_Inicio, 'MMM') AS Mes, 
                            SUM(Quantidade) AS Total_Quantidade
                        FROM 
                            Producao
                        GROUP BY 
                            FORMAT(Data_Inicio, 'MMM'), DATEPART(MONTH, Data_Inicio)
                        ORDER BY 
                            DATEPART(MONTH, Data_Inicio);''')
    
    # Verificar o retorno
    assert len(resultado) == 2  # Esperamos 2 meses no gráfico
    assert resultado[0][0] == "Jan"  # O mês deve ser "Jan"
    assert resultado[1][1] == 400  # O total de quantidade no mês "Feb" deve ser 400
