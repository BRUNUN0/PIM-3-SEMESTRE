import flet as ft
import sqlite3
import pyodbc

def Home(page: ft.Page):
    
    def gerenciamento_banco():
        def conectar():
        # Função para conectar ao banco de dados SQL Server
            conn = pyodbc.connect(
                'Driver=ODBC Driver 17 for SQL Server;'
                'Server=BRUNO-NOTE\SQLEXPRESS;'
                'Database=teste;'
                'Trusted_Connection=yes;'
            )
            return conn
        
        def obter_plantas():
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute('SELECT Nome, URL FROM Materia_Prima')
            plantas = cursor.fetchall()
            conn.close()
            return plantas
        
        return obter_plantas()
    

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
    
    def bar():
        def dialog_perfil(e):
            
            def fechar(dialog):
                dialog.open = False
                page.update()
                
            dialog = ft.AlertDialog(
                title=ft.Text(f"Detalhes do Perfil"),
                content=ft.Container(
                    height=300,
                    bgcolor=ft.colors.BLUE,
                    content=ft.Column(
                    controls=[
                        ft.Text("É com vc Isaque", size=16),
                    ],
                    spacing=6,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    )
                ),
                    
                actions=[
                    ft.TextButton("Fechar", on_click=lambda e: fechar(dialog))
                ],
                actions_alignment=ft.alignment.center_right
            )
            page.overlay.append(dialog)
            dialog.open = True
            page.update()
            
            
        appbar = ft.Container(
            # bgcolor=ft.colors.WHITE,
            width=390,
            height=50,
            padding=ft.padding.only(top=0 ,right=10, left=10),
            theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.BLACK)),
            content=ft.Row(
                controls=[
                    logo(), # Chama a logo dentro da row
                    
                    # Adiciona o menu de opções
                    ft.PopupMenuButton(
                        icon = ft.icons.MENU,
                        icon_color=ft.colors.BLACK,
                        icon_size=40,
                        menu_position=ft.PopupMenuPosition.UNDER,
                        
                        # Items do menu
                        items=[
                            ft.PopupMenuItem(
                                icon=ft.icons.DESCRIPTION,
                                text='Meus dados',
                                on_click=lambda e: dialog_perfil
                                ),
                            ft.PopupMenuItem(
                                icon=ft.icons.LOGOUT,
                                text='Sair'
                                )
                        ]
                    )
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            )
        )
        
        return appbar
    
    def clima():
        clima = ft.Container(
            bgcolor=ft.colors.WHITE,
            width=360,
            height=160,
            border_radius=16,
            padding=ft.padding.only(top=5,left=10),
            
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Container(
                                width=100,
                                height=100,
                                bgcolor=ft.colors.BLUE,
                            ),
                            ft.Container(
                                width=100,
                                height=100,
                                bgcolor=ft.colors.RED
                            ),
                            ft.Container(
                                width=100,
                                height=100,
                                bgcolor=ft.colors.GREEN
                            )
                        ]
                    )
                ]
            )
        )
        
        return clima
    
    
    def planta(nome, imagem):
        def on_click_container(e):
            
            def fechar(dialog):
                dialog.open = False
                page.update()
                
            dialog = ft.AlertDialog(
                title=ft.Text(f"Detalhes do Plantio"),
                content=ft.Container(
                    height=300,
                    bgcolor=ft.colors.BLUE,
                    content=ft.Column(
                    controls=[
                        ft.Text("ID Plantio:", size=16),
                        ft.Container(
                            content=ft.Text(f'#ID PLANTIO', size=16),
                            bgcolor='#D9D9D9',
                            border_radius=20,
                            alignment=ft.alignment.center,
                            width=150                        ),
                        ft.Text("Item final", size=16),
                        ft.Container(
                            content=ft.Text('#VALOR NOME'),
                            bgcolor='#D9D9D9',
                            border_radius=20,
                            alignment=ft.alignment.center,
                            width=150
                        ),
                        ft.Text("Data de Início", size=16),
                        ft.Container(
                            content=ft.Text('#VALOR DATA'),
                            bgcolor='#D9D9D9',
                            border_radius=20,
                            alignment=ft.alignment.center,
                            width=150
                        ),
                        ft.Text('Quantidade', size=16),
                        ft.Container(
                            content=ft.Text('#VALOR QUANTIDADE'),
                            bgcolor='#D9D9D9',
                            border_radius=20,
                            alignment=ft.alignment.center,
                            width=150
                        ),
                        ft.Text('Fase Atual', size=16),
                        ft.Container(
                            content=ft.Text('#VALOR FASE_ATUAL'),
                            bgcolor='#D9D9D9',
                            border_radius=20,
                            alignment=ft.alignment.center,
                            width=150
                        )
                    ],
                    spacing=6,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    )
                ),
                    
                actions=[
                    ft.TextButton("Fechar", on_click=lambda e: fechar(dialog))
                ],
                actions_alignment=ft.alignment.center_right
            )
            page.overlay.append(dialog)
            dialog.open = True
            page.update()
            
            
            
        planta = ft.Container(
            bgcolor="#99C2A2",
            border=ft.border.all(
                color=ft.colors.BLACK
            ),
            width=340,
            height=50,
            border_radius=9,
            padding=ft.padding.only(left=12, right=12),
            on_click=on_click_container, # -------------------------------------- AQUI CHAMA A FUNÇÃO DO BOTÃO      ATT.BRUNO
            
            content=ft.Row(
                controls=[
                    ft.Icon(
                        name=ft.icons.FOREST,
                        color=ft.colors.BLACK,
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
                # scroll='auto',
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            )
        )
        
        return planta
    
    def plantacao():
        
        # conn = sqlite3.connect('PIXFARM.db')
        # cursor = conn.cursor()
        # cursor.execute('SELECT nome_planta, imagem FROM producao')
        # plantas = cursor.fetchall()
        # conn.close()
        plantas = gerenciamento_banco()
        lista_plantas = [planta(nome, imagem) for nome, imagem in plantas]
        
        plantacao = ft.Container(
            bgcolor=ft.colors.WHITE,
            width=360,
            height=380,
            border_radius=16,
            padding=ft.padding.only(top=5),
            
            content=ft.Column(
                controls=[
                    ft.Text(value="Plantação", size=16),
                    ft.Column(
                        controls=
                        lista_plantas,
                        spacing=6,
                        scroll='auto'
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
        
        return plantacao
    
    
    
    Main = ft.Container(
        # width=390,
        # height=860,
        expand=True,
        bgcolor='#7FA677',
        border_radius=20,
        
        content=ft.Column(
            controls=[
                ft.Container(
                    padding=ft.padding.only(top=20),
                    content=ft.Stack(
                        controls=[
                            bar()
                        ]
                    )
                ),
                ft.Container(
                    padding=ft.padding.only(top=5),
                    content=ft.Stack(
                        controls=[
                            clima()
                        ]
                    )
                ),
                ft.Container(
                    padding=ft.padding.only(top=5),
                    content=ft.Stack(
                        controls=[
                            plantacao()    
                        ]
                    )
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )
    
    return Main