import flet as ft
from app.routes import rotas

def main(page: ft.Page):
    page.title = "PIXFARM"
    page.window.width = 1280
    page.window.height = 720
    rotas(page)

    page.go("/")
    page.update()

if __name__ == "__main__":
    ft.app(target=main)