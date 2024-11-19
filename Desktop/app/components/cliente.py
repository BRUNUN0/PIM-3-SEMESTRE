from app.components.gerenciamento_banco import GerenciamentoBanco

class Cliente:
    def __init__(self, gerenciamento_banco: GerenciamentoBanco):
        self.banco = gerenciamento_banco

    def obter_clientes(self):
        try:
            self.banco.conectar()
            query = '''SELECT id_cliente, Nome, CNPJ FROM Cliente'''
            self.banco.cursor.execute(query)
            clientes = self.banco.cursor.fetchall()
            return clientes
        except Exception as e:
            print(f"Erro ao obter clientes: {e}")
            self.banco.fechar_conexao()
            return None

    def obter_detalhes_clientes(self, id_cliente):
        try:
            # Obter os detalhes do cliente
            self.banco.conectar()
            query = f'''SELECT * from Cliente WHERE id_cliente = {id_cliente}'''
            self.banco.cursor.execute(query)
            detalhes_cliente = self.banco.cursor.fetchone()
            return detalhes_cliente
        except Exception as e:
            print(f"Erro ao obter detalhes do cliente: {e}")
            return None
        finally:
            self.banco.fechar_conexao()

    def atualizar_cliente(self, dados_atualizados, id_cliente):
        try:
            self.banco.conectar()
            query = '''UPDATE Cliente SET  Nome_Fantasia = ?, Email = ?, Rua = ?, Numero = ?, Bairro = ?, CEP = ?, Cidade = ?, Estado = ? WHERE id_cliente = ?'''
            parametros = (
            dados_atualizados["Nome Fantasia"],
            dados_atualizados["Email"],
            dados_atualizados["Rua"],
            dados_atualizados["Número"],
            dados_atualizados["Bairro"],
            dados_atualizados["CEP"],
            dados_atualizados["Cidade"],
            dados_atualizados["Estado"],
            id_cliente  # Aqui é onde o ID do Cliente é passado
        )
            self.banco.cursor.execute(query, parametros)
            self.banco.conn.commit()
        except Exception as e:
            print(f"Erro ao atualizar dados do Cliente {e}")
            self.banco.fechar_conexao()
            return str(e)