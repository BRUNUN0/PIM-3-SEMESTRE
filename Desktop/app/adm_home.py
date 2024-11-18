from click import style
import flet as ft
import datetime
import pyodbc
from app.components.dialogs import ConfirmationDialog
from app.components.classes import GerenciamentoBanco, Cadastro
from app.components.estoque import Estoque



def AdminHome(page: ft.Page):

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

    # Dados para o gráfico, incluindo mês, valor e cor de cada barra
    def grafico_plantas():
        dados = [
            ("Dez", 100, ft.colors.YELLOW),
            ("Nov", 90, ft.colors.GREEN),
            ("Out", 85, ft.colors.GREEN),
            ("Set", 75, ft.colors.GREEN),
            ("Ago", 65, ft.colors.BLUE),
            ("Jul", 55, ft.colors.BLUE),
            ("Jun", 45, ft.colors.BLUE),
            ("Mai", 35, ft.colors.BLUE),
            ("Abr", 25, ft.colors.RED),
            ("Mar", 20, ft.colors.RED),
            ("Fev", 15, ft.colors.RED),
            ("Jan", 10, ft.colors.RED)
        ]

        # Criação das barras do gráfico com base nos dados.
        barras = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text(label, color=ft.colors.BLACK, width=50),
                        ft.Container(
                            width=valor * 2,
                            height=20,
                            bgcolor=cor,
                        ),
                        ft.Text(f"{valor}%", width=40)
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    spacing=10
                )
                for label, valor, cor, in dados
            ],
            spacing=5
        )

        # Criação do contêiner do gráfico que vai conter as barras
        grafico = ft.Container(
            width=350,
            # height=500,
            bgcolor='#D6D6D6',
            border_radius=16,
            padding=ft.padding.only(bottom=15),

            content=ft.Column(
                controls=[
                    ft.Text(value='COLUMN', size=20, weight=ft.FontWeight.BOLD),
                    ft.Container(
                        barras
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
        return grafico
    
    def pedidos ():
        # Instancia o objeto de gerenciamento de banco para acessar dados
        # banco = GerenciamentoBanco()
        # plantas = banco.obter_pedidos()
        # # Verifica se existem plantas no banco de dados
        # if plantas:
        #     # Se houver plantas, cria uma lista de contêineres para cada planta
        #     lista_plantas = [planta(nome, imagem) for nome, imagem in plantas]
        # else:
        #     # Se não houver plantas, exibe uma mensagem dizendo que nenhum pedido foi encontrado
        #     lista_plantas = [ft.Container(expand=True, content=ft.Row(controls=[ft.Text(value="Nenhum pedido encontrado")], alignment=ft.MainAxisAlignment.CENTER))]

        estoque_mater_prima = ft.Container(
            width= 350,
            bgcolor='#D6D6D6',
            border_radius=16,
            padding=ft.padding.only(bottom=15),
            content=ft.Column(
                controls=[
                    ft.Text(value='Estoque Materia Prima', size=20, color=ft.colors.BLACK, weight=ft.FontWeight.BOLD),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
        return estoque_mater_prima

    def grupo():

        def produto(id, nome, quantidade):
            plantados = ft.Container(
                bgcolor="#99C2A2",
                border=ft.border.all(color=ft.colors.BLACK),
                # width=340,
                height=50,
                border_radius=9,
                padding=ft.padding.only(left=12, right=12),
                content=ft.Row(
                    controls=[
                        ft.Text(
                            value=f"ID: {id}",
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
            return plantados

        cadastro = Cadastro(page)
        banco = GerenciamentoBanco()
        produtos = Estoque(banco)
        produtos = produtos.obter_produtos()
        if produtos:
            lista_produtos = [produto(id, nome, quantidade) for id, nome, quantidade, _ in produtos]
        else:
            lista_produtos = [ft.Container(expand=True, content=ft.Row(controls=[ft.Text(value="Nenhum produto encontrado", color=ft.colors.BLACK)],alignment=ft.MainAxisAlignment.CENTER))]

        grupo = ft.Container(
            expand=True,
            padding=ft.padding.only(left=15, right=15, bottom=15),
            content=ft.Column(
                controls=[
                    ft.Container(
                        expand=True,
                        width=750,
                        bgcolor="#D6D6D6",
                        border_radius=16,
                        padding=ft.padding.only(left=15, right=15),
                        content=ft.Column(
                            controls=[
                                ft.Text(value='Estoque Produtos', size=20, color=ft.colors.BLACK, weight=ft.FontWeight.BOLD),
                                ft.Container(
                                    content=
                                    ft.Column(
                                        controls=
                                        lista_produtos,
                                        spacing=6,
                                        scroll=ft.ScrollMode.AUTO
                                    ),
                                    expand=True,
                                    height=200
                                )
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        )
                    ),
                    ft.Row(
                        height=100,
                        spacing=10,
                        controls=[
                            ft.Container(
                                expand=True,
                                bgcolor="#D9FFBA",
                                border_radius=16,
                                content=ft.Column(
                                    controls=[
                                        ft.Text(value='Valor', color=ft.colors.BLACK)
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                                )
                            ),
                            ft.Container(
                                expand=True,
                                bgcolor="#D9FFBA",
                                border_radius=16,
                                content=ft.Column(
                                    controls=[
                                        ft.Text(value='Valor', color=ft.colors.BLACK)
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                                )
                            )
                        ]
                    ),
                    ft.Row(
                        height=100,
                        spacing=10,
                        controls=[
                            ft.Container(
                                expand=True,
                                bgcolor="#D9FFBA",
                                border_radius=16,
                                content=ft.Column(
                                    controls=[
                                        ft.Text(value='Valor', color=ft.colors.BLACK)
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                                )
                            ),
                            ft.Container(
                                expand=True,
                                bgcolor="#D9FFBA",
                                border_radius=16,
                                content=ft.Column(
                                    controls=[
                                        ft.Text(value='Valor', color=ft.colors.BLACK)
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                                )
                            )
                        ]
                    ),
                    ft.Row(
                        height=50,
                        spacing=10,
                        controls=[
                            ft.ElevatedButton("Novo Produto", expand=True, bgcolor="#13330D", color=ft.colors.WHITE, on_click=lambda e: cadastro.abrir_cadastro("novo produto")),
                            # ft.ElevatedButton("Iniciar Nova Produção", expand=True, bgcolor="#13330D", color=ft.colors.WHITE, on_click=lambda e: cadastro.abrir_registro("iniciar producao")),
                            # ft.ElevatedButton("Finalizar Produção", expand=True, bgcolor="#13330D", color=ft.colors.WHITE, on_click=lambda e: cadastro.abrir_registro("finalizar producao")),
                        ],
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )

        )
        return grupo

    def conteudo():
        conteudo = ft.Container(
            padding=ft.padding.only(left=15, bottom=15),
            content=ft.ResponsiveRow(
                controls=[
                    ft.Row(
                        controls=[
                            grafico_plantas(),
                            pedidos(),
                            grupo()
                        ]
                    ),
                ],
                
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