import pydoc as dbc
from app.components.classes import GerenciamentoBanco as gbd
from app.components.funcionario import Funcionario
from hashlib import sha256

class Validacao:
    def __init__(self):
        pass

    def valid_Login(self, cpf, senha):
        banco = gbd()
        dado = Funcionario(banco)
        # fornecedores = banco_fornecedores.obter_fornecedores()

        senha_cripto = sha256(senha.encode('utf-8')).hexdigest()

        dados = dado.obter_funcionario_login(cpf)  # Agora usa a instância do banco
        print(dados)
        if dados:  # Verifica se dados foram encontrados
            __senha, __cpf, _id = dados[0], dados[1], dados[2]
            # print(__senha)
            # __cpf = dados[1]
            # _id = dados[2]

            if senha_cripto == __senha and cpf == __cpf:
                dados_funcionario = dado.obter_detalhes_funcionario(_id)
                print(dados_funcionario)
                # if dados_funcionario:
                #     id_funcionario = dados_funcionario[0]
                #     nome = dados_funcionario[1]
                #     sexo = dados_funcionario[3]
                #     fk_id_cargo = dados_funcionario[4]
                #     nascimento = dados_funcionario[6]
                #     email = dados_funcionario[7]
                #     setor = dados_funcionario[8]
                #     fk_data_inicio = dados_funcionario[9]
            #         # Crie uma instância de Funcionario ou qualquer outra classe necessária
            #         funcionario = Funcionario(
            #             id_funcionario=id_funcionario,
            #             nome=nome,
            #             cpf=__cpf,
            #             sexo=sexo,
            #             fk_id_cargo=fk_id_cargo,
            #             nascimento=nascimento,
            #             email=email,
            #             setor=setor,
            #             fk_data_inicio=fk_data_inicio
            #         )

        #         return True
        # return False  # Caso o login não seja bem-sucedido
    
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
