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