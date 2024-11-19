import flet as ft
import datetime
from app.components.gerenciamento_banco import Cadastro, GerenciamentoBanco
from app.components.dialogs import ConfirmationDialog
from app.components.cliente import Cliente
from app.components.detalhes import Detalhes

# Função principal que configura a interface da página de administração de clientes.
def AdminClientes(page: ft.Page):

    # Função que cria um contêiner para exibir o horário e a data.
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
    
    # Função que cria um contêiner para exibir o logotipo da aplicação.
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
    
    def icon():
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
        icon = ft.Container(
            width=200,
            content=ft.Row(
                controls=[
                    ft.IconButton(
                        icon=ft.icons.LOGOUT,
                        icon_color=ft.colors.BLACK,
                        on_click=sair,
                        # alignment=ft.alignment.center_right
                    )
                ],
                alignment=ft.MainAxisAlignment.END
            )
        )
        return icon

    # Função que cria a barra superior da aplicação com opções de navegação e logout.  
    def appbar_superior():
        app_sup = ft.Container(
            content=ft.Row(
                controls=[
                    relogio(),
                    logo(),
                    icon(),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            )
        )
        
        return app_sup

    # Função para criar os botões de navegação na tela do administrador.  
    def botoes():
        botoes = ft.Container(
            bgcolor="#D9FFBA",
            padding=ft.padding.only(top=10),
            
            content = ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            # Primeiro botão: Clientes
                            ft.Container(
                                width=150,
                                content=ft.Column(
                                    controls=[
                                        ft.IconButton(
                                            icon=ft.icons.BUSINESS_CENTER,
                                            icon_size=32,
                                            icon_color = ft.colors.with_opacity(0.5, ft.colors.BLACK),
                                            on_click=lambda e: page.go("/adm/clientes"),
                                        ),
                                        ft.Text(
                                            value='Clientes',
                                            color= ft.colors.with_opacity(0.5, ft.colors.BLACK),
                                            size=16
                                        )
                                    ],
                                    alignment=ft.MainAxisAlignment.START,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                ),
                            ),
                            # Segundo botão: Funcionários
                            ft.Container(
                                width=150,
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
                                    alignment=ft.MainAxisAlignment.START,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                ),
                            ),
                            # Terceiro botão: Fornecedores
                            ft.Container(
                                width=150,
                                content=ft.Column(
                                    controls=[
                                        ft.IconButton(
                                            icon=ft.icons.FACTORY,
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
                                    alignment=ft.MainAxisAlignment.START,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                ),
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,  # Centraliza todos os botões na linha
                        spacing=20,  # Ajusta o espaçamento entre os botões na linha
                    )
                ]
            )
        )
        
        return botoes
    
    # Função para criar a barra superior (AppBar) da página.
    def AppBar():
        AppBar = ft.Container(
            bgcolor="#D9FFBA",
            width=page.window.width,
            padding=ft.padding.all(10),
            height=175,
            expand=True,
            
            content=ft.Column(
                controls=[
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
    
    # Função que cria um contêiner para exibir informações de um cliente específico.
    def cliente(id_cliente, nome, cnpj):
        banco = GerenciamentoBanco()
        detalhes = Detalhes(page, banco)

        fornecedor = ft.Container(
            bgcolor="#99C2A2",
            border=ft.border.all(
                color=ft.colors.BLACK
            ),
            # width=340,
            height=50,
            border_radius=9,
            padding=ft.padding.only(left=12, right=12),
            on_click=lambda e: detalhes.detalhes_cliente(id_cliente),
            
            content=ft.Row(
                controls=[
                    ft.Icon(
                        name=ft.icons.PEOPLE,
                        color=ft.colors.BLACK,
                        size=30
                        ),
                    ft.Text(
                        value=f"ID: {id_cliente}",
                        color=ft.colors.BLACK,
                        width=160
                        ),
                    
                    ft.Text(
                        value=nome,
                        color=ft.colors.BLACK,
                        width=250
                        ),
                    ft.Text(
                        value=f"CNPJ: {cnpj}",
                        color=ft.colors.BLACK,
                        width=200
                    )
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            )
        )
        
        return fornecedor

    # Função que cria um contêiner principal para exibir a lista de clientes e um botão de cadastro.
    def container():
        banco = GerenciamentoBanco()
        banco_cliente = Cliente(banco)
        clientes = banco_cliente.obter_clientes()
        if clientes:
            # Se existem clientes, cria uma lista de contêineres com informações de cada cliente.
            lista_clientes = [cliente(id_cliente, nome, cnpj) for id_cliente, nome, cnpj in clientes]
        else:
            # Caso não haja clientes, exibe uma mensagem informando que nenhum cliente foi encontrado.
            lista_clientes = [ft.Container(expand=True, content=ft.Row(controls=[ft.Text(value="Nenhum cliente encontrado")],alignment=ft.MainAxisAlignment.CENTER) )]

        # Instância de Cadastro para gerenciar o diálogo de cadastro.
        cadastro = Cadastro(page)
        container = ft.Container(
            width=page.window.width,
            bgcolor='#D9D9D9',
            padding=ft.padding.all(15),
            border_radius=20,
            expand=True,

            content=ft.Column(
                controls=[
                    ft.Text(value="Clientes", color=ft.colors.BLACK),
                    # Contêiner para a lista de clientes.
                    ft.Container(
                        expand=True,
                        bgcolor=ft.colors.WHITE,
                        border_radius=12,
                        padding=ft.padding.all(15),
                        content=ft.Column(
                            controls=
                            lista_clientes,
                            spacing=6,
                            scroll=ft.ScrollMode.AUTO
                        )
                    ),
                    # Contêiner com botão para cadastrar novos clientes.
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
                                    on_click=lambda e: cadastro.abrir_cadastro('cliente')
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

    # Função que cria o contêiner principal de conteúdo para a exibição da página.        
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

    # Contêiner principal que define a estrutura e o layout da página.
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