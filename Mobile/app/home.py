import flet as ft
import sqlite3

def Home(page: ft.Page):
    
    def logo():
        logo = ft.Container(
            content=ft.Image(
                src="https://github.com/BRUNUN0/PIM-3-SEMESTRE/blob/b1af43c3defbc2696df0e40dc2520914365e6c97/Mobile/app/assets/Logo.png?raw=true",
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
                        icon_size=40,
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
            padding=ft.padding.only(top=5,left=10),
            
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Container(
                                width=100,
                                height=100,
                                bgcolor=ft.colors.BLUE,
                            ),
                            ft.Container(
                                width=100,
                                height=100,
                                bgcolor=ft.colors.RED
                            ),
                            ft.Container(
                                width=100,
                                height=100,
                                bgcolor=ft.colors.GREEN
                            )
                        ]
                    )
                ]
            )
        )
        
        return clima
    
    # def detalhes(e, nome, imagem):
    #     conn = sqlite3.connect('PIXFARM.db')
    #     cursor = conn.cursor()
    #     cursor.execute('SELECT nome_planta, imagem FROM producao')
    #     plantas = cursor.fetchall()
    #     conn.close()
        
    #     lista_plantas = [planta(nome, imagem) for nome, imagem in plantas]
        
    #     detalhes = ft.AlertDialog(
    #         title=ft.Text(
    #             value='Nome',
    #             size=20,
    #             weight='bold',
    #             color=ft.colors.BLACK
    #         ),
    #         content=ft.Column(
    #             controls=[
    #                 ft.Container(
                        
    #                 )
    #             ],
    #             width=335,
    #             height=400
    #         )
    #     )
        
    #     return detalhes
    
    def planta(nome, imagem):
        def on_click_container(e):
            page.dialog = ft.AlertDialog(
                title=ft.Text(f"Detalhes da {nome}"),
                content=ft.Container(
                    width=50,
                    height=50,
                    bgcolor=ft.colors.BLUE                    
                ),
                actions=[
                    ft.TextButton("Fechar", on_click=print("Olá Mundo"))
                ]
            )
            page.dialog.open = True
            page.update()
            
        planta = ft.Container(
            bgcolor="#99C2A2",
            border=ft.border.all(
                color=ft.colors.BLACK
            ),
            width=340,
            height=50,
            border_radius=9,
            padding=ft.padding.only(left=12, right=12),
            on_click=on_click_container, # -------------------------------------- AQUI CHAMA A FUNÇÃO DO BOTÃO      ATT.BRUNO
            
            content=ft.Row(
                controls=[
                    ft.Icon(
                        name=ft.icons.FOREST,
                        color=ft.colors.BLACK,
                        size=30
                        ),
                    ft.Text(
                        value=nome
                        ),
                    
                    ft.Container(
                        alignment=ft.alignment.center_right,
                        
                        content=ft.Image(
                            src=imagem,
                            width=30,
                        )
                    )
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            )
        )
        
        return planta
    
    def plantacao():
        
        conn = sqlite3.connect('PIXFARM.db')
        cursor = conn.cursor()
        cursor.execute('SELECT nome_planta, imagem FROM producao')
        plantas = cursor.fetchall()
        conn.close()
        
        lista_plantas = [planta(nome, imagem) for nome, imagem in plantas]
        
        plantacao = ft.Container(
            bgcolor=ft.colors.WHITE,
            width=360,
            height=380,
            border_radius=16,
            padding=ft.padding.only(top=5),
            
            content=ft.Column(
                controls=[
                    ft.Text(value="Plantação", size=16),
                    ft.Column(
                        controls=
                        lista_plantas,
                        spacing=6,
                        scroll='auto'
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
        
        return plantacao
    
    
    
    Main = ft.Container(
        # width=390,
        # height=860,
        expand=True,
        bgcolor='#7FA677',
        border_radius=20,
        
        content=ft.Column(
            controls=[
                ft.Container(
                    padding=ft.padding.only(top=20),
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
                ),
                ft.Container(
                    padding=ft.padding.only(top=5),
                    content=ft.Stack(
                        controls=[
                            plantacao()    
                        ]
                    )
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )
    
    return Main