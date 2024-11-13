from app.components.classes import GerenciamentoBanco

class Atividade:
    def __init__(self, gerenciamento_banco:GerenciamentoBanco):
        self.banco = gerenciamento_banco

    def obter_atividades(self):
        try:
            self.banco.conectar()
            query = '''SELECT 
                        a.id_atividade,
                        p.Plantio AS nome_plantio,
                        a.Data
                    FROM 
                        Atividade a
                    INNER JOIN 
                        Funcionario f ON a.fk_id_funcionario = f.id_funcionario
                    INNER JOIN 
                        Producao p ON a.fk_id_Plantio = p.id_plantio;'''
            self.banco.cursor.execute(query)
            atividades = self.banco.cursor.fetchall()
            return atividades
        except Exception as e:
            print(f"Erro ao obter atividades: {e}")
            self.banco.fechar_conexao()
            return None
        
    def obter_detalhes_atividade(self, id_atividade):
        try:
            self.banco.conectar()
            query = f'''SELECT 
                        a.id_atividade,
                        f.nome AS nome_funcionario,
                        p.Plantio AS nome_plantio,
                        a.Descricao,
                        a.Prioridade,
                        a.Duracao,
                        p.Fase_Atual
                    FROM 
                        Atividade a
                    INNER JOIN 
                        Funcionario f ON a.fk_id_funcionario = f.id_funcionario
                    INNER JOIN 
                        Producao p ON a.fk_id_Plantio = p.id_plantio
                    WHERE id_atividade = {id_atividade}'''
            self.banco.cursor.execute(query)
            detalhes_atividade = self.banco.cursor.fetchone()
            return detalhes_atividade
        except Exception as e:
            print(f"Erro ao obter detalhes da atividade: {e}")
            self.banco.fechar_conexao()
            return None