from app.components.classes import GerenciamentoBanco

class Pedido:
    def __init__(self, gerenciamento_banco:GerenciamentoBanco):
        # Armazena a instância de GerenciamentoBanco
        self.gerenciamento_banco = gerenciamento_banco

    def obter_pedidos_abertos(self):
        try:
            # Chama o método conectar na instância da classe GerenciamentoBanco
            self.gerenciamento_banco.conectar()
            
            # Define a consulta SQL
            query = '''SELECT
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
            
            # Executa a consulta
            self.gerenciamento_banco.cursor.execute(query)
            
            # Obtém os resultados
            pedidos = self.gerenciamento_banco.cursor.fetchall()
            return pedidos
        except Exception as e:
            print(f"Erro ao obter pedidos: {e}")
            return None
        finally:
            # Fecha a conexão com o banco
            self.gerenciamento_banco.fechar_conexao()

    def obter_pedidos_finalizados(self):
        try:
            self.gerenciamento_banco.conectar()
            query = '''SELECT
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
            self.gerenciamento_banco.cursor.execute(query)
            pedidos = self.gerenciamento_banco.cursor.fetchall()
            return pedidos
        except Exception as e:
            print(f"Erro ao obter pedidos: {e}")
            self.gerenciamento_banco.fechar_conexao()
            return None
        
    def obter_detalhes_pedido(self, id_pedido):
        try:
            self.gerenciamento_banco.conectar()
            query = '''SELECT
                            pe.id_pedido,
                            c.Nome AS Nome_Cliente,
                            pe.Data_Pedido,
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
            self.gerenciamento_banco.cursor.execute(query,(id_pedido))
            detalhes_pedido = self.gerenciamento_banco.cursor.fetchone()
            return detalhes_pedido
        except Exception as e:
            print(f"Erro ao obter detalhes do pedido: {e}")
            self.gerenciamento_banco.fechar_conexao()
            return None