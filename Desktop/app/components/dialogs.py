import pyodbc
import flet as ft

class GerenciamentoBanco:
    def __init__(self):
        self.conn_str = (
            'Driver=ODBC Driver 17 for SQL Server;'
            'Server=BRUNO-NOTE\\SQLEXPRESS;'
            'Database=teste;'
            'Trusted_Connection=yes;'
        )

    def conectar(self):
        # Conecta ao banco de dados
        return pyodbc.connect(self.conn_str)

    def obter_plantas(self):
        # Obtém os dados das plantas
        conn = self.conectar()
        cursor = conn.cursor()
        query = '''
            SELECT
	            Producao.Nome,
	            Materia_Prima.URL
            FROM Producao
            JOIN Materia_Prima ON Producao.fk_id_materia = Materia_Prima.id_materia
            '''
        cursor.execute(query)
        plantas = cursor.fetchall()
        conn.close()
        return plantas
    
    def obter_pedidos(self):
        # Obtém os dados dos pedidos
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT Nome, Quantidade FROM Pedidos')
        pedidos = cursor.fetchall()
        conn.close()
        return pedidos
    
    def obter_fornecedores(self):
        # Obtém os dados dos fornecedores
        conn = self.conectar()
        cursor = conn.cursor()
        query = '''

        '''
        cursor.execute(query)



class Detalhes:
    def __init__(self, titulo, conteudo, page):
        self.titulo = titulo
        self.conteudo = conteudo
        self.page = page

    def exibir(self):
        def fechar(dialog):
            dialog.open = False
            self.page.update()

        detalhes_conteudo = [
            ft.Text(key, size=16) for key in self.conteudo.keys()
        ]
        
        valores_conteudo = [
            ft.Container(
                content=ft.Text(str(value)),
                bgcolor='#D9D9D9',
                border_radius=20,
                alignment=ft.alignment.center,
                width=150,
                padding=5
            ) for value in self.conteudo.values()
        ]

        dialog = ft.AlertDialog(
            title=ft.Text(self.titulo),
            content=ft.Container(
                height=300,
                content=ft.Column(
                    controls=[
                        *detalhes_conteudo,
                        *valores_conteudo
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

        self.page.overlay.append(dialog)
        dialog.open = True
        self.page.update()


    

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









