import pyodbc
import flet as ft


class Detalhes:
    def __init__(self, title, detalhes):
        """
        Inicializa o diálogo de detalhes.
        :param title: O título do diálogo.
        :param detalhes: Um dicionário com os detalhes a serem exibidos.
        """
        self.title = title
        self.detalhes = detalhes

    def exibir_dialogo(self, page):
        """
        Cria e exibe o AlertDialog com base nos detalhes fornecidos.
        :param page: A página onde o diálogo será exibido.
        """
        # Constrói o conteúdo do diálogo com base nos detalhes
        conteudo = ft.Column(
            controls=[
                ft.Text(f"{key}: {value}", size=16) for key, value in self.detalhes.items()
            ],
            spacing=6,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

        dialog = ft.AlertDialog(
            title=ft.Text(self.title),
            content=ft.Container(
                height=300,
                bgcolor=ft.colors.BLUE,
                content=conteudo
            ),
            actions=[ft.TextButton("Fechar", on_click=lambda e: self.fechar_dialogo(dialog, page))],
            actions_alignment=ft.alignment.center_right
        )

        page.overlay.append(dialog)
        dialog.open = True
        page.update()

    def fechar_dialogo(self, dialog, page):
        """
        Fecha o diálogo.
        :param dialog: O diálogo a ser fechado.
        :param page: A página onde o diálogo está sendo exibido.
        """
        dialog.open = False
        page.update()

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
            bgcolor=ft.colors.WHITE,
            modal=True,
            title=ft.Text(self.title, color=ft.colors.BLACK),
            content=ft.Text(self.content, color=ft.colors.BLACK),
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

