import flet as ft

def Home(page: ft.Page):
    def sair(e):
        page.go("/login")  # Redireciona de volta para a tela de login
        
    def AppBar():
        AppBar = ft.Container(
            bgcolor=ft.colors.BLUE
        )
        
        return AppBar

    Main = ft.Container(
        expand=True,

        content=ft.Row(
            controls=[
                ft.Container(
                    AppBar()
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )
    
    # page.on_resized = page.update()

    return Main