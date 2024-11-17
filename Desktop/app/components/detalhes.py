import flet as ft
import hashlib
from app.components.producao import Producao
from app.components.pedido import Pedido
from app.components.atividade import Atividade
from app.components.cliente import Cliente
from app.components.fornecedor import Fornecedor
from app.components.estoque import Estoque
from app.components.funcionario import Funcionario
from app.components.classes import GerenciamentoBanco
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

    def detalhes_producao(self, id_plantio):
        self.id_plantio_atual = id_plantio
        self._alternar_modo_edicao(None, tipo_entidade='producao')
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

    def detalhes_cliente(self, id_cliente):
        self.id_cliente_atual = id_cliente
        self._alternar_modo_edicao(None, tipo_entidade="cliente")
        banco = GerenciamentoBanco()
        cliente = Cliente(banco)

        # Obter detalhes do fornecedor pelo ID
        detalhes = cliente.obter_detalhes_clientes(id_cliente)

        if detalhes is None:
            snackbar = ft.SnackBar(ft.Text("Erro ao obter detalhes do cliente."), bgcolor=ft.colors.RED)
            self.page.overlay.append(snackbar)
            snackbar.open = True
            self.page.update()
            print("Erro ao obter os detalhes do cliente.")
            return


        # Organizar os detalhes em um dicionário para exibição
        dados = {
            "ID": detalhes[0],
            "Nome": detalhes[1],
            "CNPJ": detalhes[2],
            "Email": detalhes[3],
            "Rua": detalhes[4],
            "Número": detalhes[5],
            "Bairro": detalhes[6],
            "CEP": detalhes[7],
            "Cidade": detalhes[8],
            "Estado": detalhes[9]
        }

        # Conteúdo do diálogo
        conteudo_dialog = [
            ft.Row(
                controls=[
                    ft.Text(f"Detalhes do Cliente", size=18, color=ft.colors.BLACK, weight="bold"),
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

        self.botoes = ft.Row(
            controls=[
                ft.ElevatedButton("Editar", on_click=lambda e: self._alternar_modo_edicao(e, tipo_entidade="cliente"))
            ],
            alignment=ft.MainAxisAlignment.START
        )

        conteudo_dialog.append(self.botoes)

        # Configurar o diálogo com o conteúdo
        self.dialog = ft.AlertDialog(
            bgcolor=ft.colors.WHITE,
            modal=True,
            content=ft.Container(
                width=550,
                padding=ft.padding.only(left=15, right=15),
                content=ft.Column(
                    controls=conteudo_dialog,
                    alignment=ft.MainAxisAlignment.START,
                    scroll=ft.ScrollMode.AUTO
                )
            )
        )

        self.page.overlay.append(self.dialog)
        self.dialog.open = True
        self.page.update()

    def detalhes_fornecedor(self, id_fornecedor):
        self.id_fornecedor_atual = id_fornecedor
        self._alternar_modo_edicao(None, tipo_entidade="fornecedor")
        banco = GerenciamentoBanco()
        fornecedor = Fornecedor(banco)
        """
        Abre um AlertDialog configurado para exibir detalhes do fornecedor com o ID fornecido.
        :param id_fornecedor: ID do fornecedor para buscar detalhes.
        """
        # Obter detalhes do fornecedor pelo ID
        detalhes = fornecedor.obter_detalhes_fornecedores(id_fornecedor)

        if detalhes is None:
            self.page.snack_bar = ft.SnackBar(ft.Text("Erro ao obter detalhes do fornecedor."), bgcolor=ft.colors.RED)
            self.page.snack_bar.open = True
            self.page.update()
            print("Erro ao obter os detalhes do fornecedor.")
            return


        # Organizar os detalhes em um dicionário para exibição
        dados = {
            "ID": detalhes[0],
            "Nome/Razão Social": detalhes[1],
            "Nome Fantasia": detalhes[2],
            "CNPJ": detalhes[3],
            "Email": detalhes[4],
            "Telefone": detalhes[5],
            "Rua": detalhes[6],
            "Número": detalhes[7],
            "Bairro": detalhes[8],
            "CEP": detalhes[9],
            "Cidade": detalhes[10],
            "Estado": detalhes[11]
        }

        # Conteúdo do diálogo
        conteudo_dialog = [
            ft.Row(
                controls=[
                    ft.Text(f"Detalhes do Fornecedor", size=18, weight="bold"),
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

        self.botoes = ft.Row(
            controls=[
                ft.ElevatedButton("Editar", on_click=lambda e: self._alternar_modo_edicao(e, tipo_entidade="fornecedor"))
            ],
            alignment=ft.MainAxisAlignment.START
        )

        conteudo_dialog.append(self.botoes)

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

    def detalhes_materia_prima(self, id_materia):
        self.id_materia_atual = id_materia
        self._alternar_modo_edicao(None, tipo_entidade="materia_prima")
        banco = GerenciamentoBanco()
        mp = Estoque(banco)

        # Obter detalhes do fornecedor pelo ID
        detalhes = mp.obter_detalhes_materia_prima(id_materia)

        if detalhes is None:
            snackbar = ft.SnackBar(ft.Text("Erro ao obter detalhes da materia prima."), bgcolor=ft.colors.RED)
            self.page.overlay.append(snackbar)
            snackbar.open = True
            self.page.update()
            return


        # Organizar os detalhes em um dicionário para exibição
        dados = {
            "ID": detalhes[0],
            "Fornecedor": detalhes[1],
            "CNPJ Fornecedor": detalhes[2],
            "Nome Materia Prima": detalhes[3],
            "Quantidade": detalhes[4],
            "Data da Compra": detalhes[5],
        }

        # Conteúdo do diálogo
        conteudo_dialog = [
            ft.Row(
                controls=[
                    ft.Text(f"Detalhes do Funcionario", size=18, color=ft.colors.BLACK, weight="bold"),
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
                padding=ft.padding.only(left=15, right=15),
                content=ft.Column(
                    controls=conteudo_dialog,
                    alignment=ft.MainAxisAlignment.START,
                    scroll=ft.ScrollMode.AUTO
                )
            )
        )

        self.page.overlay.append(self.dialog)
        self.dialog.open = True
        self.page.update()

    def detalhes_funcionario(self, id_funcionario):
        self.id_funcionario_atual = id_funcionario
        self._alternar_modo_edicao(None, tipo_entidade='funcionario')
        banco = GerenciamentoBanco()
        funcionario = Funcionario(banco)

        # Obter detalhes do fornecedor pelo ID
        detalhes = funcionario.obter_detalhes_funcionario(id_funcionario)

        if detalhes is None:
            snackbar = ft.SnackBar(ft.Text("Erro ao obter detalhes do funcionario."), bgcolor=ft.colors.RED)
            self.page.overlay.append(snackbar)
            snackbar.open = True
            self.page.update()
            # print("Erro ao obter os detalhes do funcionario.")
            return


        # Organizar os detalhes em um dicionário para exibição
        dados = {
            "ID": detalhes[0],
            "Nome": detalhes[1],
            "CPF": detalhes[2],
            "Sexo": detalhes[3],
            "Cargo": detalhes[4],
            "Senha": detalhes[5],
            "Nascimento": detalhes[6],
            "Email": detalhes[7],
            "Setor": detalhes[8],
            "Data inicial": detalhes[9]
        }

        # Conteúdo do diálogo
        conteudo_dialog = [
            ft.Row(
                controls=[
                    ft.Text(f"Detalhes do Funcionario", size=18, color=ft.colors.BLACK, weight="bold"),
                    ft.IconButton(icon=ft.icons.CLOSE, icon_color=ft.colors.BLACK, on_click=self._fechar_dialog)
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            )
        ]

        # Adicionar os campos do dicionário `dados` ao diálogo, permitindo a edição
        for titulo, valor in dados.items():
            if titulo == "Senha":
                campo = ft.TextField(value="", label="Nova senha (deixe em branco para manter)", color=ft.colors.BLACK, read_only=True)
            else:
                campo = ft.TextField(value=str(valor), color=ft.colors.BLACK, read_only=(titulo == "ID"))
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

        self.botoes = ft.Row(
            controls=[
                ft.ElevatedButton("Editar", on_click=lambda e: self._alternar_modo_edicao(e, tipo_entidade="funcionario"))
            ],
            alignment=ft.MainAxisAlignment.START
        )

        conteudo_dialog.append(self.botoes)

        # Configurar o diálogo com o conteúdo
        self.dialog = ft.AlertDialog(
            bgcolor=ft.colors.WHITE,
            modal=True,
            content=ft.Container(
                width=550,
                padding=ft.padding.only(left=15, right=15),
                content=ft.Column(
                    controls=conteudo_dialog,
                    alignment=ft.MainAxisAlignment.START,
                    scroll=ft.ScrollMode.AUTO
                )
            )
        )

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
            dialogo_confirmacao = ConfirmationDialog(
                title="Confirmar Alterações",
                content="Deseja realmente salvar as alterações?",
                actions=[
                ft.TextButton("Cancelar", on_click=lambda e: dialogo_confirmacao.close_dialog()),
                ft.ElevatedButton("Confirmar", on_click=lambda e: [dialogo_confirmacao.close_dialog(), self.salvar_alteracoes(None, tipo_entidade=tipo_entidade)])
                ],
                page=self.page
            )
            # Quando em modo de edição, mostra o botão "Salvar"
            self.botoes.controls = [
                ft.ElevatedButton("Salvar", on_click=lambda e: dialogo_confirmacao.open_dialog())
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
            banco = GerenciamentoBanco()
            cliente = Cliente(banco)
            resultado = cliente.atualizar_cliente(dados_atualizados, self.id_cliente_atual)
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
