from app.components.classes import GerenciamentoBanco

class Fornecedor:
    def __init__(self, gerenciamento_banco: GerenciamentoBanco):
        self.banco = gerenciamento_banco

    def obter_fornecedores(self):
        try:
            # Obtém os dados dos fornecedores
            self.banco.conectar()
            query = '''SELECT id_fornecedor, Nome_Fantasia, CNPJ FROM Fornecedor'''
            self.banco.cursor.execute(query)
            fornecedores = self.banco.cursor.fetchall()
            return fornecedores
        except Exception as e:
            print(f"Erro ao obter fornecedores: {e}")
            self.banco.fechar_conexao()
            return None

    def obter_detalhes_fornecedores(self, id_fornecedor):
        try:
            # Obter os detalhes do fornecedor
            self.banco.conectar()
            query = f'''SELECT * from Fornecedor WHERE id_fornecedor = {id_fornecedor}'''
            self.banco.cursor.execute(query)
            detalhes_fornecedor = self.banco.cursor.fetchone()
            return detalhes_fornecedor
        except Exception as e:
            print(f"Erro ao obter detalhes do fornecedor: {e}")
            self.banco.fechar_conexao()
            return None

    def atualizar_fornecedor(self, dados_atualizados, id_fornecedor):
        try:
            self.banco.conectar()
            query = '''UPDATE Fornecedor SET Nome_Fantasia = ?, Email = ?, Telefone = ?, Rua = ?, Numero = ?, Bairro = ?, CEP = ?, Cidade = ?, Estado = ? WHERE id_fornecedor = ?'''
            parametros = (
            dados_atualizados["Nome Fantasia"],
            dados_atualizados["Email"],
            dados_atualizados["Telefone"],
            dados_atualizados["Rua"],
            dados_atualizados["Número"],
            dados_atualizados["Bairro"],
            dados_atualizados["CEP"],
            dados_atualizados["Cidade"],
            dados_atualizados["Estado"],
            id_fornecedor  # Aqui é onde o ID do fornecedor é passado
            )
            self.banco.cursor.execute(query, parametros)
            self.banco.conn.commit()
            return True
        except Exception as e:
            print(f"Erro ao atualizar dados do fornecedor: {e}")
            self.banco.fechar_conexao()
            return str(e)

