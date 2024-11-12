import flet as ft
import time
import pyodbc
from app.components.classes import Cadastro, Fornecedor, GerenciamentoBanco, Detalhes
from app.components.dialogs import ConfirmationDialog

# Função principal que configura a interface da página de administração de fornecedores.
def AdminFornecedores(page: ft.Page):
    # page.theme = ft.Theme(color_scheme_seed="white")

    # Função que cria um contêiner para exibir o horário e a data.
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
    
    # Função que cria um contêiner para exibir o logotipo da aplicação.
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

    # Função que cria a barra superior da aplicação com opções de navegação e logout.   
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

    # Função para criar os botões de navegação na tela do administrador.     
    def botoes():
        botoes = ft.Container(
            bgcolor="#D9FFBA",
            
            content = ft.Column(
    controls=[
        ft.Row(
            controls=[
                # Primeiro botão: Clientes
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
                # Segundo botão: Funcionários
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
                # Terceiro botão: Fornecedores
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
            expand=True,
            
            content=ft.Column(
                controls=[
                    # Define os controles (conteúdos) dentro da AppBar.
                    ft.Container(
                        expand=True,
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

    
    def fornecedor(id_fornecedor, nome, cnpj):
        # Cria um objeto de detalhes (presumivelmente, para exibir mais informações sobre o fornecedor)
        detalhes = Detalhes(page)

        # Cria o contêiner que vai representar o fornecedor.    
        fornecedor = ft.Container(
            bgcolor="#99C2A2",
            border=ft.border.all(color=ft.colors.BLACK),
            height=50,
            border_radius=9,
            padding=ft.padding.only(left=12, right=12),
            on_click=lambda e: detalhes.detalhes_fornecedor(id_fornecedor),
            
            content=ft.Row(
                controls=[
                    ft.Icon(
                        name=ft.icons.FOREST,
                        color=ft.colors.BLACK,
                        size=30
                        ),
                    ft.Text(
                        value=f"ID: {id_fornecedor}"
                        ),
                    
                    ft.Text(
                        value=nome
                        ),
                    ft.Text(
                        value=cnpj
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            )
        )
        
        return fornecedor

    # Instancia o objeto de gerenciamento de banco de dados
    def container():
        banco = Fornecedor()
        fornecedores = banco.obter_fornecedores()
        # Verifica se há fornecedores. Se houver, cria a lista de fornecedores com base nas informações do banco
        if fornecedores:
            lista_fornecedores = [fornecedor(id_fornecedor, nome, cnpj) for id_fornecedor, nome, cnpj in fornecedores]
        else:
            # Caso não haja fornecedores, cria um contêiner informando que não há fornecedores
            lista_fornecedores = [ft.Container(expand=True, content=ft.Row(controls=[ft.Text(value="Nenhum fornecedor encontrado", color=ft.colors.BLACK)],alignment=ft.MainAxisAlignment.CENTER) )]

        # Cria o objeto de cadastro (presumivelmente, para adicionar novos fornecedores)
        cadastro = Cadastro(page)
        container = ft.Container(
            width=page.window.width,
            bgcolor='#D9D9D9',
            padding=ft.padding.all(15),
            border_radius=20,
            expand=True,

            content=ft.Column(
                controls=[
                    ft.Text(value="Fornecedores"),
                    ft.Container(
                        expand=True,
                        bgcolor=ft.colors.WHITE,
                        border_radius=12,
                        padding=ft.padding.all(20),
                        content=ft.Column(
                            controls=
                            lista_fornecedores,
                            spacing=6,
                            scroll=ft.ScrollMode.AUTO
                        ),
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
                                    on_click=lambda e: cadastro.abrir_cadastro("fornecedor")
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

    # Cria o contêiner principal da página, com padding e expansão       
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
            )
        )

        return conteudo

    # Criação do contêiner principal da página
    Main = ft.Container(
        bgcolor=ft.colors.WHITE,
        expand=True,
        padding=ft.padding.all(0),

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