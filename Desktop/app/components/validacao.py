
import pydoc as dbc 
import flet as ft
from app.components.gerenciamento_banco import GerenciamentoBanco as gbd
from app.components.funcionario import Funcionario
from hashlib import sha256



class Validacao:
    def __init__(self):
        pass

    def valid_Login(self, cpf, senha):
        banco = gbd()
        dado = Funcionario(banco)
        # fornecedores = banco_fornecedores.obter_fornecedores()

        # Recebe a senha inserida 
        senha_cripto = sha256(senha.encode('utf-8')).hexdigest()
        print(senha_cripto)

        dados = dado.obter_funcionario_login(cpf)  # Agora usa a instância do banco
        print(dados)


        if dados:  # Verifica se dados foram encontrados
            __senha, __cpf, _id = dados[0], dados[1], dados[2]

            if senha_cripto == __senha and cpf == __cpf:
                dados_funcionario = dado.obter_detalhes_funcionario(_id)
                print(dados_funcionario)
                return True
        return False  # Caso o login não seja bem-sucedido

    

