import flet as ft

def Login(page: ft.Page):

    def logo():
        logo = ft.Container(
            content=ft.Image(
                src="app/assets/Logo.png",
                width=50,
                height=50,
            ),
            alignment=ft.alignment.top_center,
        )
        return logo

    def background():
        background = ft.Stack(
            controls=[
                ft.Container(
                        content=ft.Image(
                            src='app/assets/bg.jpg'
                        )
                    ),
                    # Provavelmente será removido
                    ft.Container(
                        bgcolor=ft.colors.with_opacity(0.8, ft.colors.BLACK)
                        # bgcolor=ft.colors.BLACK
                    )
                ]
            )

        return background
    

    def campos():
        campos = ft.Container(
            bgcolor='#7FA677',
            width=450,
            height=350,
            alignment=ft.alignment.center,
            border_radius=ft.border_radius.all(10),
            content=ft.Column(
                controls=[
                    ft.TextField(
                        label='ID',
                        width=350,
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
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )

        return campos
    
    def caixa_login():
        caixa_login = ft.Container(
            bgcolor='#7FA677',
            width=450,
            height=350,
            alignment=ft.alignment.center,
            border_radius=ft.border_radius.all(10),
            content=ft.Column(
                controls=[
                    logo(),
                    campos()
                ]
            )
        )

        return caixa_login
    
    Main = ft.Container(
        width=1280,
        height=720,
        bgcolor='#7FA677',

        content=ft.Column(
            controls=[
                ft.Container(
                    content=ft.Stack(
                        controls=[
                            ft.Container(
                                background()
                            ),
                            ft.Container(
                                caixa_login()
                            )
                        ],
                        alignment=ft.alignment.center
                    )
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

    return Main