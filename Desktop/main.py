import flet as ft
from app.routes import rotas

def main(page: ft.Page):
    page.title = "PIXFARM"
    page.window.width = 1200
    page.window.height = 800
    rotas(page)

    page.go("/login")
    page.update()

if __name__ == "__main__":
    ft.app(target=main)