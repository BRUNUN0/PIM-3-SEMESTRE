import flet as ft
from datetime import datetime
import pyodbc
from app.components.dialogs import DialogoSaida
from app.components.classes import GerenciamentoBanco, Detalhes, Cadastro


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

    def materia(id, nome, quantidade, url):       
        materia_prima = ft.Container(
            bgcolor="#99C2A2",
            border=ft.border.all(
                color=ft.colors.BLACK
            ),
            width=340,
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
                    ),
                    ft.Container(
                        alignment=ft.alignment.center_right,
                        
                        content=ft.Image(
                            src=url,
                            width=30,
                        )
                    )
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            )
        )
        
        return materia_prima
    
    def materias_primas ():

        banco = GerenciamentoBanco()
        materia_prima_data = banco.obter_materia_prima()
        if materia_prima_data:
            lista_materias_primas = [materia(id, nome, quantidade, url) for id, nome, quantidade, url in materia_prima_data]
        else:
            lista_materias_primas = [ft.Container(expand=True, content=ft.Row(controls=[ft.Text(value="Nenhuma materia prima encontrada", color=ft.colors.BLACK)],alignment=ft.MainAxisAlignment.CENTER))]
        estoque_mater_prima = ft.Container(
            width= 350,
            bgcolor='#D6D6D6',
            border_radius=16,
            padding=ft.padding.all(15),

            content=ft.Column(
                controls=[
                    ft.Text(value='Estoque Materia Prima', size=20, color=ft.colors.BLACK, weight=ft.FontWeight.BOLD),
                    ft.Column(
                        controls=
                        lista_materias_primas,
                        spacing=6,
                        scroll=ft.ScrollMode.AUTO
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
        return estoque_mater_prima

    def plantacao(id_plantio, plantio, nome, quantidade):
        detalhes = Detalhes(page)
        produto = ft.Container(
            bgcolor="#99C2A2",
            border=ft.border.all(color=ft.colors.BLACK),
            width=340,
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
        producoes = banco.obter_producao()
        if producoes:
            lista_plantacao = [plantacao(id_plantio, plantio, nome, quantidade) for id_plantio, plantio, nome, quantidade, *rest in producoes]
        else:
            lista_plantacao = [ft.Container(expand=True, content=ft.Row(controls=[ft.Text(value="Nenhuma plantaçao encontrada", color=ft.colors.BLACK)],alignment=ft.MainAxisAlignment.CENTER))]
            
        plantacoes = ft.Container(
            width=350,
            bgcolor="#D6D6D6",
            border_radius=16,
            padding=ft.padding.all(15),


            content=ft.Column(
                controls=[
                    ft.Text(value='Itens Plantados', size=20, color=ft.colors.BLACK, weight=ft.FontWeight.BOLD),
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

    def grupo():

        def produto(id, nome, quantidade):
            plantados = ft.Container(
                bgcolor="#99C2A2",
                border=ft.border.all(color=ft.colors.BLACK),
                height=30,
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
        produtos = banco.obter_produtos()
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
                        padding=ft.padding.all(15),
                        content=ft.Column(
                            controls=[
                                ft.Text(value='Estoque Produtos', size=20, color=ft.colors.BLACK, weight=ft.FontWeight.BOLD),
                                ft.Column(
                                    controls=
                                    lista_produtos,
                                    spacing=6,
                                    scroll=ft.ScrollMode.AUTO
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
                            ft.ElevatedButton("Registrar Recebimento", expand=True, bgcolor="#13330D", color=ft.colors.WHITE, on_click=lambda e: cadastro.abrir_cadastro("materia prima")),
                            ft.ElevatedButton("Iniciar Nova Produção", expand=True, bgcolor="#13330D", color=ft.colors.WHITE, on_click=lambda e: cadastro.abrir_registro("iniciar producao")),                            ft.ElevatedButton("Finalizar Produção", expand=True, bgcolor="#13330D", color=ft.colors.WHITE, on_click=lambda e: cadastro.abrir_registro("finalizar producao")),
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
            padding=ft.padding.only(left=25,),
            content=ft.ResponsiveRow(
                controls=[
                    ft.Row(
                        controls=[
                            materias_primas(),
                            plantacoes(),
                            grupo()
                        ]
                    )
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
    
    # page.on_resized = page.update()

    return Main