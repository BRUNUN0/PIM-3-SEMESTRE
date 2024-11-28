import pydoc as dbc 
import flet as ft
from app.components.gerenciamento_banco import GerenciamentoBanco as gbd
from app.components.funcionario import Funcionario
from hashlib import sha256


class Validacao:
    def __init__(self):
        pass


    def valid_Login(self, cpf, senha):
        if not self.validar_cpf(cpf):
            print('CPF inválido.')
            return False

        # Criar uma instância mockada do banco e do funcionário
        banco = gbd()  # Banco real pode ser necessário ou mockar o banco aqui
        funcionario = Funcionario(banco)

        # Recebe a senha inserida
        senha_cripto = sha256(senha.encode('utf-8')).hexdigest()
        print(f'Senha criptografada: {senha_cripto}')

        # Obtém os dados do banco
        dados = funcionario.obter_funcionario_login(cpf)  # Usa o mock para retornar os dados
        print(dados)

        if dados:  # Verifica se dados foram encontrados
            senha_db, cpf_db, id_funcionario, nome, cargo = dados

            if senha_cripto == senha_db and cpf == cpf_db:
                usuario = {
                    "id": id_funcionario,
                    "cpf": cpf_db,
                    "nome": nome,
                    "cargo": cargo,
                }
                print(f'Antes de salvar o usuario no salvar sessão: {usuario}')
                funcionario.salvar_sessao(usuario)  # Aqui é onde o mock precisa ser verificado
                return True
        
        print("Credenciais inválidas")
        return False  # Caso o login não seja bem-sucedido

    
    def verificar_usuario_logado(self, funcionario: Funcionario, page: ft.Page):
        usuario = funcionario.obter_sessao()
        print(f"Usuario logado: {usuario}")
        if not usuario or not usuario.get('nome'):
            page.go('/login')
            return False
        return True
        
    def Logout(page: ft.Page, funcionario: Funcionario):
        """
        Realiza o logout do usuário.
        """
        funcionario.limpar_sessao()
        page.go("/login")  # Redireciona para a tela de login

    @staticmethod
    def validar_cpf(cpf):
        if not cpf:  # Verifica se o CPF é vazio ou None
            return False
        # Remove caracteres não numéricos
        cpf = ''.join(filter(str.isdigit, cpf))
        
        if len(cpf) != 11 or cpf == cpf[0] * 11:
            return False
        
        try:
            # Verifica o primeiro dígito verificador
            soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
            digito1 = (soma * 10 % 11) % 10

            # Verifica o segundo dígito verificador
            soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
            digito2 = (soma * 10 % 11) % 10

            return digito1 == int(cpf[9]) and digito2 == int(cpf[10])
        except ValueError:
            return False
