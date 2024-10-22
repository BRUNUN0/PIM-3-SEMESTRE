import flet as ft

def Login(page: ft.Page):

    def background():
        background = ft.Container(
            content=ft.Stack(
                controls=[
                    ft.Container(
                        content=ft.Image(
                            src='app/assets/bg.jpg'
                        )
                    ),
                    ft.Container(
                        # bgcolor=ft.colors.with_opacity(0.8, ft.colors.BLACK)
                        bgcolor=ft.colors.BLACK
                    )
                ]
            )
        )

        return background
    
    Main = ft.Container(
        bgcolor='#7FA677',

        content=ft.Column(
            controls=[
                background()
            ]
        )

    )

    return Main