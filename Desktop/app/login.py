from app.components.validacao import Validacao
from app.components.gerenciamento_banco import Atualizar
import flet as ft


def Login(page: ft.Page):
    page.title = "PIXFARM"

    def _login(e):
        valid = Validacao()

        cpf = campo_cpf.value
        senha = campo_senha.value

        if not cpf:
            mostrar_erro_login(page, "O CPF não pode estar vazio!")
            return

        if not senha:
            mostrar_erro_login(page, "A senha não pode estar vazia!")
            return

        if not Validacao.validar_cpf(cpf):
            mostrar_erro_login(page, "CPF inválido!")
            return

        login_sucesso = valid.valid_Login(cpf, senha)
        
        if login_sucesso:
            page.go("/")
            page.update()
        else:
            mostrar_erro_login(page)
            page.update()

    def mostrar_erro_login(page, mensagem="CPF ou Senha inválidos!"):
        snackbar = ft.SnackBar(ft.Text(mensagem), bgcolor=ft.colors.RED)
        page.overlay.append(snackbar)
        snackbar.open = True
        page.update()
    
    def _red_senha(e):
        atualizar = Atualizar(page)
        print('Recupera')
        atualizar.abrir_dialogo_atualizar()
        

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
    btn_senha = ft.TextButton(
        text="Redefinir Senha",
        on_click=lambda e: _red_senha(e)
    )
    btn_login = ft.ElevatedButton(
        text="Entrar",
        height=40,
        bgcolor="#13330D",                 #botão entrar
        color=ft.colors.WHITE,
        on_click=lambda e: _login(e)
    )


    
    # Definindo background
    def campos():
        campos = ft.Container(
            content=ft.Column(
                controls=[
                    campo_cpf,
                    campo_senha,
                    ft.Container(
                        content=ft.Row(
                            spacing=140,
                            controls=[
                                btn_senha,
                                btn_login,
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        )
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

