import flet as ft
from app import adm_clientes
from app.home import Home
from app.login import Login
from app.adm_home import AdminHome
from app.adm_clientes import AdminClientes
from app.adm_fornecedores import AdminFornecedores



def rotas(page: ft.Page):
    def route_change(route):
        page.views.clear()

        if page.route == "/":
            page.views.append(ft.View(route="/", controls=[Home(page)]))

        elif page.route == "/login":
            page.views.append(ft.View(route="/login", controls=[Login(page)]))

        elif page.route == "/adm":
            page.views.append(ft.View(route="/adm", controls=[AdminHome(page)]))
        
        elif page.route == "/adm/clientes":
            page.views.append(ft.View(route="/adm/clientes", controls=[AdminClientes(page)]))

        elif page.route == "/adm/fornecedores":
            page.views.append(ft.View(route="/adm/fornecedores", controls=[AdminFornecedores(page)]))

        page.update()

    page.on_route_change = route_change
    
    def on_resize(event):
        # Aqui você pode colocar qualquer ação desejada quando a tela for redimensionada
        print(f"Nova largura: {page.window.width}, Nova altura: {page.window.height}")
        page.update()

    # Associa a função `on_resize` ao evento de redimensionamento da página
    page.on_resized = on_resize