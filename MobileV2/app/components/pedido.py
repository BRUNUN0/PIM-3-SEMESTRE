from app.components.gerenciamento_banco import GerenciamentoBanco

class Pedido:
    def __init__(self, gerenciamento_banco:GerenciamentoBanco):
        # Armazena a instância de GerenciamentoBanco
        self.banco = gerenciamento_banco

    def contar_pedidos_abertos(self):
        try:
            self.banco.conectar()
            query = '''SELECT 
                            COUNT(*) AS Total_Pedidos_Abertos 
                        FROM 
                            Pedido 
                        WHERE 
                            Status = 'Em andamento';'''
            self.banco.cursor.execute(query)
            n_pedidos_abertos = self.banco.cursor.fetchone()
            return n_pedidos_abertos[0]
        except Exception as e:
            print(f"Erro ao obter soma de pedidos abertos: {e}")
            self.banco.fechar_conexao()
            return None
        