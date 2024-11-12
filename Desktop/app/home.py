import flet as ft
import datetime
from app.components.dialogs import DialogoSaida, Detalhes
from app.components.classes import GerenciamentoBanco


def Home(page: ft.Page):
    page.title = "Home"
    def sair(e):
        page.go("/login")  # Redireciona de volta para a tela de login

        
    def relogio():
        agora = datetime.datetime.now()
        relogio = ft.Container(
            width=200,
            content=ft.Column(
                controls=[
                    ft.Text(value=agora.strftime("%H:%M:%S"), color=ft.colors.BLACK, size=16),
                    ft.Text(value=agora.strftime("%d/%m/%Y"), color=ft.colors.BLACK),
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
                        bgcolor=ft.colors.WHITE,
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
        def hover_btn(e):
            e.control.icon_color=ft.colors.BLACK if e.data == "true" else None
            e.control.update()
        

        botoes = ft.Container(
            expand=True,
            # height=100,
            bgcolor="#D9FFBA",
            
            content = ft.Column(
    controls=[
        ft.Row(
            controls=[
                ft.Container(
                    on_hover=hover_btn,
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
                    padding=10,
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
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
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
            expand=True,
            
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

    def pproducao(nome, imagem):

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
            on_click=on_click_container,
            
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
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            )
        )
        
        return planta
    
    def em_producao ():

        banco = GerenciamentoBanco()
        producoes = banco.obter_producao()
        if producoes:
            lista_producao = [pproducao(nome, imagem) for  _, _, nome, _, imagem in producoes]
        else:
            lista_producao = [ft.Container(expand=True, content=ft.Row(controls=[ft.Text(value="Nenhuma produção em andamento", color=ft.colors.BLACK)],alignment=ft.MainAxisAlignment.CENTER) )]

        producao = ft.Container(
            width=350,
            bgcolor='#D6D6D6',
            border_radius=16,

            content=ft.Column(
                controls=[
                    ft.Text(value='Em produção:', size=20, color=ft.colors.BLACK, weight=ft.FontWeight.BOLD),
                    ft.Column(
                        controls=
                        lista_producao,
                        spacing=6,
                        scroll=ft.ScrollMode.AUTO
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
        return producao
    
    def pedido(nome, imagem):
        planta = ft.Container(
            bgcolor="#99C2A2",
            border=ft.border.all(
                color=ft.colors.BLACK
            ),
            width=340,
            height=50,
            border_radius=9,
            padding=ft.padding.only(left=12, right=12),
            on_click=print("Grita socorro"), 
            
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
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            )
        )
        
        return planta

    def pedidos():
        banco = GerenciamentoBanco()
        # producoes = banco.obter_pedidos_abertos()
        # if producoes:
        #     lista_producao = [pedido(nome, imagem) for  nome, imagem in producoes]
        # else:
        #     lista_producao = [ft.Container(expand=True, content=ft.Row(controls=[ft.Text(value="Nenhum pedido no momento", color=ft.colors.BLACK)],alignment=ft.MainAxisAlignment.CENTER) )]

        producao = ft.Container(
            width=350,
            bgcolor='#D6D6D6',
            border_radius=16,

            content=ft.Column(
                controls=[
                    ft.Text(value='Pedidos:', size=20, color=ft.colors.BLACK, weight=ft.FontWeight.BOLD),
                    # ft.Column(
                    #     controls=
                    #     lista_producao,
                    #     spacing=6,
                    #     scroll=ft.ScrollMode.AUTO
                    # )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
        return producao


    def conteudo():
        conteudo = ft.Container(
            padding=ft.padding.only(left=25,),
            content=ft.ResponsiveRow(
                controls=[
                    ft.Row(
                        controls=[
                            em_producao(),
                            pedidos()
                        ]
                    ),
                ],
                
            )
        )

        return conteudo
    

    Main = ft.Container(
        bgcolor=ft.colors.WHITE,
        expand=True,
        padding=ft.padding.only(bottom=10),

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

    return Main