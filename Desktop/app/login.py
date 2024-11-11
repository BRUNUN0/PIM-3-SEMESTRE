import flet as ft
<<<<<<< HEAD
from app.components.validacao import Validacao 


def Login(page: ft.Page):
    
    def login(e):
        cpf_valor = campo_cpf.value
        senha_valor = campo_senha.value
        print(f"CPF: {cpf_valor}, Senha: {senha_valor}")
# Enviado usuario para a pagina "/" (bruno nao sei o que seria"/)

    def logo():
        logo = ft.Container(
            bgcolor='#7FA677',
            # height=100,
            border_radius=ft.border_radius.all(100),
            # padding=ft.padding.only(top=-70),
            content=ft.Image(
                src="https://github.com/BRUNUN0/PIM-3-SEMESTRE/blob/b1af43c3defbc2696df0e40dc2520914365e6c97/Mobile/app/assets/Logo.png?raw=true",
                width=130,
                height=130,
            ),
            # alignment=ft.alignment.center,
        )
        return logo
# Logo da pagina
    def background():
        background = ft.Stack(
            controls=[
                ft.Container(
                    width=page.window.width,
                    expand=True,
                    bgcolor=ft.colors.BLUE,
                    content=ft.Image(
                        src='app/assets/bg.jpg',
                        fit=ft.ImageFit.COVER,
                        expand=True
                        )
                    ),
                    ft.Container(
                        bgcolor=ft.colors.with_opacity(0.2, ft.colors.BLACK)
                    )
                ],
            expand=True,
            )

        return background
    
    campo_cpf = ft.TextField(
        label='CPF',
        width=350,
        height=50,
        border_radius=ft.border_radius.all(8),
        color=ft.colors.BLACK,
        text_style=ft.TextStyle(size=16),
        label_style=ft.TextStyle(
            color=ft.colors.BLACK,
            size=14
        )
    )
    campo_senha = ft.TextField(
        label='Senha',
        width=350,
        height=50,
        password=True,
        border_radius=ft.border_radius.all(8),
        color=ft.colors.BLACK,
        text_style=ft.TextStyle(size=16),
        label_style=ft.TextStyle(
            color=ft.colors.BLACK,
            size=14
        )
    )
    # btn_login = ft.ElevatedButton(
    #     text="Entrar",
    #     width=100,
    #     height=40,
    #     bgcolor="#13330D",                 #botão entrar
    #     color=ft.colors.WHITE,
    #     on_click=lambda e: login(e)
    # )


    
# Definindo background
    def campos():
        campos = ft.Container(
            content=ft.Column(
                controls=[
                    campo_cpf,
                    campo_senha,
                    ft.Container(
                        btn_login(),
                        padding=ft.padding.only(left=250),
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )

        return campos
    
    def btn_login():
        # Botão Entrar
        btn = ft.ElevatedButton(
            text="Entrar",
            width=100,
            height=40,
            bgcolor="#13330D",                 #botão entrar
            color=ft.colors.WHITE,
            on_click=lambda e: login(e)
            )
        
        return btn
        
    def caixa_login():
        caixa_login = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Stack(
                        controls=[
                            ft.Container(
                                width=400,
                                height=300,
                                bgcolor='#7FA677',
                                border_radius=ft.border_radius.all(20),
                                
                                
                            ),
                            ft.Container(
                                logo(),
                                
                                padding=ft.padding.only(top=-60),
                            ),
                            ft.Container(
                                campos(),
                                padding=ft.padding.only(top=90)              #caixa de login
                            ),
                        ],
                        alignment=ft.alignment.top_center
                        
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )

        return caixa_login
    
    Main = ft.Container(
        expand=True,

        content=ft.Row(
            controls=[
                ft.Container(
                    expand=True,
                    content=ft.Stack(
                        controls=[
                            ft.Container(
                                background(),
                                expand=True
                            ),
                            ft.Container(
                                caixa_login(),
                                alignment=ft.alignment.center        # isso aqui eu nao sei o que é | Isaque: faz as coisas dantro do Container sempre ficar no centro da "Caixa"
                            ),
                        ],
                        alignment=ft.alignment.center,
                    )
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )
    
    # page.on_resized = page.update()

    return Main