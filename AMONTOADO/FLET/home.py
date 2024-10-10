import flet as ft

def Home(page: ft.Page):
    return ft.Container(
        bgcolor='cyan',
        height=300,
        alignment=ft.alignment.center,
        content=ft.Column(
            controls=[
                ft.Text('HOME', size=40),
                ft.ElevatedButton("Ir para a loja", on_click=lambda _: page.go('/store'))
            ]
        )
    )