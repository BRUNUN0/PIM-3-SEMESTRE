import flet as ft

def Home(page: ft.Page):
    return ft.Container(
        content=ft.Column(
            controls=[
                ft.TextField("Página Home"),
                ft.ElevatedButton("Ir Login", on_click=lambda _: page.go('/login'))
            ]
        )
    )