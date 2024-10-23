import flet as ft
from app.home import Home
from app.login import Login


def rotas(page: ft.Page):
    def route_change(route):
        page.views.clear()

        if page.route == "/":
            page.views.append(ft.View(route="/", controls=[Home(page)]))

        elif page.route == "/login":
            page.views.append(ft.View(route="/login", controls=[Login(page)]))
        
        page.update()

    page.on_route_change = route_change
    
    def on_resize(event):
        # Aqui você pode colocar qualquer ação desejada quando a tela for redimensionada
        print(f"Nova largura: {page.window.width}, Nova altura: {page.window.height}")
        page.update()

    # Associa a função `on_resize` ao evento de redimensionamento da página
    page.on_resized = on_resize