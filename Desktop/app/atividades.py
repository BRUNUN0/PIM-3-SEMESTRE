import colorsys
import flet as ft
import datetime
from app.components.gerenciamento_banco import Cadastro, GerenciamentoBanco
from app.components.dialogs import DialogoSaida, ConfirmationDialog
from app.components.atividade import Atividade
from app.components.detalhes import Detalhes


def Atividades(page: ft.Page):
    page.title = "Atividades"


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
                src="https://github.com/BRUNUN0/PIM-3-SEMESTRE/blob/b1af43c3defbc2696df0e40dc2520914365e6c97/Mobile/app/assets/Logo.png?raw=True",
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
                ft.TextButton('Não', on_click=lambda e: confirmation_dialog.close_dialog()),
                ft.TextButton('Sim', on_click=lambda e: go_adm())
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
    
    def atividade(id_atividade, nome, data):
        banco = GerenciamentoBanco
        detalhes = Detalhes(page, banco)
            
        atividade = ft.Container(
            bgcolor="#99C2A2",
            border=ft.border.all(color=ft.colors.BLACK),
            height=50,
            border_radius=9,
            padding=ft.padding.only(left=12, right=12),
            on_click=lambda e: detalhes.detalhes_atividade(id_atividade),
            
            content=ft.Row(
                controls=[
                    ft.Icon(
                        name=ft.icons.TASK_ALT,
                        color=ft.colors.BLACK,
                        size=30
                        ),
                    ft.Text(
                        value=f"ID: {id_atividade}",
                        color=ft.colors.BLACK
                        ),
                    
                    ft.Text(
                        value=nome,
                        color=ft.colors.BLACK
                        ),
                    ft.Text(
                        value=data,
                        color=ft.colors.BLACK
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            )
        )
        
        return atividade
    
    def container():
        banco = GerenciamentoBanco()
        banco_atividades = Atividade(banco)
        atividades = banco_atividades.obter_atividades()
        if atividades:
            lista_atividades = [atividade(id_atividade, nome, data) for id_atividade, nome, data in atividades]
        else:
            lista_atividades = [ft.Container(expand=True, content=ft.Row(controls=[ft.Text(value="Nenhuma atividade encontrada", color=ft.colors.BLACK)],alignment=ft.MainAxisAlignment.CENTER))]

        cadastro = Cadastro(page)
        container = ft.Container(
            bgcolor='#D9D9D9',
            padding=ft.padding.only(left=15, right=15, top=15, bottom=5),
            border_radius=20,
            expand=True,

            content=ft.Column(
                controls=[
                    ft.Text(
                        value="Atividades", color=ft.colors.BLACK),
                    ft.Container(
                        expand=True,
                        bgcolor=ft.colors.WHITE,
                        border_radius=12,
                        padding=ft.padding.all(20),
                        content=ft.Column(
                            controls=
                            lista_atividades,
                            spacing=6,
                            scroll=ft.ScrollMode.AUTO
                        )
                    ),
                    ft.Container(
                        padding=ft.padding.only(left=50, right=50),

                        content=ft.Row(
                            controls=[
                                ft.ElevatedButton(
                                    text='Registrar Atividade',
                                    color=ft.colors.WHITE,
                                    height=40,
                                    bgcolor=ft.colors.GREEN_900,
                                    on_click=lambda e: cadastro.abrir_registro('atividade')
                                )
                            ],
                            alignment=ft.MainAxisAlignment.END
                        )

                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )

        )

        return container
            
    def conteudo():
        conteudo = ft.Container(
            padding=ft.padding.only(left=25, right=25, top=0, bottom=0),
            expand=True,
            content=ft.ResponsiveRow(
                controls=[
                    ft.Column(
                        controls=[
                            container()
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                ],
                # alignment=ft.MainAxisAlignment.CENTER,
            )
        )

        return conteudo

    Main = ft.Container(
        expand=True,
        padding=ft.padding.all(0),
        bgcolor=ft.colors.WHITE,

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