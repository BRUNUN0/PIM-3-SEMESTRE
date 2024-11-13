import flet as ft
from app.routes import rotas

def main(page: ft.Page):
    page.theme = ft.Theme(color_scheme_seed="blue")
    page.title = "PIXFARM"
    page.window.maximized = False
    page.window.resizable = False
    rotas(page)
    print(page.route)

    # page.go("/adm/funcionarios")
    page.go('/pedidos')
    page.update()

if __name__ == "__main__":
    ft.app(target=main)

