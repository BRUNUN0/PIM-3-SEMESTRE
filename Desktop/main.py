import flet as ft
from app.routes import rotas

def main(page: ft.Page):
    page.title = "PIXFARM"
    page.window.maximized = True
    page.window.resizable = False
    rotas(page)
    print(page.route)

    page.go("/login")
    page.update()

if __name__ == "__main__":
    ft.app(target=main)