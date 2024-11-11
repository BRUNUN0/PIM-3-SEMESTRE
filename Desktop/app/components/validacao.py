import pydoc as dbc
from app.components.classes import GerenciamentoBanco as gbd
from app.components.funcionario import Funcionario as f

class Validacao:


    def valid_Login(self, cpf, senha):
        dados = gbd.obter_funcionario_login(cpf) # Recebe os seguintes dados na seguinte ordem === Senha | CPF | ID
        
        # quando utilizado dois anderlaine o escopo de utilização é fechado apenas para esta funcão.
        __senha = dados[0]
        __cpf = dados[1]
        _id = dados[2]

        if(senha == __senha and cpf == __cpf):# id, nome, cpf, sexo, cargo, senha, nascimento, email, setor, data_inicio
           dados_funcionario =  gbd.obter_detalhes_funcionario(_id)
        if(dados_funcionario):
            nome = dados_funcionario[1]
            sexo = dados_funcionario[3]
            fk_id_cargo = dados_funcionario[4]
            nascimento = dados_funcionario[6]
            email = dados_funcionario[7]
            setor = dados_funcionario[8]
            fk_data_inicio = dados_funcionario[9]
            f.__init__(_id, nome, cpf, sexo, fk_id_cargo, senha, nascimento, email, setor, fk_data_inicio)
            return True
        else: print("Erro ")


            
