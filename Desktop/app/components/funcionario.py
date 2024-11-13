from app.components.classes import GerenciamentoBanco

class Funcionario:   
    # def __init__(self, id_funcionario, nome, cpf, sexo, fk_id_cargo, senha, nascimento, email, setor, fk_data_inicio, gerenciamento_banco:GerenciamentoBanco):
    def __init__(self, gerenciamento_banco: GerenciamentoBanco):
        self.banco = gerenciamento_banco
        # self.id_funcionario = id_funcionario
        # self.nome = nome
        # self.cpf = cpf
        # self.sexo = sexo
        # self.fk_id_cargo = fk_id_cargo
        # self.senha = senha
        # self.nascimento = nascimento
        # self.email = email
        # self.setor = setor
        # self.fk_data_inicio = fk_data_inicio

    def __str__(self):
        return f"Funcionário: {self.nome}, ID: {self.id_funcionario}"
    
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

    def atualizar_funcionario(self, dados_atualizados, id_funcionario):
        print(dados_atualizados)
        try:
            self.banco.conectar()
            query = f'''UPDATE Funcionario SET  Nome = ?, Sexo = ?, Senha = ?, Nascimento = ?, Email = ?, Setor = ? WHERE id_funcionario = ?'''
            parametros = (
            dados_atualizados["Nome"],
            dados_atualizados["Sexo"],
            dados_atualizados["Senha"],
            dados_atualizados["Nascimento"],
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
            print(cpf)
            self.banco.cursor.execute( '''SELECT Senha, CPF, id_funcionario FROM Funcionario WHERE cpf = ?''', (cpf,))
            dados_login = self.banco.cursor.fetchone()
            print(dados_login)
            return dados_login
        except Exception as e:
            print(f"Erro ao obter login")
        finally:
            self.banco.fechar_conexao()
            return None