import pydoc as dbc
from app.components.classes import GerenciamentoBanco as gbd
from app.components.funcionario import Funcionario as f
from hashlib import sha256

class Validacao:
    def __init__(self):
        self.gbd = gbd()  # Instancia o GerenciamentoBanco

    def valid_Login(self, cpf, senha):

        senha_cripto = sha256(senha.encode()).digest()

        dados = self.gbd.obter_funcionario_login(cpf)  # Agora usa a instância do banco
        if dados:  # Verifica se dados foram encontrados
            __senha = dados[0]
            print(__senha)
            __cpf = dados[1]
            _id = dados[2]

            if senha_cripto == __senha and cpf == __cpf:
                dados_funcionario = self.gbd.obter_detalhes_funcionario(_id)
                if dados_funcionario:
                    nome = dados_funcionario[1]
                    sexo = dados_funcionario[3]
                    fk_id_cargo = dados_funcionario[4]
                    nascimento = dados_funcionario[6]
                    email = dados_funcionario[7]
                    setor = dados_funcionario[8]
                    fk_data_inicio = dados_funcionario[9]
                    # Crie uma instância de Funcionario ou qualquer outra classe necessária
                    funcionario = Funcionario(_id, nome, cpf, sexo, fk_id_cargo, senha, nascimento, email, setor, fk_data_inicio)
                    return True
        return False  # Caso o login não seja bem-sucedido

class Funcionario:
    def __init__(self, id_funcionario, nome, cpf, sexo, fk_id_cargo, senha, nascimento, email, setor, fk_data_inicio):
        self.id_funcionario = id_funcionario
        self.nome = nome
        self.cpf = cpf
        self.sexo = sexo
        self.fk_id_cargo = fk_id_cargo
        self.senha = senha
        self.nascimento = nascimento
        self.email = email
        self.setor = setor
        self.fk_data_inicio = fk_data_inicio