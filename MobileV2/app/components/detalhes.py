import flet as ft
import hashlib
from app.components.producao import Producao
# from app.components.pedido import Pedido
# from app.components.atividade import Atividade
# from app.components.cliente import Cliente
# from app.components.fornecedor import Fornecedor
# from app.components.estoque import Estoque
# from app.components.funcionario import Funcionario
from app.components.gerenciamento_banco import GerenciamentoBanco
from app.components.dialogs import ConfirmationDialog

class Detalhes:
    def __init__(self, page, gerenciamento_banco:GerenciamentoBanco):
        """
        Inicializa a classe DetalhesDialog para exibir os detalhes de uma entidade.
        :param page: A página onde o dialog será mostrado.
        :param banco: Instância de GerenciamentoBanco para consultar os dados.
        """
        self.page = page
        self.dialog = None
        self.gerenciamento_banco = gerenciamento_banco
        self.botoes = None
        self.campos = {}
        self.campos_nao_editaveis = ["ID", "Nome/Razão Social", "CNPJ", "CPF", "Cargo", "Data inicial"]

    # def detalhes_pedido(self, id_pedido):
    #     self.id_pedido_atual = id_pedido

    #     banco = GerenciamentoBanco()
    #     pedido = Pedido(banco)

    #     detalhes = pedido.obter_detalhes_pedido(id_pedido)

    #     if detalhes is None:
    #         snackbar = ft.SnackBar(ft.Text("Erro ao obter detalhes do pedido."), bgcolor=ft.colors.RED)
    #         self.page.overlay.append(snackbar)
    #         snackbar.open = True
    #         self.page.update()
    #         return
        
    #     dados = {
    #         "ID": detalhes[0],
    #         "Cliente": detalhes[1],
    #         "Data do Pedido": detalhes[2],
    #         "Produto": detalhes[3],
    #         "Quantidade": detalhes[4],
    #         "Previsão de Entrega (dias)": detalhes[5],
    #         "Status": detalhes[6]
    #     }

    #     # Conteúdo do diálogo
    #     conteudo_dialog = [
    #         ft.Row(
    #             controls=[
    #                 ft.Text(f"Detalhes do Pedido", color=ft.colors.BLACK, size=18, weight="bold"),
    #                 ft.IconButton(icon=ft.icons.CLOSE, icon_color=ft.colors.BLACK, on_click=self._fechar_dialog)
    #             ],
    #             alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    #         )
    #     ]

    #     # Adicionar os campos do dicionário `dados` ao diálogo
    #     for titulo, valor in dados.items():
    #         campo = ft.TextField(value=str(valor), color=ft.colors.BLACK, read_only=True)
    #         self.campos[titulo] = campo
    #         conteudo_dialog.append(
    #             ft.Row(
    #                 controls=[
    #                     ft.Text(f"{titulo}:", size=14, color=ft.colors.BLACK, weight="bold"),
    #                     campo
    #                 ],
    #                 alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    #             )
    #         )

    #     # Configurar o diálogo com o conteúdo
    #     self.dialog = ft.AlertDialog(
    #         bgcolor=ft.colors.WHITE,
    #         modal=True,
    #         content=ft.Container(
    #             width=550,
    #             # padding=ft.padding.only(left=15, right=15),
    #             content=ft.Column(
    #                 controls=conteudo_dialog,
    #                 alignment=ft.MainAxisAlignment.START,
    #                 scroll=ft.ScrollMode.AUTO
    #             )
    #         )
    #     )

    #     # Exibe o dialog
    #     self.page.overlay.append(self.dialog)
    #     self.dialog.open = True
    #     self.page.update()

    # def detalhes_atividade(self, id_atividade):
    #     self.id_atividade_atual = id_atividade
    #     banco = GerenciamentoBanco()
    #     atividade = Atividade(banco)
    #     detalhes = atividade.obter_detalhes_atividade(id_atividade)

    #     if detalhes is None:
    #         snackbar = ft.SnackBar(ft.Text("Erro ao obter detalhes da atividade."), bgcolor=ft.colors.RED)
    #         self.page.overlay.append(snackbar)
    #         snackbar.open = True
    #         self.page.update()
    #         return
        
    #     dados = {
    #         "ID": detalhes[0],
    #         "Plantio": detalhes[1],
    #         "Descrição da Atividade": detalhes[2],
    #         "Prioridade (1 a 3)": detalhes[3],
    #         "Data": detalhes[4],
    #         "Tempo": detalhes[5],
    #         "Fase Atual": detalhes[6]
    #     }
    #     # Conteúdo do diálogo
    #     conteudo_dialog = [
    #         ft.Row(
    #             controls=[
    #                 ft.Text(f"Detalhes da Atividade", color=ft.colors.BLACK, size=18, weight="bold"),
    #                 ft.IconButton(icon=ft.icons.CLOSE, icon_color=ft.colors.BLACK, on_click=self._fechar_dialog)
    #             ],
    #             alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    #         )
    #     ]

    #     # Adicionar os campos do dicionário `dados` ao diálogo
    #     for titulo, valor in dados.items():
    #         campo = ft.TextField(value=str(valor), color=ft.colors.BLACK, read_only=True)
    #         self.campos[titulo] = campo
    #         conteudo_dialog.append(
    #             ft.Row(
    #                 controls=[
    #                     ft.Text(f"{titulo}:", size=14, color=ft.colors.BLACK, weight="bold"),
    #                     campo
    #                 ],
    #                 alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    #             )
    #         )

    #     # Configurar o diálogo com o conteúdo
    #     self.dialog = ft.AlertDialog(
    #         bgcolor=ft.colors.WHITE,
    #         modal=True,
    #         content=ft.Container(
    #             width=550,
    #             # padding=ft.padding.only(left=15, right=15),
    #             content=ft.Column(
    #                 controls=conteudo_dialog,
    #                 alignment=ft.MainAxisAlignment.START,
    #                 scroll=ft.ScrollMode.AUTO
    #             )
    #         )
    #     )

    #     # Exibe o dialog
    #     self.page.overlay.append(self.dialog)
    #     self.dialog.open = True
    #     self.page.update()

    def detalhes_producao(self, id_plantio):
        self.id_plantio_atual = id_plantio
        # self._alternar_modo_edicao(None, tipo_entidade='producao')
        banco = GerenciamentoBanco()
        producao = Producao(banco)

        detalhes = producao.obter_detalhes_plantio(id_plantio)

        if detalhes is None:
            snackbar = ft.SnackBar(ft.Text("Erro ao obter detalhes da produçao."), bgcolor=ft.colors.RED)
            self.page.overlay.append(snackbar)
            snackbar.open = True
            self.page.update()
            return
        
        dados = {
            "ID": detalhes[0],
            "Plantio": detalhes[1],
            "Data de Inicio": detalhes[2],
            "Produto": detalhes[3],
            "Quantidade": detalhes[4]
        }

        # Conteúdo do diálogo
        conteudo_dialog = [
            ft.Row(
                controls=[
                    ft.Text(f"Detalhes da Produçao", color=ft.colors.BLACK, size=18, weight="bold"),
                    ft.IconButton(icon=ft.icons.CLOSE, icon_color=ft.colors.BLACK, on_click=self._fechar_dialog)
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            )
        ]

        # Adicionar os campos do dicionário `dados` ao diálogo
        for titulo, valor in dados.items():
            campo = ft.Text(value=str(valor), size=16, color=ft.colors.BLACK)
            self.campos[titulo] = campo
            conteudo_dialog.append(
                ft.Row(
                    controls=[
                        ft.Text(f"{titulo}:", size=16, color=ft.colors.BLACK, weight="bold"),
                        campo
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                )
            )

        # Configurar o diálogo com o conteúdo
        self.dialog = ft.AlertDialog(
            bgcolor=ft.colors.WHITE,
            modal=False,
            content=ft.Container(
                # padding=ft.padding.only(left=15, right=15),
                content=ft.Column(
                    controls=conteudo_dialog,
                    alignment=ft.MainAxisAlignment.START,
                    scroll=ft.ScrollMode.AUTO
                )
            )
        )

        # Exibe o dialog
        self.page.overlay.append(self.dialog)
        self.dialog.open = True
        self.page.update()


    def _fechar_dialog(self, e=None):
        # Fecha o diálogo sem salvar
        self.dialog.open = False
        self.page.update()
