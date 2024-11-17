import flet as ft
from app.routes import rotas
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


def main(page: ft.Page):
    page.theme = ft.Theme(color_scheme_seed="blue")
    page.title = "PIXFARM"
    page.window.maximized = False
    page.window.resizable = False
    rotas(page)
    print(page.route)

    # page.go("/adm/funcionarios")
    # page.go('/adm/fornecedores')
    page.go('/')
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
