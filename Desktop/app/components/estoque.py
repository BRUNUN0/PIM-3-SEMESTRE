from app.components.classes import GerenciamentoBanco

class Estoque:
    def __init__(self, gerenciamento_banco:GerenciamentoBanco):
        self.banco = gerenciamento_banco

    def obter_produtos(self):
        try:
            self.banco.conectar()
            query = '''SELECT
                        p.id_produto,
                        p.Produto,
                        p.Quantidade,
                        p.Previsao
                    FROM Produto p'''
            self.banco.cursor.execute(query)
            produtos = self.banco.cursor.fetchall()
            return produtos
        except Exception as e:
            print(f"Erro ao obter produtos: {e}")
            self.banco.fechar_conexao()
            return None

    def obter_materia_prima(self):
        try:
            self.banco.conectar()
            query = '''SELECT
                        mp.id_materia,
                        mp.Nome,
                        mp.Quantidade,
                        mp.URL
                    FROM Materia_Prima mp'''
            self.banco.cursor.execute(query)
            materias_primas = self.banco.cursor.fetchall()
            return materias_primas
        except Exception as e:
            print(f"Erro ao obter materias primas: {e}")
            self.banco.fechar_conexao()
            return None

    # Detalhes Historico de Compra por Matéria Prima
    def obter_detalhes_materia_prima(self, id_materia):
        try:
            self.banco.conectar()
            query = f'''SELECT
                            c.id_compra AS id,
                            f.Nome_Fantasia AS fornecedor,
                            f.CNPJ AS cnpj,
                            mp.Nome AS nome,
                            mp.Quantidade AS quantidade,
                            c.Data_compra AS data_compra,
                            mp.URL AS url
                        FROM
                            Materia_Prima mp
                        INNER JOIN Compra c ON c.id_compra = mp.id_materia
                        INNER JOIN Fornecedor f ON f.id_fornecedor = mp.id_materia
                        WHERE
                            mp.id_materia = {id_materia}'''
            self.banco.cursor.execute(query)
            detalhes_materia_prima = self.banco.cursor.fetchone()
            print(detalhes_materia_prima)
            return detalhes_materia_prima()
        except Exception as e:
            print(f"Erro ao obter detalhes da materia prima: {e}")
            self.banco.fechar_conexao()
            return None