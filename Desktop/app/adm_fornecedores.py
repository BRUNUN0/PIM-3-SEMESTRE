import flet as ft
import time
import pyodbc
from app.components.classes import Cadastro, GerenciamentoBanco
from app.components.dialogs import ConfirmationDialog


def AdminFornecedores(page: ft.Page):

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
        def go_home(e):
            page.go('/')
            confirmation_dialog.close_dialog()

        def sair(e):
            confirmation_dialog.open_dialog()

        confirmation_dialog = ConfirmationDialog(
            "Deseja sair de administrador?",
            "Escolha se deseja ir para tela inicial ou sair",
            [
                ft.TextButton('Cancelar', on_click=lambda e: confirmation_dialog.close_dialog()),
                ft.TextButton('Pagina Inicial', on_click=go_home)
            ],
            page
        )

        app_sup = ft.Container(
            content=ft.Row(
                controls=[
                    relogio(),
                    logo(),
                    ft.IconButton(
                        icon=ft.icons.LOGOUT,
                        icon_color=ft.colors.BLACK,
                        on_click=sair
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
                                on_click=lambda e: page.go("/adm/clientes"),
                                icon_color = ft.colors.with_opacity(0.5, ft.colors.BLACK),
                            ),
                            ft.Text(
                                value='Clientes',
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
                                icon=ft.icons.PERSON,
                                icon_size=32,
                                on_click=lambda e: page.go('/adm/funcionarios'),
                                icon_color = ft.colors.with_opacity(0.5, ft.colors.BLACK), 
                            ),
                            ft.Text(
                                value='Funcionários',
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
                                icon=ft.icons.CONTENT_PASTE_SEARCH,
                                icon_size=32,
                                on_click=lambda e: page.go('/adm/fornecedores'),
                                icon_color = ft.colors.with_opacity(0.5, ft.colors.BLACK), 
                            ),
                            ft.Text(
                                value='Fornecedores',
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
    
    def lista():
        lista = ft.ListView(
            expand=True,
            controls=[ft.Text(f'Item {i}') for i in range (100)],
            first_item_prototype=False
        )
        
        return lista
    
    def fornecedor(id_fornecedor, nome, cnpj):
            
        fornecedor = ft.Container(
            bgcolor="#99C2A2",
            border=ft.border.all(
                color=ft.colors.BLACK
            ),
            # width=340,
            height=50,
            border_radius=9,
            padding=ft.padding.only(left=12, right=12),
            
            content=ft.Row(
                controls=[
                    ft.Icon(
                        name=ft.icons.FOREST,
                        color=ft.colors.BLACK,
                        size=30
                        ),
                    ft.Text(
                        value=id_fornecedor
                        ),
                    
                    ft.Text(
                        value=nome
                        ),
                    ft.Text(
                        value=cnpj
                    )
                ],
                # scroll='auto',
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            )
        )
        
        return fornecedor

    def container():
        banco = GerenciamentoBanco()
        fornecedores = banco.obter_fornecedores()
        if fornecedores is None:
            print('Erro aqui')
        lista_fornecedores = [fornecedor(id_fornecedor, nome, cnpj) for id_fornecedor, nome, cnpj in fornecedores]

        cadastro = Cadastro(page)
        container = ft.Container(
            width=page.window.width,
            # height=150,
            bgcolor='#D9D9D9',
            padding=ft.padding.only(left=15, right=15, top=15, bottom=5),
            border_radius=20,
            expand=True,

            content=ft.Column(
                controls=[
                    ft.Container(
                        expand=True,
                        bgcolor=ft.colors.WHITE,
                        border_radius=12,
                        content=ft.Column(
                            controls=
                            lista_fornecedores,
                            spacing=6
                        )
                    ),
                    ft.Container(
                        padding=ft.padding.only(left=50, right=50),

                        content=ft.Row(
                            controls=[
                                ft.ElevatedButton(
                                    text='Cadastrar',
                                    color=ft.colors.WHITE,
                                    width=120,
                                    height=40,
                                    bgcolor=ft.colors.GREEN_900,
                                    on_click=lambda e: cadastro.abrir_dialog("fornecedor")
                                )
                            ],
                            alignment=ft.MainAxisAlignment.END
                        )

                    )
                ]
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