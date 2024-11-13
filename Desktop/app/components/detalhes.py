import flet as ft
from hashlib import sha256
from app.components.pedido import Pedido
from app.components.atividade import Atividade
from app.components.classes import GerenciamentoBanco

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
        self.em_edicao = False
        self.botoes = None
        self.campos = {}
        self.campos_nao_editaveis = ["ID", "Nome/Razão Social", "CNPJ", "CPF", "Cargo", "Data inicial"]

    def detalhes_pedido(self, id_pedido):
        self.id_pedido_atual = id_pedido
        self._alternar_modo_edicao(None, tipo_entidade='pedido')

        banco = GerenciamentoBanco()
        pedido = Pedido(banco)

        detalhes = pedido.obter_detalhes_pedido(id_pedido)
        
        if detalhes is None:
            snackbar = ft.SnackBar(ft.Text("Erro ao obter detalhes do pedido."), bgcolor=ft.colors.RED)
            self.page.overlay.append(snackbar)
            snackbar.open = True
            self.page.update()
            return
        
        dados = {
            "ID": detalhes[0],
            "Cliente": detalhes[1],
            "Data do Pedido": detalhes[2],
            "Produto": detalhes[3],
            "Quantidade": detalhes[4],
            "Previsão de Entrega (dias)": detalhes[5],
            "Status": detalhes[6]
        }

        # Conteúdo do diálogo
        conteudo_dialog = [
            ft.Row(
                controls=[
                    ft.Text(f"Detalhes do", color=ft.colors.BLACK, size=18, weight="bold"),
                    ft.IconButton(icon=ft.icons.CLOSE, icon_color=ft.colors.BLACK, on_click=self._fechar_dialog)
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            )
        ]

        # Adicionar os campos do dicionário `dados` ao diálogo
        for titulo, valor in dados.items():
            campo = ft.TextField(value=str(valor), color=ft.colors.BLACK, read_only=True)
            self.campos[titulo] = campo
            conteudo_dialog.append(
                ft.Row(
                    controls=[
                        ft.Text(f"{titulo}:", size=14, color=ft.colors.BLACK, weight="bold"),
                        campo
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                )
            )

        # Configurar o diálogo com o conteúdo
        self.dialog = ft.AlertDialog(
            bgcolor=ft.colors.WHITE,
            modal=True,
            content=ft.Container(
                width=550,
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

    def detalhes_atividade(self, id_atividade):
        self.id_atividade_atual = id_atividade
        self._alternar_modo_edicao(None, tipo_entidade='atividade')
        banco = GerenciamentoBanco()
        atividade = Atividade(banco)
        detalhes = atividade.obter_detalhes_atividade(id_atividade)

        if detalhes is None:
            snackbar = ft.SnackBar(ft.Text("Erro ao obter detalhes da atividade."), bgcolor=ft.colors.RED)
            self.page.overlay.append(snackbar)
            snackbar.open = True
            self.page.update()
            return
        
        dados = {
            "ID": detalhes[0],
            "Plantio": detalhes[1],
            "Descrição da Atividade": detalhes[2],
            "Prioridade (1 a 3)": detalhes[3],
            "Data": detalhes[4],
            "Tempo": detalhes[5],
            "Fase Atual": detalhes[6]
        }
        # Conteúdo do diálogo
        conteudo_dialog = [
            ft.Row(
                controls=[
                    ft.Text(f"Detalhes do", color=ft.colors.BLACK, size=18, weight="bold"),
                    ft.IconButton(icon=ft.icons.CLOSE, icon_color=ft.colors.BLACK, on_click=self._fechar_dialog)
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            )
        ]

        # Adicionar os campos do dicionário `dados` ao diálogo
        for titulo, valor in dados.items():
            campo = ft.TextField(value=str(valor), color=ft.colors.BLACK, read_only=True)
            self.campos[titulo] = campo
            conteudo_dialog.append(
                ft.Row(
                    controls=[
                        ft.Text(f"{titulo}:", size=14, color=ft.colors.BLACK, weight="bold"),
                        campo
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                )
            )

        # Configurar o diálogo com o conteúdo
        self.dialog = ft.AlertDialog(
            bgcolor=ft.colors.WHITE,
            modal=True,
            content=ft.Container(
                width=550,
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

    def _alternar_modo_edicao(self, e, tipo_entidade):
        """Alterna o modo de edição dos campos e ajusta o botão de salvar para a entidade especificada."""
        self.em_edicao = not self.em_edicao

        if not hasattr(self, 'botoes') or self.botoes is None:
            self.botoes = ft.Row(
                controls=[
                    ft.ElevatedButton("Editar", on_click=self._alternar_modo_edicao)
                    ],
                alignment=ft.MainAxisAlignment.START
                )

        for titulo, campo in self.campos.items():
            if titulo not in self.campos_nao_editaveis:
                campo.read_only = not self.em_edicao  # Alterna entre modo de edição e leitura
            else:
                campo.read_only = True
                campo.opacity = 0.5
            campo.update()

        if self.em_edicao:
            # Quando em modo de edição, mostra o botão "Salvar"
            self.botoes.controls = [
                ft.ElevatedButton("Salvar", on_click=lambda e: self.salvar_alteracoes(e, tipo_entidade=tipo_entidade))
            ]
        else:
            # Quando em modo de leitura, mostra o botão "Editar"
            self.botoes.controls = [
                ft.ElevatedButton("Editar", on_click=lambda e: self._alternar_modo_edicao(e, tipo_entidade=tipo_entidade))
            ]
        self.page.update()

    def salvar_alteracoes(self, e, tipo_entidade):
        dados_atualizados = {}
        for titulo, campo in self.campos.items():
            if not campo.read_only:
                dados_atualizados[titulo] = campo.value

        if dados_atualizados["Senha"]:
            dados_atualizados["Senha"] = self.hash_password_sha256(dados_atualizados["Senha"])
        else:
            dados_atualizados.pop["Senha"]

        if tipo_entidade == "fornecedor":
            banco = Fornecedor()
            resultado = banco.atualizar_fornecedor(dados_atualizados, self.id_fornecedor_atual)
        elif tipo_entidade == "cliente":
            banco = Cliente()
            resultado = banco.atualizar_cliente(dados_atualizados, self.id_cliente_atual)
        elif tipo_entidade == "funcionario":
            # banco = Funcionario()
            banco = GerenciamentoBanco()
            resultado = banco.atualizar_funcionario(dados_atualizados, self.id_funcionario_atual)
        else:
            print("Tipo de entidade desconhecido")
            return

        if resultado is True:
            snack_bar = ft.SnackBar(ft.Text(f"Alterações em {tipo_entidade} realizadas com sucesso!"), bgcolor=ft.colors.GREEN)
        else:
            snack_bar = ft.SnackBar(ft.Text(f"Erro ao salvar alterações em {tipo_entidade}!"), bgcolor=ft.colors.RED)

        self.page.overlay.append(snack_bar)
        snack_bar.open = True
        self.dialog.open = False
        self.page.update()

    def _fechar_dialog(self, e=None):
        # Fecha o diálogo sem salvar
        self.dialog.open = False
        self.page.update()

    def hash_password_sha256(self, password):
        hashed = hashlib.sha256(password.encode('utf-8')).hexdigest()
        return hashed
