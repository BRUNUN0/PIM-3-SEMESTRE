# Importando o pacote necessário
import flet as ft

# Função que cria a página do login
def main(page: ft.Page):
    # Container de Login
    login_container = ft.Column(
        controls=[
            # Container para o logo
            ft.Container(
                content=ft.Image(
                    src="logo.png",  # Substitua "logo.png" pelo caminho da sua imagem
                    width=100,
                    height=100,
                    fit=ft.ImageFit.CONTAIN
                ),
                width=130,
                height=130,
                alignment=ft.alignment.center,
                border_radius=ft.border_radius.all(100),
                bgcolor="#7FA677"
            ),
            # Container do formulário de login
            ft.Container(
                bgcolor="#7FA677",
                width=350,
                height=250,
                alignment=ft.alignment.center,
                border_radius=ft.border_radius.all(10),
                content=ft.Column(
                    controls=[
                        # Campo ID
                        ft.TextField(
                            label="ID",
                            width=250,
                            height=50,
                            border_radius=ft.border_radius.all(8),
                            bgcolor=ft.colors.WHITE,
                            color=ft.colors.BLACK,
                            text_style=ft.TextStyle(size=16),
                            label_style=ft.TextStyle(
                                color=ft.colors.BLACK,
                                size=14
                            )
                        ),
                        # Campo Senha
                        ft.TextField(
                            label="Senha",
                            width=250,
                            height=50,
                            password=True,
                            border_radius=ft.border_radius.all(8),
                            bgcolor=ft.colors.WHITE,
                            color=ft.colors.BLACK,
                            text_style=ft.TextStyle(size=16),
                            label_style=ft.TextStyle(
                                color=ft.colors.BLACK,
                                size=14
                            )
                        ),
                        # Botão Entrar
                        ft.ElevatedButton(
                            text="Entrar",
                            width=100,
                            height=40,
                            bgcolor=ft.colors.GREEN_900,
                            color=ft.colors.WHITE,
                            on_click=lambda e: print("Login clicado")
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20
                )
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True  # Para centralizar o container de login
    )

    # Adiciona o container de login à página
    page.add(login_container)

# Inicia a aplicação
ft.app(target=main)
