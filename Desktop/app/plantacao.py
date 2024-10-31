import flet as ft
from datetime import datetime
import pyodbc
from app.components.dialogs import DialogoSaida, Detalhes
from app.components.classes import GerenciamentoBanco


def Plantacao(page: ft.Page):
    def sair(e):
        page.go("/login")  # Redireciona de volta para a tela de login

        
    def relogio():
        relogio = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(value="00:00:00", size=16),
                    ft.Text(value="28/10/2024"),
                ]
            )
        )
        return relogio
    
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
        
    def appbar_superior():
        dialogo_saida = DialogoSaida(page)
        
        app_sup = ft.Container(
            content=ft.Row(
                controls=[
                    relogio(),
                    logo(),
                    ft.PopupMenuButton(
                        icon=ft.icons.MENU,
                        icon_color=ft.colors.BLACK,
                        icon_size=40,
                        menu_position=ft.PopupMenuPosition.UNDER,
                        
                        items=[
                            ft.PopupMenuItem(
                                icon=ft.icons.ADD_MODERATOR,
                                text='Administrar',
                                on_click=lambda e: page.go('/adm')
                            ),
                            ft.PopupMenuItem(
                                icon=ft.icons.LOGOUT,
                                text='Sair',
                                on_click=lambda e: dialogo_saida.abrir()
                            )
                        ]
                    )
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            )
        )
        
        return app_sup
        
    def botoes():
        botoes = ft.Container(
            expand=True,
            # height=100,
            bgcolor="#D9FFBA",
            
            content = ft.Column(
    controls=[
        ft.Row(
            controls=[
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.IconButton(
                                width=50,
                                height=50,
                                icon=ft.icons.HOME,
                                icon_size=32,
                                on_click=lambda e: page.go('/'),
                                icon_color = ft.colors.with_opacity(0.5, ft.colors.BLACK),
                            ),
                            ft.Text(
                                value='Home',
                                color= ft.colors.with_opacity(0.5, ft.colors.BLACK),
                                size=16,
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    alignment=ft.alignment.center,
                    padding=10,  # Ajuste o espaçamento entre os botões
                ),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.IconButton(
                                icon=ft.icons.ECO,
                                icon_size=32,
                                on_click=lambda e: page.go('/plantacao'),
                                icon_color = ft.colors.with_opacity(0.5, ft.colors.BLACK), 
                            ),
                            ft.Text(
                                value='Plantação',
                                color= ft.colors.with_opacity(0.5, ft.colors.BLACK),
                                size=16,
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    alignment=ft.alignment.center,
                    padding=10,
                ),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.IconButton(
                                icon=ft.icons.BOOKMARK_ADD_SHARP,
                                icon_size=32,
                                on_click=lambda e: page.go('/pedidos'),
                                icon_color = ft.colors.with_opacity(0.5, ft.colors.BLACK), 
                            ),
                            ft.Text(
                                value='Pedidos',
                                color= ft.colors.with_opacity(0.5, ft.colors.BLACK),
                                size=16,
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    alignment=ft.alignment.center,
                    padding=10,
                ),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.IconButton(
                                icon=ft.icons.CHECKLIST,
                                icon_size=32,
                                on_click=lambda e: page.go('/atividades'),
                                icon_color = ft.colors.with_opacity(0.5, ft.colors.BLACK), 
                            ),
                            ft.Text(
                                value='Atividades',
                                color= ft.colors.with_opacity(0.5, ft.colors.BLACK),
                                size=16,
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    alignment=ft.alignment.center,
                    padding=10,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,  # Centraliza todos os botões na linha
            spacing=20,  # Ajusta o espaçamento entre os botões na linha
        )
    ]
)

        )
        
        return botoes
    
    def AppBar():
        AppBar = ft.Container(
            bgcolor="#D9FFBA",
            width=page.window.width,
            height=175,
            
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                appbar_superior(),
                                botoes()
                            ],
                        ),
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        
        return AppBar

    # def grafico_plantas():
    #     dados = [
    #         ("Dez", 100, ft.colors.YELLOW),
    #         ("Nov", 90, ft.colors.GREEN),
    #         ("Out", 85, ft.colors.GREEN),
    #         ("Set", 75, ft.colors.GREEN),
    #         ("Ago", 65, ft.colors.BLUE),
    #         ("Jul", 55, ft.colors.BLUE),
    #         ("Jun", 45, ft.colors.BLUE),
    #         ("Mai", 35, ft.colors.BLUE),
    #         ("Abr", 25, ft.colors.RED),
    #         ("Mar", 20, ft.colors.RED),
    #         ("Fev", 15, ft.colors.RED),
    #         ("Jan", 10, ft.colors.RED)
    #     ]

    #     barras = ft.Column(
    #         controls=[
    #             ft.Row(
    #                 controls=[
    #                     ft.Text(label, width=50),
    #                     ft.Container(
    #                         width=valor * 2,
    #                         height=20,
    #                         bgcolor=cor,
    #                     ),
    #                     ft.Text(f"{valor}%", width=40)
    #                 ],
    #                 alignment=ft.MainAxisAlignment.START,
    #                 spacing=10
    #             )
    #             for label, valor, cor, in dados
    #         ],
    #         spacing=5
    #     )

    #     grafico = ft.Container(
    #         width=350,
    #         height=500,
    #         bgcolor='#D6D6D6',
    #         border_radius=16,

    #         content=ft.Column(
    #             controls=[
    #                 ft.Text(value='COLUMN', size=20, weight=ft.FontWeight.BOLD),
    #                 ft.Container(
    #                     barras
    #                 )
    #             ],
    #             horizontal_alignment=ft.CrossAxisAlignment.CENTER
    #         )
    #     )
    #     return grafico
    
    def planta(nome, imagem):

        def on_click_container(e):
            print(f"Clicado: {nome}")  
            
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
                        color=ft.colors.GREEN_900,
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
                # scroll='auto',
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            )
        )
        
        return planta
    
    def plantacao ():

        banco = GerenciamentoBanco()
        plantas_data = banco.obter_plantas()

        lista_plantas = [planta(nome, imagem) for nome, imagem in plantas_data]

        grafico = ft.Container(
            width=350,
            height=500,
            bgcolor='#D6D6D6',
            border_radius=16,

            content=ft.Column(
                controls=[
                    ft.Text(value='COLUMN', size=20, weight=ft.FontWeight.BOLD),
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
        return grafico

    def conteudo():
        conteudo = ft.Container(
            padding=ft.padding.only(left=25,),
            content=ft.ResponsiveRow(
                controls=[
                    ft.Row(
                        controls=[
                            # grafico_plantas(),
                            plantacao()
                        ]
                    ),
                    # ft.Container(
                    #     width=250,
                    #     height=500,
                    #     bgcolor='#D6D6D6',
                    #     padding=ft.padding.only(left=10),
                    #     border_radius=16
                    # )
                ],
                
            )
        )

        return conteudo

    Main = ft.Container(
        expand=True,
        padding=ft.padding.all(0),
        # bgcolor=ft.colors.RED,

        content=ft.Column(
            controls=[
                ft.Container(
                    AppBar(),
                    alignment=ft.alignment.top_center
                ),
                ft.Container(
                    conteudo(),
                    expand=True
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )
    
    # page.on_resized = page.update()

    return Main