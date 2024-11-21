import flet as ft
from app.adm_funcionarios import AdminFuncionarios
from app.home import Home
from app.login import Login
from app.plantacao import Plantacao
from app.pedidos import Pedidos
from app.atividades import Atividades
from app.adm_home import AdminHome
from app.adm_clientes import AdminClientes
from app.adm_funcionarios import AdminFuncionarios
from app.adm_fornecedores import AdminFornecedores

from app.components.gerenciamento_banco import GerenciamentoBanco as gb
from app.components.funcionario import Funcionario
from app.components.validacao import Validacao

valid = Validacao()


def rotas(page: ft.Page):
    banco = gb()
    funcionario = Funcionario(banco)


    def route_change(route):            
        page.views.clear()

        # rotas_protegidas = [
        #     "/", "/plantacao", "/pedidos", "/atividades", "/adm", "/adm/clientes", "/adm/funcionarios", "/adm/fornecedores"
        # ]

        # usuario_logado = valid.verificar_usuario_logado(funcionario, page)
        # print(f"Rota acessada: {page.route}, Usuario logado: {usuario_logado}")

        # if page.route in rotas_protegidas and not usuario_logado:
        #     return

        # Pagina de Login
        if page.route == "/login":
            page.views.append(ft.View(route="/login", controls=[Login(page)]))

        # Home
        elif page.route == "/":
            page.views.append(ft.View(route="/", controls=[Home(page)]))

        # Plantação
        elif page.route == "/plantacao":
            page.views.append(ft.View(route="/plantacao", controls=[Plantacao(page)]))

        # Pedidos
        elif page.route == "/pedidos":
            page.views.append(ft.View(route="/pedidos", controls=[Pedidos(page)]))

        # Atividades
        elif page.route == "/atividades":
            page.views.append(ft.View(route="/atividades", controls=[Atividades(page)]))

        # Home Administrador
        elif page.route == "/adm":
            page.views.append(ft.View(route="/adm", controls=[AdminHome(page)]))
        
        # Administração de Clientes
        elif page.route == "/adm/clientes":
            page.views.append(ft.View(route="/adm/clientes", controls=[AdminClientes(page)]))

        # Administração de Funcionários
        elif page.route == "/adm/funcionarios":
            page.views.append(ft.View(route="/adm/funcionarios", controls=[AdminFuncionarios(page)]))

        # Administração de fornecedores
        elif page.route == "/adm/fornecedores":
            page.views.append(ft.View(route="/adm/fornecedores", controls=[AdminFornecedores(page)]))

        page.update()
        print(page.route)

    page.on_route_change = route_change
    
    def on_resize(event):
        # Aqui você pode colocar qualquer ação desejada quando a tela for redimensionada
        # print(f"Nova largura: {page.window.width}, Nova altura: {page.window.height}")
        page.update()

    # Associa a função `on_resize` ao evento de redimensionamento da página
    page.on_resized = on_resize