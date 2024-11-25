from app.components.gerenciamento_banco import GerenciamentoBanco

class Producao:
    def __init__(self, gerenciamento_banco:GerenciamentoBanco):
        self.banco = gerenciamento_banco

    def obter_producao(self):
        try:
            self.banco.conectar()
            query = '''SELECT
                        p.id_plantio,
                        p.Plantio,
                        p.Nome,
                        p.Quantidade,
                        mp.URL
                    FROM Producao p
                    JOIN Materia_Prima mp ON p.fk_id_materia = mp.id_materia
                    WHERE p.Data_Fim IS NULL;'''
            self.banco.cursor.execute(query)
            producao = self.banco.cursor.fetchall()
            return producao
        except Exception as e:
            print(f"Erro ao obter producao: {e}")
            self.banco.fechar_conexao()
            return []

    def obter_detalhes_plantio(self, id_plantio):
        try:
            self.banco.conectar()
            query = f'''
                SELECT
                    id_plantio,
                    Plantio,
                    FORMAT(Data_Inicio, 'dd/MM/yyyy'),
                    Nome,
                    Quantidade
                FROM 
                    Producao
                WHERE id_plantio = {id_plantio}
            '''
            self.banco.cursor.execute(query)
            detalhes = self.banco.cursor.fetchone()
            return detalhes
        except Exception as e:
            print(f"Erro ao obter fornecedores: {e}")
            self.banco.fechar_conexao()
            return None
        
    def grafico_qnt_prod_mes(self):
        try:
            self.banco.conectar()
            query = '''SELECT 
                            FORMAT(Data_Inicio, 'MMM') AS Mes, 
                            SUM(Quantidade) AS Total_Quantidade
                        FROM 
                            Producao
                        GROUP BY 
                            FORMAT(Data_Inicio, 'MMM'), DATEPART(MONTH, Data_Inicio)
                        ORDER BY 
                            DATEPART(MONTH, Data_Inicio);'''
            self.banco.cursor.execute(query)
            grafico = self.banco.cursor.fetchall()
            return grafico
        except Exception as e:
            print(f"Erro ao obter grafico")
            self.banco.fechar_conexao()
            return []