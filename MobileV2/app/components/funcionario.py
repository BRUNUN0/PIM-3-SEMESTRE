from app.components.gerenciamento_banco import GerenciamentoBanco
from hashlib import sha256

class Funcionario:   
    def __init__(self, gerenciamento_banco: GerenciamentoBanco):
        self.banco = gerenciamento_banco
        self.sessao = {}

    def salvar_sessao(self, usuario):
        # Salva as informações do usuário na sessão.
        print(f"Antes de salvar o usuário no salvar_sessao: {usuario}")
        self.sessao['usuario_logado'] = usuario
        print(f"Sessão salva: {self.sessao}")
        print(f"Usuario {usuario['nome']} logado com sucesso.")
        # print(f'Usuario {usuario['nome']} logado com sucesso. Sessão salva: {self.sessao}')

    def obter_sessao(self):
        # Retorna as informações do usuário logado.
        # return self.sessao['usuario_logado']
        # return self.sessao.get('usuario_logado')
        print(f"Obtendo sessão: {self.sessao}")
        return self.sessao.get('usuario_logado')
    
    def limpar_sessao(self):
        self.sessao.clear()
        print('Usuario deslogado com sucesso')
    
    def obter_funcionarios(self):
        try:
            self.banco.conectar()
            query = '''SELECT 
                        f.id_funcionario AS id,
                        f.nome AS nome,
                        c.cargo AS cargo
                    FROM 
                        Funcionario f
                    INNER JOIN Cargo c ON f.fk_id_cargo = c.id_cargo;'''
            self.banco.cursor.execute(query)
            clientes = self.banco.cursor.fetchall()
            return clientes
        except Exception as e:
            print(f"Erro ao obter clientes: {e}")
            self.banco.fechar_conexao()
            return None
        
    def obter_detalhes_funcionario(self, id_funcionario):
        try:
            # Obter detalhes do funcionario
            self.banco.conectar()
            query = f'''SELECT
                            f.id_funcionario as id,
                            f.nome as nome,
                            f.CPF as cpf,
                            f.Sexo as sexo,
                            c.cargo as cargo,
                            f.senha as senha,
                            f.Nascimento as nascimento,
                            f.Email as email,
                            f.Setor as setor,
                            hc.Data_Inicio as data_inicio
                            FROM
                        Funcionario f
                        INNER JOIN Cargo c ON c.Cargo = c.Cargo
                        INNER JOIN Historico_Cargo hc ON hc.Data_Inicio = hc.Data_Inicio
                        WHERE id_funcionario = {id_funcionario}'''
            self.banco.cursor.execute(query)
            detalhes_funcionario = self.banco.cursor.fetchone()
            
            return detalhes_funcionario
        except Exception as e:
            print(f"Erro ao obter detalhes do funcionario: {e}")
            self.banco.fechar_conexao()
            return None


    def obter_funcionario_login(self, cpf):
        try:
            self.banco.conectar()
            query = '''SELECT Senha, CPF, id_funcionario, Nome, Cargo 
                    FROM Funcionario 
                    INNER JOIN Cargo ON Funcionario.fk_id_cargo = Cargo.id_cargo
                    WHERE CPF = ?'''
            self.banco.cursor.execute(query, (cpf,))
            dados_login = self.banco.cursor.fetchone()

            if not dados_login:
                print("Usuário não encontrado.")
                return None

            return dados_login  # Retorna os dados diretamente para validação posterior

        except Exception as e:
            print(f"Erro ao obter login: {e}")
        finally:
            self.banco.fechar_conexao()

        return None