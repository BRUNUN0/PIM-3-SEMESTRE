import flet as ft

def Home(page: ft.Page):
    def sair(e):
        page.go("/login")  # Redireciona de volta para a tela de login

    return ft.Container(
        bgcolor='cyan',
        height=300,
        alignment=ft.alignment.center,
        content=ft.Column(
            controls=[
                ft.Text('Home', size=40, weight=ft.FontWeight.BOLD),
                ft.ElevatedButton(
                    text='Logout',
                    on_click=sair  # Lógica de logout
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )
