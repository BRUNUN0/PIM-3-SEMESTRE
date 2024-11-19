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
        funcionario = Funcionario(banco)
        # fornecedores = banco_fornecedores.obter_fornecedores()

        # Recebe a senha inserida 
        senha_cripto = sha256(senha.encode('utf-8')).hexdigest()
        print(f'Senha criptografada: {senha_cripto}')

        # Obtém os dados do banco
        dados = funcionario.obter_funcionario_login(cpf)  # Agora usa a instância do banco
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
                funcionario.salvar_sessao(usuario)
                # dados_funcionario = dado.obter_detalhes_funcionario(_id)
                # print(dados_funcionario)
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
