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
    
    def fechar_conexao(self):
        if self.conn:
            self.conn.close()



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









