import flet as ft

def Login(page: ft.Page):
    
    def background():
        background = ft.Stack(
            ft.Container(
                content=ft.Image(
                    src="app/assets/bg.jpg",
                    fit=ft.ImageFit.COVER,
                    )
            ),
            # ft.Container(
            #     content=ft.Container(
            #         bgcolor=ft.colors.with_opacity(0.4, ft.colors.BLACK),
            #         expand=True
            #     )
            # )
        )
        return background
    
    Main = ft.Container(
        expand=True,
        bgcolor='#7FA677',
        border_radius=20,
        
        content=ft.Stack(
            expand=True,
            controls=[
                ft.Container(
                    background(),
                    # bgcolor=ft.colors.with_opacity(0.4, ft.colors.BLACK),
                )
            ]
        )
    )
    
    return Main