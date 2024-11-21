# from app.components.validacao import Validacao
import flet as ft

# valid = Validacao()
def Login(page: ft.Page):
    page.title = "PIXFARM"


    def _login(e):
        cpf_valor = campo_cpf.value
        senha_valor = campo_senha.value

        print(f"cpf do cara: {cpf_valor}")
        print(f"senha do caba: {senha_valor}")

    #     # login_sucesso = valid.valid_Login(cpf_valor, senha_valor)
        
    #     if login_sucesso:
    #         page.go("/")
    #         page.update()
    #     else: 
    #         print("Erro de login")
    #         mostrar_erro_login(page)
    #         page.update()

    # def mostrar_erro_login(page):
    #     dialog = ft.AlertDialog(
    #         content=ft.Container(
    #             width=60,
    #             height=25,
    #             content=ft.Text("CPF ou Senha incorretos!"),
    #             alignment=ft.alignment.center,
    #         ),
    #     )
    #     page.overlay.append(dialog)
    #     dialog.open = True
    #     page.update()
        

    def logo():
        logo = ft.Container(
            bgcolor='#7FA677',
            border_radius=ft.border_radius.all(100),
            content=ft.Image(
                src="https://github.com/BRUNUN0/PIM-3-SEMESTRE/blob/b1af43c3defbc2696df0e40dc2520914365e6c97/Mobile/app/assets/Logo.png?raw=true",
                width=130,
                height=130,
            ),
        ) 
        return logo
    

    # Logo da pagina    
    def background():
        background = ft.Stack(
            controls=[
                ft.Container(
                    expand=True,
                    bgcolor=ft.colors.BLUE,
                    content=ft.Image(
                        src='https://github.com/BRUNUN0/PIM-3-SEMESTRE/blob/341bd27476279d2aa9ce9c5295f538336d1b2458/Mobile/app/assets/bg.jpg?raw=true',
                        fit=ft.ImageFit.COVER,
                        # expand=True
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
    btn_login = ft.ElevatedButton(
        text="Entrar",
        height=40,
        bgcolor="#13330D",
        color=ft.colors.WHITE,
        on_click=lambda e: _login(e)
    )

    # Definindo background
    def campos():
        campos = ft.Container(
            padding=ft.padding.only(left=15, right=15),
            content=ft.Column(
                controls=[
                    campo_cpf,
                    campo_senha,
                    ft.Container(
                        btn_login,
                        alignment=ft.alignment.center_right
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
        return campos
        
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
                                padding=ft.padding.only(top=90)
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
                                alignment=ft.alignment.center
                            ),
                        ],
                        alignment=ft.alignment.center,
                    )
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )
    return Main