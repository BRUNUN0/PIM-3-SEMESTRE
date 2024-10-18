import flet as ft

def Home(page: ft.Page):
    
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
                            ...
                        ]
                    )
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )
    
    return Main