import flet as ft

def Login(page: ft.Page):
    
    def login(e):
        print("Login Solicitado")
        page.go('/')
        
    def rec_senha(e):
        print("Esqueci minha senha, socorro!")
    
    def logo():
        logo = ft.Container(
            content=ft.Image(
                src="https://github.com/BRUNUN0/PIM-3-SEMESTRE/blob/b1af43c3defbc2696df0e40dc2520914365e6c97/Mobile/app/assets/Logo.png?raw=true",
                width=150,
                height=150,
            ),
            alignment=ft.alignment.top_center,
        )
        return logo
    
    def botao():
        btn = ft.Container(
            width=300,
            height=60,
            
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.TextButton(
                                text="Esqueci minha senha",
                                width=180,
                                height=40,
                                on_click= lambda e: rec_senha(e)
                            ),
                            ft.ElevatedButton(
                                text="Entrar",
                                width=100,
                                height=40,
                                bgcolor=ft.colors.GREEN_900,
                                color=ft.colors.WHITE,
                                on_click= lambda e: login(e)
                            )
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    )
                ],
            )   
        )
        return btn
    
    def campos():
        campos = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Column(
                        controls=[
                            logo(),
                            ft.TextField(
                            label="ID",
                            width=300,
                            height=50,
                            border_radius=ft.border_radius.all(8),
                            color=ft.colors.BLACK,
                            text_style=ft.TextStyle(size=16),
                            label_style=ft.TextStyle(
                                color=ft.colors.BLACK,
                                size=14
                                )
                            ),
                            ft.TextField(
                                label="Senha",
                                width=300,
                                height=50,
                                password=True,
                                color=ft.colors.BLACK,
                                text_style=ft.TextStyle(size=16),
                                label_style=ft.TextStyle(
                                    color=ft.colors.BLACK,
                                    size=14
                                )
                            ),
                            
                            ft.Row(
                                controls=[
                                    ft.Stack(
                                        controls=[
                                            botao()
                                        ],
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.CENTER
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    )
                ]
            )
        )
        return campos
    
    Main = ft.Container(
        # width=390,
        # height=,
        expand=True,
        bgcolor='#7FA677',
        border_radius=20,
        
        content=ft.Column(
            controls=[
                ft.Container(
                    content=ft.Stack(
                        controls=[
                            campos()
                        ]
                    )
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )
    page.update()
    
    return Main