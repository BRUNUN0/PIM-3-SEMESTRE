import flet as ft
import datetime
from app.components.gerenciamento_banco import GerenciamentoBanco
from app.components.detalhes import Detalhes
from app.components.producao import Producao
from app.components.pedido import Pedido

def Home(page: ft.Page):

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
            # width=200,
            content=ft.Image(
                src="https://github.com/BRUNUN0/PIM-3-SEMESTRE/blob/b1af43c3defbc2696df0e40dc2520914365e6c97/Mobile/app/assets/Logo.png?raw=True",
                # src = "https://ibb.co/8x9fQ4W",
                width=50,
                height=50,
            ),
            alignment=ft.alignment.top_center,
        )
        return logo
    
    def menu():
        menu = ft.PopupMenuButton(
            bgcolor=ft.colors.WHITE,
            icon=ft.icons.MENU,
            icon_color=ft.colors.BLACK,
            icon_size=40,
            menu_position=ft.PopupMenuPosition.UNDER,
            items=[
                ft.PopupMenuItem(
                    icon=ft.icons.DESCRIPTION,
                    text='Meus Dados',
                    on_click=lambda e: print('tome dados do usuario')
                ),
                ft.PopupMenuItem(
                    icon=ft.icons.LOGOUT,
                    text='Sair',
                    on_click=lambda e: print('uii fugi')
                )
            ]
        )
        return menu
    
    def appbar():
        appbar = ft.Container(
            height=50,
            content=ft.Row(
                controls=[
                    logo(),
                    menu()
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            )
        )
        return appbar
    
    def container():
        banco = GerenciamentoBanco()
        pedidos = Pedido(banco)
        n_pedidos = pedidos.contar_pedidos_abertos()
        print(n_pedidos)

        cards = ft.Container(
            padding=ft.padding.only(left=10, right=10),
            # height=900,
            # expand
            content=ft.Row(
                controls=[
                    ft.Container(
                        expand=True,
                        bgcolor=ft.colors.RED,
                        content=ft.Column(
                            controls=[
                                ft.Text(value='Pedidos Ativos', size=18, weight='bold', text_align=ft.TextAlign.CENTER, color=ft.colors.BLACK),
                                ft.Text(value=n_pedidos, size=12, text_align=ft.TextAlign.CENTER, color=ft.colors.BLACK)
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        )
                    ),
                    ft.Container(
                        expand=True,
                        bgcolor=ft.colors.BLUE,
                        content=ft.Text(value='teste2')
                    ),
                    ft.Container(
                        expand=True,
                        bgcolor=ft.colors.GREEN,
                        content=ft.Column(
                            controls=[
                                ft.Text(value='testando'),
                                ft.Text(value='testando ainda')
                            ]
                        )
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )
        container = ft.Container(
            # expand=True,
            height=120,
            bgcolor=ft.colors.WHITE,
            border_radius=20,
            content=ft.Column(
                controls=[
                    cards
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
        return container
    
    def plantacao(id_plantio, plantio, nome, quantidade):
        banco = GerenciamentoBanco
        detalhes = Detalhes(page, banco)

        produto = ft.Container(
            bgcolor="#99C2A2",
            border=ft.border.all(color=ft.colors.BLACK),
            height=50,
            border_radius=9,
            padding=ft.padding.only(left=12, right=12),
            on_click=lambda e: detalhes.detalhes_producao(id_plantio),
            content=ft.Row(
                controls=[
                    ft.Text(
                        value=f"ID: {id_plantio}",
                        color=ft.colors.BLACK
                    ),
                    ft.Text(
                        value=plantio,
                        color=ft.colors.BLACK
                    ),
                    ft.Text(
                        value=nome,
                        color=ft.colors.BLACK
                    ),
                    ft.Text(
                        value=quantidade,
                        color=ft.colors.BLACK
                    )
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            )
        )
        return produto

    def plantacoes():
        banco = GerenciamentoBanco()
        banco_producao = Producao(banco)
        producoes = banco_producao.obter_producao()
        if producoes:
            lista_plantacao = [plantacao(id_plantio, plantio, nome, quantidade) for id_plantio, plantio, nome, quantidade, *rest in producoes]
        else:
            lista_plantacao = [ft.Container(expand=True, content=ft.Row(controls=[ft.Text(value="Nenhuma plantaçao encontrada", color=ft.colors.BLACK)],alignment=ft.MainAxisAlignment.CENTER))]
            
        plantacoes = ft.Container(
            expand=True,
            bgcolor="#FFFFFF",
            border_radius=16,
            padding=ft.padding.only(left=15, right=15),


            content=ft.Column(
                controls=[
                    ft.Text(value='Plantação', size=20, color=ft.colors.BLACK, weight=ft.FontWeight.BOLD),
                    ft.Column(
                        controls=
                        lista_plantacao,
                        spacing=6,
                        scroll=ft.ScrollMode.AUTO
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )

        return plantacoes
    
    def conteudo():
        conteudo = ft.Container(
            padding=ft.padding.only(left=10, right=10, bottom=10),
            content=ft.Column(
                controls=[
                    container(),
                    plantacoes()
                ]
            )
        )
        return conteudo

        
    
    
    Main = ft.Container(
        # width=390,
        # height=860,
        expand=True,
        bgcolor='#7FA677',
        padding=ft.padding.only(top=15),
        # border_radius=20,
        content=ft.Column(
            controls=[
                ft.Container(
                    appbar(),
                    alignment=ft.alignment.top_center
                ),
                ft.Container(
                    conteudo(),
                    expand=True
                    # plantacoes(),
                    # alignment=ft.alignment.center
                )
            ]
        )
    )
    
    return Main