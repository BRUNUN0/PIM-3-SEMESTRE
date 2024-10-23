import flet as ft

def Home(page: ft.Page):
    def sair(e):
        page.go("/login")  # Redireciona de volta para a tela de login
        
    def botoes():
        botoes = ft.Container(
            width=400,
            height=50,
            bgcolor=ft.colors.BLACK,
            
            content = ft.Column(
    controls=[
        ft.Row(
            controls=[
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.IconButton(
                                icon=ft.icons.HOME,
                                icon_size=32,
                                on_click=lambda e: print("Home clicado"),
                            ),
                            ft.Text(
                                value='Home',
                                color=ft.colors.WHITE,
                                size=16,
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    alignment=ft.alignment.center,
                    padding=10,  # Ajuste o espaçamento entre os botões
                ),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.IconButton(
                                icon=ft.icons.SETTINGS,
                                icon_size=32,
                                on_click=lambda e: print("Configurações clicado"),
                            ),
                            ft.Text(
                                value='Configurações',
                                color=ft.colors.WHITE,
                                size=16,
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    alignment=ft.alignment.center,
                    padding=10,
                ),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.IconButton(
                                icon=ft.icons.INFO,
                                icon_size=32,
                                on_click=lambda e: print("Info clicado"),
                            ),
                            ft.Text(
                                value='Info',
                                color=ft.colors.WHITE,
                                size=16,
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    alignment=ft.alignment.center,
                    padding=10,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,  # Centraliza todos os botões na linha
            spacing=20,  # Ajusta o espaçamento entre os botões na linha
        )
    ]
)

        )
        
        return botoes
    
    def AppBar():
        AppBar = ft.Container(
            bgcolor=ft.colors.BLUE,
            width=page.window.width,
            height=100,
            
            content=ft.Column(
                controls=[
                    ft.Container(
                        botoes()
                    )
                ]
            )
        )
        
        return AppBar

    Main = ft.Container(

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