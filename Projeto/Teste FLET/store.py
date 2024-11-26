import flet as ft

def Store(page: ft.Page):
    return ft.Container(
        bgcolor='amber',
        height=300,
        alignment=ft.alignment.center,
        content=ft.Column(
            controls=[
                ft.Text('Store', size=40),
                ft.ElevatedButton("Voltar para Home", on_click=lambda _: page.go('/'))
            ]
        )
    )