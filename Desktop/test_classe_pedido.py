import pytest
from unittest.mock import Mock
from app.components.gerenciamento_banco import GerenciamentoBanco
from app.components.pedido import Pedido

# Mockando a classe GerenciamentoBanco
@pytest.fixture
def mock_banco():
    banco = Mock(spec=GerenciamentoBanco)
    banco.cursor = Mock()
    banco.conectar = Mock()
    banco.fechar_conexao = Mock()
    return banco

def test_obter_pedidos_abertos(mock_banco):
    # Configurando o retorno esperado para o fetchall
    mock_banco.cursor.fetchall.return_value = [
        (1, 'Cliente 1', 'Produto A', 10),
        (2, 'Cliente 2', 'Produto B', 5)
    ]
    
    pedido = Pedido(mock_banco)
    
    # Chamando o método a ser testado
    pedidos = pedido.obter_pedidos_abertos()
    
    # Verificando se a consulta foi executada corretamente
    query_esperada = '''SELECT
                        pe.id_pedido,
                        c.Nome AS Nome_Cliente,
                        pd.Produto,
                        i.Quantidade
                    FROM
                        Pedido pe
                    INNER JOIN Item_Pedido i ON pe.id_pedido = i.fk_id_pedido
                    INNER JOIN Produto pd ON pd.id_produto = i.fk_id_produto
                    INNER JOIN Cliente c ON pe.fk_id_cliente = c.id_cliente
                    WHERE
                        pe.Status = 'Em andamento';'''
    
    mock_banco.cursor.execute.assert_called_once_with(query_esperada)
    
    # Verificando se os pedidos retornados são os esperados
    assert len(pedidos) == 2
    assert pedidos[0] == (1, 'Cliente 1', 'Produto A', 10)
    assert pedidos[1] == (2, 'Cliente 2', 'Produto B', 5)

def test_obter_pedidos_finalizados(mock_banco):
    # Configurando o retorno esperado para o fetchall
    mock_banco.cursor.fetchall.return_value = [
        (3, 'Cliente 3', 'Produto C', 2)
    ]
    
    pedido = Pedido(mock_banco)
    
    # Chamando o método a ser testado
    pedidos = pedido.obter_pedidos_finalizados()
    
    # Verificando se a consulta foi executada corretamente
    query_esperada = '''SELECT
                        pe.id_pedido,
                        c.Nome AS Nome_Cliente,
                        pd.Produto,
                        i.Quantidade
                    FROM
                        Pedido pe
                    INNER JOIN Item_Pedido i ON pe.id_pedido = i.fk_id_pedido
                    INNER JOIN Produto pd ON pd.id_produto = i.fk_id_produto
                    INNER JOIN Cliente c ON pe.fk_id_cliente = c.id_cliente
                    WHERE
                        pe.Status = 'Finalizado';'''
    
    mock_banco.cursor.execute.assert_called_once_with(query_esperada)
    
    # Verificando se os pedidos retornados são os esperados
    assert len(pedidos) == 1
    assert pedidos[0] == (3, 'Cliente 3', 'Produto C', 2)

def test_obter_detalhes_pedido(mock_banco):
    # Configurando o retorno esperado para o fetchone
    mock_banco.cursor.fetchone.return_value = (1, 'Hidroponia Center', '25/11/2022', 'Alface', 20, 45, 'Em andamento')
    
    pedido = Pedido(mock_banco)
    
    # Chamando o método a ser testado
    detalhes = pedido.obter_detalhes_pedido(1)
    
    # Verificando se a consulta foi executada corretamente
    query_esperada = '''SELECT
                            pe.id_pedido,
                            c.Nome AS Nome_Cliente,
                            FORMAT(pe.Data_Pedido, 'dd/MM/yyyy'),
                            pd.Produto,
                            i.Quantidade AS Quantidade_Produto,
                            pd.Previsao AS Previsao_Entrega,
                            pe.Status AS Status_Pedido
                        FROM
                            Pedido pe
                        INNER JOIN Cliente c ON pe.fk_id_cliente = c.id_cliente
                        INNER JOIN Item_Pedido i ON pe.id_pedido = i.fk_id_pedido
                        INNER JOIN Produto pd ON pd.id_produto = i.fk_id_produto
                        WHERE
                            pe.id_pedido = ?;'''
    
    mock_banco.cursor.execute.assert_called_once_with(query_esperada, (1))
    
    # Verificando se os detalhes do pedido estão corretos
    assert detalhes == (1, 'Hidroponia Center', '25/11/2022', 'Alface', 20, 45, 'Em andamento')

def test_contar_pedidos_abertos(mock_banco):
    # Configurando o retorno esperado para o fetchone
    mock_banco.cursor.fetchone.return_value = (5,)  # 5 pedidos abertos
    
    pedido = Pedido(mock_banco)
    
    # Chamando o método a ser testado
    total_pedidos_abertos = pedido.contar_pedidos_abertos()
    
    # Verificando se a consulta foi executada corretamente
    query_esperada = '''SELECT 
                            COUNT(*) AS Total_Pedidos_Abertos 
                        FROM 
                            Pedido 
                        WHERE 
                            Status = 'Em andamento';'''
    
    mock_banco.cursor.execute.assert_called_once_with(query_esperada)
    
    # Verificando se o número de pedidos abertos está correto
    assert total_pedidos_abertos == (5,)

