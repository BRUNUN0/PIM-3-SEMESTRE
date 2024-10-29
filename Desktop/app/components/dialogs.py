import pyodbc
import flet as ft

class BancoGerenciamento:
    def __init__(self, server, database, driver='ODBC Driver 17 for SQL Server'):
        self.server = server
        self.database = database
        self.driver = driver
        self.conn = None

    def conectar(self):
        # Conecta ao banco de dados usando as configurações fornecidas
        self.conn = pyodbc.connect(
            f'Driver={self.driver};'
            f'Server={self.server};'
            f'Database={self.database};'
            'Trusted_Connection=yes;'
        )
        return self.conn

    def obter_plantas(self):
        # Obtém os dados das plantas no banco
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT Nome, URL FROM Materia_Prima')
        plantas = cursor.fetchall()
        conn.close()
        return plantas

class Planta:
    def __init__(self, nome, imagem, page):
        self.nome = nome
        self.imagem = imagem
        self.page = page

    def detalhes_planta(self, e):
        # Mostra o diálogo com detalhes da planta
        detalhes = DetalhesPlantio()  # Assumindo que DetalhesPlantio já está definida
        dialog = detalhes.mostrar_detalhes(self.page)

    def exibir_planta(self):
        # Cria e retorna um container para exibir a planta
        planta = ft.Container(
            bgcolor="#99C2A2",
            border=ft.border.all(color=ft.colors.BLACK),
            width=340,
            height=50,
            border_radius=9,
            padding=ft.padding.only(left=12, right=12),
            on_click=self.detalhes_planta,
            content=ft.Row(
                controls=[
                    ft.Icon(name=ft.icons.FOREST, color=ft.colors.BLACK, size=30),
                    ft.Text(value=self.nome),
                    ft.Container(
                        alignment=ft.alignment.center_right,
                        content=ft.Image(src=self.imagem, width=30),
                    )
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            )
        )
        return planta



# CLASSE PARA CRIAÇÃO DE DIALOGS DE SAIDA
class ConfirmationDialog:
    def __init__(self, title, content, actions, page):
        self.title = title
        self.content = content
        self.actions = actions
        self.page = page
        self.dialog = None

    def create_dialog(self):
        # Cria o diálogo com as ações especificadas
        self.dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text(self.title),
            content=ft.Text(self.content),
            actions=self.actions,  # Usa as ações definidas
            actions_alignment='center'
        )

    def open_dialog(self):
        # Abre o diálogo com as ações fornecidas
        if self.dialog is None:
            self.create_dialog()
        self.page.overlay.append(self.dialog)
        self.dialog.open = True
        self.page.update()

    def close_dialog(self, e=None):
        # Fecha o diálogo
        if self.dialog:
            self.dialog.open = False
            self.page.update()


class DialogoSaida(ConfirmationDialog):
    def __init__(self, page):
        # Define o título e o conteúdo do diálogo de saída, e as ações específicas para ele
        super().__init__("Deseja sair?", "Escolha uma das opções abaixo:", [], page)

    def abrir(self):
        # Abre o diálogo de confirmação de saída com duas opções
        sair_button = ft.TextButton("Sair", on_click=self.sair)
        cancelar_button = ft.TextButton("Cancelar", on_click=self.close_dialog)
        
        self.actions = [cancelar_button, sair_button]  # Define as ações
        self.open_dialog()

    def sair(self, e=None):
        # Realiza o logoff e redireciona para a tela de login
        self.page.go('/login')  # Ajuste o redirecionamento se necessário
        self.close_dialog()













class DetalhesPlantio:
    def __init__(self, id_plantio="ID PLANTIO", item_final="#VALOR NOME", data_inicio="#VALOR DATA", quantidade="#VALOR QUANTIDADE", fase_atual="#VALOR FASE_ATUAL", page=None):
        self.id_plantio = id_plantio
        self.item_final = item_final
        self.data_inicio = data_inicio
        self.quantidade = quantidade
        self.fase_atual = fase_atual
        self.page = page  # Opcional, se você não passar page no construtor

    def mostrar_detalhes(self):
        dialog = ft.AlertDialog(
            title=ft.Text(f"Detalhes do Plantio"),
            content=ft.Column(
                controls=[
                    ft.Text("ID Plantio:", size=16),
                    ft.Container(
                        content=ft.Text(self.id_plantio, size=16),
                        bgcolor='#D9D9D9',
                        border_radius=20,
                        alignment=ft.alignment.center,
                        width=150
                    ),
                    ft.Text("Item final", size=16),
                    ft.Container(
                        content=ft.Text(self.item_final, size=16),
                        bgcolor='#D9D9D9',
                        border_radius=20,
                        alignment=ft.alignment.center,
                        width=150
                    ),
                    ft.Text("Data inicio", size=16),
                    ft.Container(
                        content=ft.Text(self.data_inicio, size=16),
                        bgcolor='#D9D9D9',
                        border_radius=20,
                        alignment=ft.alignment.center,
                        width=150
                    ),
                    ft.Text("Quantidade", size=16),
                    ft.Container(
                        content=ft.Text(self.quantidade, size=16),
                        bgcolor='#D9D9D9',
                        border_radius=20,
                        alignment=ft.alignment.center,
                        width=150
                    ),
                    ft.Text("Fase atual", size=16),
                    ft.Container(
                        content=ft.Text(self.fase_atual, size=16),
                        bgcolor='#D9D9D9',
                        border_radius=20,
                        alignment=ft.alignment.center,
                        width=150
                    ),
                ],
                spacing=6,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            actions=[
                ft.TextButton("Fechar", on_click=lambda e: self.fechar_dialog())
            ],
            actions_alignment=ft.alignment.center_right
        )
        

        def fechar_dialog(self):
            self.dialog.open = False  # Assumindo que você atribui dialog a self.dialog dentro de mostrar_detalhes
            self.page.update()  # Assumindo que você passou page como argumento ou tem ele definido em outro lugar

        self.dialog = dialog  # Assumindo que você quer acessar a instância do diálogo mais tarde (opcional)
        self.page.overlay.append(dialog)
        self.dialog.open = True
        self.page.update()