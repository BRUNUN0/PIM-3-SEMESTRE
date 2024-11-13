import flet as ft
import datetime
from app.components.classes import GerenciamentoBanco, Cadastro
from app.components.pedido import Pedido
from app.components.detalhes import Detalhes


def Pedidos(page: ft.Page):

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
            width=200,
            content=ft.Image(
                src="https://github.com/BRUNUN0/PIM-3-SEMESTRE/blob/b1af43c3defbc2696df0e40dc2520914365e6c97/Mobile/app/assets/Logo.png?raw=true",
                width=50,
                height=50,
            ),
            alignment=ft.alignment.top_center,
            on_click= lambda e: page.go('/adm')
        )
        return logo
    
    def menu():
        menu = ft.Container(
            width=200,
            content=ft.Row(
                controls=[
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
                                # on_click=lambda e: dialogo_saida.abrir()
                            )
                        ]
                    )
                ],
                alignment=ft.MainAxisAlignment.END
            )
        )
        return menu
        
    def appbar_superior():
        app_sup = ft.Container(
            content=ft.Row(
                controls=[
                    relogio(),
                    logo(),
                    menu()
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
    
    def pedido(id_pedido, cliente, nome, produto):
        # Cria um objeto de detalhes (presumivelmente, para exibir mais informações sobre o fornecedor)
        banco = GerenciamentoBanco
        detalhes = Detalhes(page, banco)

        # Cria o contêiner que vai representar o fornecedor.    
        pedido = ft.Container(
            bgcolor="#99C2A2",
            border=ft.border.all(color=ft.colors.BLACK),
            height=50,
            border_radius=9,
            padding=ft.padding.only(left=12, right=12),
            on_click=lambda e: detalhes.detalhes_pedido(id_pedido),
            
            content=ft.Row(
                controls=[
                    # ft.Icon(
                    #     name=ft.icons.FOREST,
                    #     color=ft.colors.BLACK,
                    #     size=30
                    #     ),
                    ft.Text(
                        value=f"ID: {id_pedido}",
                        color=ft.colors.BLACK
                        ),
                    ft.Text(
                        value=cliente,
                        color=ft.colors.BLACK
                    ),
                    ft.Text(
                        value=nome,
                        color=ft.colors.BLACK
                        ),
                    ft.Text(
                        value=produto,
                        color=ft.colors.BLACK
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            )
        )
        
        return pedido

    def pedidos_ativos():
        banco = GerenciamentoBanco()
        banco_pedidos = Pedido(banco)
        pedidos = banco_pedidos.obter_pedidos_abertos()
        if pedidos:
            lista_pedidos = [pedido(id_pedido, cliente, nome, produto) for id_pedido, cliente, nome, produto in pedidos]
        else:
            lista_pedidos = [ft.Container(expand=True, content=ft.Row(controls=[ft.Text(value="Nenhum pedido encontrado", color=ft.colors.BLACK)],alignment=ft.MainAxisAlignment.CENTER) )]


        cadastro = Cadastro(page)
        container = ft.Container(
            bgcolor='#D9D9D9',
            padding=ft.padding.only(left=15, right=15, top=15, bottom=5),
            border_radius=20,
            expand=True,

            content=ft.Column(
                controls=[
                    ft.Text(value='Pedidos Ativos', color=ft.colors.BLACK, size=20, weight=ft.FontWeight.BOLD),
                    ft.Container(
                        expand=True,
                        bgcolor=ft.colors.WHITE,
                        border_radius=12,
                        padding=ft.padding.all(15),
                        content=ft.Column(
                            controls=
                            lista_pedidos,
                            spacing=6,
                            scroll=ft.ScrollMode.AUTO
                        )
                    ),
                    ft.Container(
                        padding=ft.padding.only(left=50, right=50),

                        content=ft.Row(
                            controls=[
                                ft.ElevatedButton(
                                    text='Finalizar Pedido',
                                    color=ft.colors.WHITE,
                                    height=40,
                                    bgcolor="#13330D",
                                    on_click=lambda e: print("fazer")
                                ),
                                ft.ElevatedButton(
                                    text='Registrar Pedido',
                                    color=ft.colors.WHITE,
                                    # width=120,
                                    height=40,
                                    bgcolor="#13330D",
                                    on_click=lambda e: cadastro.abrir_registro('pedido')
                                )
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        )

                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )

        )

        return container
    
    def pedidos_finalizados():
        banco = GerenciamentoBanco()
        banco_pedidos = Pedido(banco)
        pedidos = banco_pedidos.obter_pedidos_finalizados()
        if pedidos:
            lista_pedidos = [pedido(id_pedido, cliente, nome, produto) for id_pedido, cliente, nome, produto in pedidos]
        else:
            lista_pedidos = [ft.Container(expand=True, content=ft.Row(controls=[ft.Text(value="Nenhum pedido encontrado", color=ft.colors.BLACK)],alignment=ft.MainAxisAlignment.CENTER) )]

        pedidos_finalizados = ft.Container(
            bgcolor='#D9D9D9',
            padding=ft.padding.only(left=15, right=15, top=15, bottom=15),
            border_radius=20,
            expand=True,

            content=ft.Column(
                controls=[
                    ft.Text(value='Pedidos Finalizados', color=ft.colors.BLACK,size=20, weight=ft.FontWeight.BOLD),
                    ft.Container(
                        expand=True,
                        bgcolor=ft.colors.WHITE,
                        border_radius=12,
                        padding=ft.padding.all(15),
                        content=ft.Column(
                            controls=
                            lista_pedidos,
                            spacing=6,
                            scroll=ft.ScrollMode.AUTO
                        )
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
        return pedidos_finalizados
    
            
    def conteudo():
        conteudo = ft.Container(
            padding=ft.padding.only(left=25, right=25, top=0, bottom=0),
            expand=True,
            content=ft.ResponsiveRow(
                controls=[
                    ft.Row(
                        controls=[
                            pedidos_ativos(),
                            pedidos_finalizados()
                        ],
                    ),
                ],
                # alignment=ft.MainAxisAlignment.CENTER,
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
    
    # page.on_resized = page.update()

    return Main