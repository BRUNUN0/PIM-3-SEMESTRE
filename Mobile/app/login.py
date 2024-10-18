import flet as ft

def Login(page: ft.Page):
    
    def login(e):
        print("Login Solicitado")
        page.go('/home')
    
    def logo():
        logo = ft.Container(
            content=ft.Image(
                src="app/assets/Logo.png",
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
                                on_click= lambda e: print("Esqueci minha senha, socorro!")
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
                            bgcolor=ft.colors.WHITE,
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
            # ft.Column(
            # controls=[
            #     ft.TextField(
            #         label="ID",
            #         width=300,
            #         height=50,
            #         border_radius=ft.border_radius.all(8),
            #         bgcolor=ft.colors.WHITE,
            #         color=ft.colors.BLACK,
            #         text_style=ft.TextStyle(size=16),
            #         label_style=ft.TextStyle(
            #             color=ft.colors.BLACK,
            #             size=14
            #         )
            #     ),
            #     ft.TextField(
            #         label="Senha",
            #         width=300,
            #         height=50,
            #         color=ft.colors.BLACK,
            #         text_style=ft.TextStyle(size=16),
            #         label_style=ft.TextStyle(
            #             color=ft.colors.BLACK,
            #             size=14
            #         )
            #     ),
            #     ft.Row(
            #         controls=[
            #             botao()
            #         ]
            #     )
            # ],
            # horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
        return campos
        
    Main = ft.Container(
        width=390,
        height=860,
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
    
    return Main
    
    # ft.Container(
    #     expand=True,
    #     content=ft.Stack(
    #         controls=[
    #             # Background
    #             ft.Container(
    #                 image_src="Desktop/app/assets/Logo.png",
    #                 image_fit=ft.ImageFit.COVER,
    #                 expand=True  # Preenche todo o espaço
    #             ),
    #             ft.Container(
    #                 bgcolor=ft.colors.with_opacity(0.4, ft.colors.BLACK),
    #             ),

    #             # Container de Login
    #             ft.Column(
    #                 controls=[
    #                     ft.Container(
    #                         bgcolor="#7FA677",
    #                         width=350,
    #                         height=300,
    #                         alignment=ft.alignment.center,
    #                         border_radius=ft.border_radius.all(10),
    #                         content=ft.Column(
    #                             controls=[
    #                                 ft.Container(
    #                                     content=ft.Image(
    #                                         src="Desktop/app/assets/Logo.png",
    #                                         width=100,
    #                                         height=100,
    #                                         fit=ft.ImageFit.CONTAIN,
    #                                     ),
    #                                     width=130,
    #                                     height=130,
    #                                     alignment=ft.alignment.top_center,
    #                                     # padding=ft.padding(top=-60),
    #                                     border_radius=ft.border_radius.all(100),
    #                                     bgcolor="#7FA677"
    #                                 ),
    #                                 # Campo ID
    #                                 ft.TextField(
    #                                     label="ID",
    #                                     width=250,
    #                                     height=50,
    #                                     border_radius=ft.border_radius.all(8),
    #                                     bgcolor=ft.colors.WHITE,
    #                                     color=ft.colors.BLACK,
    #                                     text_style=ft.TextStyle(size=16),
    #                                     label_style=ft.TextStyle(
    #                                         color=ft.colors.BLACK,
    #                                         size=14
    #                                     )
    #                                 ),
    #                                 # Campo Senha
    #                                 ft.TextField(
    #                                     label="Senha",
    #                                     width=250,
    #                                     height=50,
    #                                     password=True,
    #                                     border_radius=ft.border_radius.all(8),
    #                                     bgcolor=ft.colors.WHITE,
    #                                     color=ft.colors.BLACK,
    #                                     text_style=ft.TextStyle(size=16),
    #                                     label_style=ft.TextStyle(
    #                                         color=ft.colors.BLACK,
    #                                         size=14
    #                                     )
    #                                 ),
    #                                 # Botão Entrar
    #                                 ft.ElevatedButton(
    #                                     text="Entrar",
    #                                     width=100,
    #                                     height=40,
    #                                     bgcolor=ft.colors.GREEN_900,
    #                                     color=ft.colors.WHITE,
    #                                     on_click=lambda e: print("Login clicado")
    #                                 )
    #                             ],
    #                             alignment=ft.MainAxisAlignment.CENTER,
    #                             horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    #                             spacing=20
    #                         )
    #                     ),
    #                 ],
    #                 alignment=ft.MainAxisAlignment.CENTER,
    #                 horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    #                 expand=True  # Para centralizar o container de login
    #             ),

    #             # Logo
    #             # ft.Container(
    #             #     content=ft.Image(
    #             #         src="app/assets/logo.png",
    #             #         fit=ft.ImageFit.CONTAIN
    #             #     ),
    #             #     top=120,
    #             #     width=150,
    #             #     height=150,
    #             #     border_radius=ft.border_radius.all(100),
    #             #     bgcolor="#7FA677",
    #             # )
    #         ],
    #         alignment=ft.alignment.center  # Centraliza todos os itens no Stack
    #     ),
    #     alignment=ft.alignment.center
    # )
