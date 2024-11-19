import flet as ft
import datetime
from app.components.dialogs import ConfirmationDialog, DialogoSaida, Detalhes
from app.components.gerenciamento_banco import GerenciamentoBanco
from app.components.producao import Producao
from app.components.detalhes import Detalhes


def Home(page: ft.Page):
    page.title = "Home"
    
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
                # src="https://github.com/BRUNUN0/PIM-3-SEMESTRE/blob/b1af43c3defbc2696df0e40dc2520914365e6c97/Mobile/app/assets/Logo.png?raw=True",
                # src = "https://ibb.co/8x9fQ4W",
                src = "app/assets/Logo.png",
                width=50,
                height=50,
            ),
            alignment=ft.alignment.top_center,
        )
        return logo
        
    def menu():
        def go_adm(e):
            page.go('/login')
            confirmation_dialog.close_dialog()
            

        def sair(e):
            confirmation_dialog.open_dialog()

        confirmation_dialog = ConfirmationDialog(
            "Deseja realmente sair?",
            " ",
            [
                ft.TextButton('Não', on_click=lambda e: confirmation_dialog.close_dialog(e)),
                ft.TextButton('Sim', on_click=lambda e: go_adm(e))
            ],
            page
        )

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
                                on_click=sair
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
            bgcolor="#D9FFBA",
            padding=ft.padding.only(top=10),
            
            content = ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            # Botão Home
                            ft.Container(
                                width=150,
                                content=ft.Column(
                                    controls=[
                                        ft.IconButton(
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
                                    alignment=ft.MainAxisAlignment.START,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                )
                            ),
                            # Botão Plantação
                            ft.Container(
                                width=150,
                                content=ft.Column(
                                    controls=[
                                        ft.IconButton(
                                            icon=ft.icons.ECO,
                                            icon_size=32,
                                            icon_color = ft.colors.with_opacity(0.5, ft.colors.BLACK),
                                            on_click=lambda e: page.go('/plantacao')
                                        ),
                                        ft.Text(
                                            value='Plantação',
                                            color= ft.colors.with_opacity(0.5, ft.colors.BLACK),
                                            size=16,
                                        )
                                    ],
                                    alignment=ft.MainAxisAlignment.START,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                )
                            ),
                            # Botão Pedidos
                            ft.Container(
                                width=150,
                                content=ft.Column(
                                    controls=[
                                        ft.IconButton(
                                            icon=ft.icons.BOOKMARK_ADD_SHARP,
                                            icon_size=32,
                                            icon_color = ft.colors.with_opacity(0.5, ft.colors.BLACK),
                                            on_click=lambda e: page.go('/pedidos')
                                        ),
                                        ft.Text(
                                            value='Pedidos',
                                            color= ft.colors.with_opacity(0.5, ft.colors.BLACK),
                                            size=16,
                                        )
                                    ],
                                    alignment=ft.MainAxisAlignment.START,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                )
                            ),
                            # Botão Atividades
                            ft.Container(
                                width=150,
                                content=ft.Column(
                                    controls=[
                                        ft.IconButton(
                                            icon=ft.icons.CHECKLIST,
                                            icon_size=32,
                                            icon_color = ft.colors.with_opacity(0.5, ft.colors.BLACK),
                                            on_click=lambda e: page.go('/atividades'),
                                        ),
                                        ft.Text(
                                            value='Atividades',
                                            color= ft.colors.with_opacity(0.5, ft.colors.BLACK),
                                            size=16,
                                        )
                                    ],
                                    alignment=ft.MainAxisAlignment.START,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                )
                            )
                        ],
                        # Centraliza todos os botões na linha
                        alignment=ft.MainAxisAlignment.CENTER,
                    )
                ]
            )
        )
        
        return botoes
    
    def AppBar():
        AppBar = ft.Container(
            bgcolor="#D9FFBA",
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

    def pproducao(id_plantio, nome, imagem):
        banco = GerenciamentoBanco()
        detalhes = Detalhes(page, banco)

        planta = ft.Container(
            bgcolor="#99C2A2",
            border=ft.border.all(
                color=ft.colors.BLACK
            ),
            height=50,
            border_radius=9,
            padding=ft.padding.only(left=12, right=12),
            on_click=lambda e: detalhes.detalhes_producao(id_plantio),
            
            content=ft.Row(
                controls=[
                    ft.Icon(
                        name=ft.icons.FOREST,
                        color=ft.colors.BLACK,
                        size=30
                        ),
                    ft.Text(
                        value=nome,
                        color=ft.colors.BLACK
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
        banco_producao = Producao(banco)
        producoes = banco_producao.obter_producao()
        if producoes:
            lista_producao = [pproducao(id_plantio, nome, imagem) for  id_plantio, _, nome, _, imagem in producoes]
        else:
            lista_producao = [ft.Container(expand=True, content=ft.Row(controls=[ft.Text(value="Nenhuma produção em andamento", color=ft.colors.BLACK)],alignment=ft.MainAxisAlignment.CENTER) )]

        producao = ft.Container(
            width=350,
            bgcolor='#D6D6D6',
            padding=ft.padding.only(left=10, right=10),
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

    def grafico_pedidos():
        banco = GerenciamentoBanco()
        grafico = Producao(banco)
        dados_grafico = grafico.grafico_qnt_prod_mes()  # Retorna dados como [(mes, total_producao), ...]

        if dados_grafico:
            # Criar gráficos com base nos dados retornados
            lista_producao = [
                ft.Row(
                    controls=[
                        ft.Text(mes, color=ft.colors.BLACK, width=50),
                        ft.Container(
                            width=total_producao * 2,  # Ajuste o multiplicador para escalar a largura da barra
                            height=20,
                            bgcolor=ft.colors.BLUE if total_producao >= 50 else ft.colors.RED,
                        ),
                        ft.Text(f"{total_producao} unidades", color=ft.colors.BLACK, width=80)
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    spacing=10
                )
                for mes, total_producao in dados_grafico
            ]
        else:
            lista_producao = [
                ft.Container(
                    expand=True,
                    content=ft.Row(
                        controls=[ft.Text(value="Nenhuma produção em andamento", color=ft.colors.BLACK)],
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                )
            ]

        grafico_container = ft.Container(
            width=350,
            bgcolor='#D6D6D6',
            border_radius=16,
            padding=ft.padding.all(15),
            content=ft.Column(
                controls=[
                    ft.Text(value='Produção por Mês:', size=20, color=ft.colors.BLACK, weight=ft.FontWeight.BOLD),
                    ft.Column(
                        controls=lista_producao,
                        spacing=6,
                        scroll=ft.ScrollMode.AUTO
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
        return grafico_container



    def conteudo():
        conteudo = ft.Container(
            padding=ft.padding.only(left=25,),
            content=ft.ResponsiveRow(
                controls=[
                    ft.Row(
                        controls=[
                            em_producao(),
                            grafico_pedidos()
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