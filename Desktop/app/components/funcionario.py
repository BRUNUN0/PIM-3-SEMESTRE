from app.components.gerenciamento_banco import GerenciamentoBanco
import hashlib
from hashlib import sha256
from datetime import datetime

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
                            f.Nome as nome,
                            f.CPF as cpf,
                            f.Sexo as sexo,
                            c.Cargo as cargo,
                            f.Senha as senha,
                            FORMAT(f.Nascimento, 'dd-MM-yyyy') as nascimento,
                            f.Email as email,
                            f.Setor as setor,
                            FORMAT(hc.Data_Inicio, 'dd-MM-yyyy') as data_inicio
                        FROM
                            Funcionario f
                        INNER JOIN Cargo c ON f.fk_id_cargo = c.id_cargo
                        INNER JOIN Historico_Cargo hc ON f.id_funcionario = hc.fk_id_funcionario
                            AND hc.Data_Inicio = (
                                SELECT MAX(Data_Inicio)
                                FROM Historico_Cargo
                                WHERE fk_id_funcionario = f.id_funcionario
                            )
                        WHERE 
                            f.id_funcionario = {id_funcionario};'''
            self.banco.cursor.execute(query)
            detalhes_funcionario = self.banco.cursor.fetchone()
            
            return detalhes_funcionario
        except Exception as e:
            print(f"Erro ao obter detalhes do funcionario: {e}")
            self.banco.fechar_conexao()
            return None

    def atualizar_funcionario(self, dados_atualizados, id_funcionario):
        print(dados_atualizados)
        try:
            self.banco.conectar()

            # Garantir que a data esteja no formato YYYY-MM-DD antes de salvar
            if "Nascimento" in dados_atualizados and dados_atualizados["Nascimento"]:
                # Converte a data para o formato YYYY-MM-DD se estiver no formato DD-MM-YYYY
                dados_atualizados["Nascimento"] = datetime.strptime(dados_atualizados["Nascimento"], "%d-%m-%Y").strftime("%Y-%m-%d")

            # Se a senha não foi passada (campo vazio ou ausente), manter a senha existente
            if "Senha" not in dados_atualizados or not dados_atualizados["Senha"]:
                # Buscar a senha atual no banco de dados
                query_busca_senha = '''SELECT Senha FROM Funcionario WHERE id_funcionario = ?'''
                self.banco.cursor.execute(query_busca_senha, (id_funcionario,))
                senha_atual = self.banco.cursor.fetchone()
                if senha_atual:
                    # Atribui a senha atual ao dicionário
                    dados_atualizados["Senha"] = senha_atual[0]
            print(dados_atualizados)
            query = '''UPDATE Funcionario SET Nome = ?, Sexo = ?, Senha = ?, Nascimento = ?, Email = ?, Setor = ? WHERE id_funcionario = ?'''
            parametros = (
                dados_atualizados["Nome"],
                dados_atualizados["Sexo"],
                dados_atualizados["Senha"],  # A senha agora estará garantida, seja a nova ou a atual
                dados_atualizados["Nascimento"],  # A data já estará no formato correto
                dados_atualizados["Email"],
                dados_atualizados["Setor"],
                id_funcionario
            )
            
            self.banco.cursor.execute(query, parametros)
            self.banco.conn.commit()
            return True
        except Exception as e:
            print(f"Erro ao atualizar dados do fornecedor {e}")
            self.banco.fechar_conexao()
            return str(e)

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
    
    def verifica_rg_senha(self, rg, senha_atual):
        try:
            self.banco.conectar()
            query = ''' SELECT
                            f.RG,
                            f.Senha
                        FROM
                            Funcionario f
                        WHERE
                            f.RG = ?'''
            self.banco.cursor.execute(query, (rg))
            dados = self.banco.cursor.fetchone()
            if dados:
                senha_hash = dados[0]  # A senha armazenada no banco
                # Verifica se a senha atual corresponde ao que está no banco
                if senha_hash == self.hash_password(senha_atual):
                    return True
                else:
                    return False
            return False

        except Exception as e:
            print(f"Erro ao verificar RG e senha: {e}")
            return False

        finally:
            self.banco.fechar_conexao()

    def atualizar_senha(self, rg, nova_senha_hash):
        try:
            self.banco.conectar()
            query = ''' UPDATE Funcionario
                        SET Senha = ?
                        WHERE RG = ?'''
            self.banco.cursor.execute(query, (nova_senha_hash, rg))
            self.banco.cursor.commit()
            # Verifica se alguma linha foi afetada
            if self.banco.cursor.rowcount > 0:
                print(f"Senha do funcionário com RG {rg} atualizada com sucesso.")
                return True
            else:
                print(f"Nenhum funcionário encontrado com o RG {rg}.")
                return False

        except Exception as e:
            print(f"Erro ao atualizar a senha: {e}")
            return False

        finally:
            self.banco.fechar_conexao()