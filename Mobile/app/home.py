import flet as ft

def Home(page: ft.Page):
    
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
    
    def bar():
        appbar = ft.Container(
            # bgcolor=ft.colors.WHITE,
            width=390,
            height=50,
            padding=ft.padding.only(top=0 ,right=10, left=10),
            theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.BLACK)),
            content=ft.Row(
                controls=[
                    # ft.IconButton(icon=ft.icons.HOME),
                    logo(), # Chama a logo dentro da row
                    
                    # Adiciona o menu de opções
                    ft.PopupMenuButton(
                        icon = ft.icons.MENU,
                        icon_color=ft.colors.BLACK,
                        menu_position=ft.PopupMenuPosition.UNDER,
                        
                        # Items do menu
                        items=[
                            ft.PopupMenuItem(
                                icon=ft.icons.DESCRIPTION,
                                text='Meus dados',
                                ),
                            ft.PopupMenuItem(
                                icon=ft.icons.LOGOUT,
                                text='Sair'
                                )
                        ]
                    )
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            )
        )
        
        return appbar
    
    def clima():
        clima = ft.Container(
            bgcolor=ft.colors.WHITE,
            width=360,
            height=160,
            border_radius=16,
            padding=ft.padding.only(left=10, right=10),
        )
        
        return clima
    
    
    
    Main = ft.Container(
        width=390,
        height=860,
        bgcolor='#7FA677',
        border_radius=20,
        
        content=ft.Column(
            controls=[
                ft.Container(
                    padding=ft.padding.only(top=5),
                    content=ft.Stack(
                        controls=[
                            bar()
                        ]
                    )
                ),
                ft.Container(
                    padding=ft.padding.only(top=5),
                    content=ft.Stack(
                        controls=[
                            clima()
                        ]
                    )
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )
    
    return Main