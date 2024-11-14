import pydoc as dbc
import flet as ft
from app.components.classes import GerenciamentoBanco as gbd
from app.components.funcionario import Funcionario as f
from hashlib import sha256


class Validacao:
    def __init__(self):
        self.gbd = gbd()  # Instancia o GerenciamentoBanco

    print("Ta vindo pra ca primeiro essa bosta")
    def valid_Login(self, cpf, senha):

        # Recebe a senha inserida 
        senha_cripto = sha256(senha.encode('utf-8')).hexdigest()
        print(senha_cripto)

        dados = gbd.obter_funcionario_login(cpf)  # Agora usa a instância do banco
        if dados:  # Verifica se dados foram encontrados
            __senha = dados[0]
            print(__senha)
            __cpf = dados[1]
            _id = dados[2]

            if senha_cripto == __senha and cpf == __cpf:
                r = True
                return r
        else:
            print("Usuario não encontrato")


    
    def validar_cpf(cpf):
        """Valida um CPF de 11 dígitos.
        Args:
            cpf (str): CPF a ser validado, sem formatação.

        Returns:
            bool: True se o CPF for válido, False caso contrário.
        """

        # Remove caracteres não numéricos
        cpf = ''.join(c for c in cpf if c.isdigit())

        # Verifica se o CPF tem 11 dígitos
        if len(cpf) != 11:
            return False

        # Primeira parte da validação
        soma = 0
        multiplicador = 10
        for i in range(9):
            soma += int(cpf[i]) * multiplicador
            multiplicador -= 1
        resto = soma * 11 % 10
        if resto != int(cpf[9]):
            return False

        # Segunda parte da validação
        soma = 0
        multiplicador = 11
        for i in range(10):
            soma += int(cpf[i]) * multiplicador
            multiplicador -= 1
        resto = soma * 11 % 10
        if resto != int(cpf[10]):
            return False

        return True

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

