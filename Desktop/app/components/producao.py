from app.components.classes import GerenciamentoBanco

class Producao:
    def __init__(self, gerenciamento_banco:GerenciamentoBanco):
        self.gerenciamento_banco = gerenciamento_banco

    def obter_producao(self):
        try:
            self.gerenciamento_banco.conectar()
            query = '''SELECT
                        p.id_plantio,
                        p.Plantio,
                        p.Nome,
                        p.Quantidade,
                        mp.URL
                    FROM Producao p
                    JOIN Materia_Prima mp ON p.fk_id_materia = mp.id_materia
                    WHERE p.Data_Fim IS NULL;'''
            self.gerenciamento_banco.cursor.execute(query)
            producao = self.gerenciamento_banco.cursor.fetchall()
            return producao
        except Exception as e:
            print(f"Erro ao obter producao: {e}")
            self.gerenciamento_banco.fechar_conexao()
            return []

    def obter_detalhes_plantio(self, id_plantio):
        try:
            self.gerenciamento_banco.conectar()
            query = f'''
                SELECT
                    id_plantio,
                    Plantio,
                    Data_Inicio,
                    Nome,
                    Quantidade
                FROM 
                    Producao
                WHERE id_plantio = {id_plantio}
            '''
            self.gerenciamento_banco.cursor.execute(query)
            detalhes = self.gerenciamento_banco.cursor.fetchone()
            return detalhes
        except Exception as e:
            print(f"Erro ao obter fornecedores: {e}")
            self.gerenciamento_banco.fechar_conexao()
            return None