import hashlib
import flet as ft
import pyodbc
from datetime import datetime, date
from hashlib import sha256


class GerenciamentoBanco:
    def __init__(self):
        self.conn_str = r'Driver=ODBC Driver 17 for SQL Server;Server=facu-pixfarm.czwmyguc4vet.sa-east-1.rds.amazonaws.com;Database=PIXFARM;UID=admin;PWD=pixfarm2024;'
        self.conn = None
        self.cursor = None

    def conectar(self):
        # Conecta ao banco de dados
        if self.conn is None:
            try:
                self.conn = pyodbc.connect(self.conn_str)
                self.cursor = self.conn.cursor()
            except pyodbc.Error as err:
                print(f"Erro ao conectar no banco de dados: {err}")
                self.conn = None
                self.cursor = None

    def fechar_conexao(self):
        if self.conn:
            try:
                self.conn.close()
            except pyodbc.error as err:
                print(f"Erro ao fechar a conexão: {err}")
            finally:
                self.conn = None
                self.cursor = None








    def cadastro(self, tipo_cadastro, dados):
        self.conectar()
        if tipo_cadastro == 'fornecedor':
            try:
                self.cursor.execute(
                    '''{CALL InserirFornecedor (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)}''', 
                        (dados['Nome'], dados['Nome Fantasia'], dados['CNPJ'], dados['Email'], dados['Telefone'], dados['Rua'], dados['Número'], dados['Bairro'], dados['CEP'], dados['Cidade'], dados['Estado'])
                        )
                self.conn.commit()
                print("Fornecedor inserido com sucesso.")
                return True, None
            except pyodbc.IntegrityError as e:
                error_message = str(e).split('(')[1].split(')')[0]
                print("Erro de integridade:", error_message)
                return False, error_message
            except pyodbc.ProgrammingError as e:
                error_message = str(e).split('(')[1].split(')')[0]
                print("Erro de programação:", e)
                return False, error_message
            except pyodbc.Error as e:
                error_message = str(e).split('(')[1].split(')')[0]
                print("Erro ao inserir fornecedor:", e)
                return False, error_message
            finally:
                self.fechar_conexao()
            
        elif tipo_cadastro == 'cliente':
            try:
                self.cursor.execute(
                    '''{CALL InserirCliente (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)}''',
                    (dados['Nome'], dados['Nome Fantasia'], dados['CNPJ'], dados['Email'], dados['Rua'], dados['Numero'], dados['Bairro'], dados['CEP'], dados['Cidade'], dados['Estado'])
                    )
                self.conn.commit()
                return True, None
            except pyodbc.IntegrityError as e:
                error_message = str(e).split('(')[1].split(')')[0]
                print("Erro de integridade:", error_message)
                return False, error_message
            except pyodbc.ProgrammingError as e:
                error_message = str(e).split('(')[1].split(')')[0]
                print("Erro de programação:", e)
                return False, error_message
            except pyodbc.Error as e:
                error_message = str(e).split('(')[1].split(')')[0]
                print("Erro ao inserir fornecedor:", e)
                return False, error_message
            finally:
                self.fechar_conexao()
        
        elif tipo_cadastro == 'funcionario':
            try:
                self.cursor.execute(
                    '''{CALL CadastrarFuncionario (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)}''',
                    (dados['Nome'], dados['CPF'], dados['Sexo'], dados['Cargo'], dados['Descricao'], dados['Salario'], dados['Senha'], dados['Nascimento'], dados['Email'], dados['Setor'], dados['Data_Inicio'])
                )
                self.conn.commit()
                return True, None
            except pyodbc.IntegrityError as e:
                error_message = str(e).split('(')[1].split(')')[0]
                print("Erro de integridade:", error_message)
                return False, error_message
            except pyodbc.ProgrammingError as e:
                error_message = str(e).split('(')[1].split(')')[0]
                print("Erro de programação:", e)
                return False, error_message
            except pyodbc.Error as e:
                error_message = str(e).split('(')[1].split(')')[0]
                print("Erro ao inserir fornecedor:", e)
                return False, error_message
            finally:
                self.fechar_conexao()

        elif tipo_cadastro == 'materia prima':
            try:
                self.cursor.execute('''{CALL RegistrarCompra (?, ?, ?, ?, ?)}''',
                (dados["CNPJ Fornecedor"], dados["Data"], dados["Materia Prima"], dados["Quantidade"], dados["URL imagem (png)"])
                )
                self.conn.commit()
                return True, None
            except pyodbc.IntegrityError as e:
                error_message = str(e).split('(')[1].split(')')[0]
                print("Erro de integridade:", error_message)
                return False, error_message
            except pyodbc.ProgrammingError as e:
                error_message = str(e).split('(')[1].split(')')[0]
                print("Erro de programação:", e)
                return False, error_message
            except pyodbc.Error as e:
                error_message = str(e).split('(')[1].split(')')[0]
                print("Erro ao inserir fornecedor:", e)
                return False, error_message
            finally:
                self.fechar_conexao()

        elif tipo_cadastro == 'iniciar producao':
            try:
                self.cursor.execute('''{CALL IniciarProducao (?, ?, ?, ?, ?, ?)}''',
                (dados["Nome Produção"], dados["ID Matéria Prima"], dados["Produto Final"], dados["Quantidade"], dados["Data Inicio"], dados["Fase Atual"])
                )
                self.conn.commit()
                return True, None
            except pyodbc.IntegrityError as e:
                error_message = str(e).split('(')[1].split(')')[0]
                print("Erro de integridade:", error_message)
                return False, error_message
            except pyodbc.ProgrammingError as e:
                error_message = str(e).split('(')[1].split(')')[0]
                print("Erro de programação:", e)
                return False, error_message
            except pyodbc.Error as e:
                error_message = str(e).split('(')[1].split(')')[0]
                print("Erro ao inserir fornecedor:", e)
                return False, error_message
            finally:
                self.fechar_conexao()

        elif tipo_cadastro == 'finalizar producao':
            try:
                self.cursor.execute('''{CALL Finaliza_Producao (?, ?)}''',
                (dados["ID Plantio"], dados["Data Fim"])
                )
                self.conn.commit()
                return True, None
            except pyodbc.IntegrityError as e:
                error_message = str(e).split('(')[1].split(')')[0]
                print("Erro de integridade:", error_message)
                return False, error_message
            except pyodbc.ProgrammingError as e:
                error_message = str(e).split('(')[1].split(')')[0]
                print("Erro de programação:", e)
                return False, error_message
            except pyodbc.Error as e:
                error_message = str(e).split('(')[1].split(')')[0]
                print("Erro ao inserir fornecedor:", e)
                return False, error_message
            finally:
                self.fechar_conexao()

                
        elif tipo_cadastro == 'atividade':
            try:
                print(dados)
                self.cursor.execute('''{CALL RegistrarAtividade (?, ?, ?, ?, ?, ?, ?)}''',
                (dados["Nome do Funcionario"], dados["Nome Plantio"], dados["Descrição"], dados["Prioridade(1 a 3)"], dados["Data"], dados["Duração"], dados["Fase Atual"])
                )
                self.conn.commit()
                return True, None
            except pyodbc.IntegrityError as e:
                error_message = str(e).split('(')[1].split(')')[0]
                print("Erro de integridade:", error_message)
                return False, error_message
            except pyodbc.ProgrammingError as e:
                error_message = str(e).split('(')[1].split(')')[0]
                print("Erro de programação:", e)
                return False, error_message
            except pyodbc.Error as e:
                error_message = str(e).split('(')[1].split(')')[0]
                print("Erro ao inserir fornecedor:", e)
                return False, error_message
            finally:
                self.fechar_conexao()

        elif tipo_cadastro == "novo produto":
            try:
                self.cursor.execute('''INSERT INTO Produto (Produto, Previsao) VALUES (?, ?)''',
                (dados["Novo produto"], dados["Previsao de entrega"])
                )
                self.conn.commit()
                return True, None
            except pyodbc.IntegrityError as e:
                error_message = str(e).split('(')[1].split(')')[0]
                print("Erro de integridade:", error_message)
                return False, error_message
            except pyodbc.ProgrammingError as e:
                error_message = str(e).split('(')[1].split(')')[0]
                print("Erro de programação:", e)
                return False, error_message
            except pyodbc.Error as e:
                error_message = str(e).split('(')[1].split(')')[0]
                print("Erro ao inserir fornecedor:", e)
                return False, error_message
            finally:
                self.fechar_conexao()

        elif tipo_cadastro == "pedido":
            try:
                self.cursor.execute('''{CALL RegistrarPedido (?, ?, ?, ?)}''',
                (dados["CNPJ do Cliente"], dados["Data Pedido"], dados["Produto"], dados["Quantidade"])
                )
                self.conn.commit()
                return True, None
            except pyodbc.IntegrityError as e:
                error_message = str(e).split('(')[1].split(')')[0]
                print("Erro de integridade:", error_message)
                return False, error_message
            except pyodbc.ProgrammingError as e:
                error_message = str(e).split('(')[1].split(')')[0]
                print("Erro de programação:", e)
                return False, error_message
            except pyodbc.Error as e:
                error_message = str(e).split('(')[1].split(')')[0]
                print("Erro ao inserir fornecedor:", e)
                return False, error_message
            finally:
                self.fechar_conexao()



class Cadastro:
    def __init__(self, page):
        """
        Inicializa a classe Cadastro com a página onde o dialog será exibido.
        :param page: A página do aplicativo onde o dialog será mostrado.
        """
        self.page = page
        self.dialog = None
        self.inputs = {}
        self.senha_input = None
        self.dados_salvos = None  # Armazena temporariamente os dados salvos para possível reversão

    def abrir_cadastro(self, tipo_cadastro):
        """
        Abre um AlertDialog configurado com os campos apropriados para o tipo de cadastro fornecido.
        :param tipo_cadastro: String representando o tipo de cadastro (ex.: "fornecedor", "cliente", "produto").
        """
        self.tipo_cadastro = tipo_cadastro
        campos_por_tipo = {
            "fornecedor": [
                {"titulo": "Informações Básicas", "campos": ["Nome", "Nome Fantasia", "CNPJ", "Email", "Telefone"]},
                {"titulo": "Endereço", "campos": ["Rua", "Número", "Bairro", "CEP", "Cidade", "Estado"]}
            ],
            "cliente": [
                {"titulo": "Informações Básicas", "campos": ["Nome", "Nome Fantasia", "CNPJ", "Email"]},
                {"titulo": "Endereço", "campos": ["Rua", "Numero", "Bairro", "CEP", "Cidade", "Estado"]}
            ],
            "funcionario": [
                {"titulo": "Informações do Funcionario", "campos": ["Nome", "CPF", "Sexo", "Nascimento", "Email", "Setor", "Senha"]},
                {"titulo": "Cargo", "campos": ["Cargo", "Descricao", "Salario", "Data Inicio"]}
            ],
            "materia prima": [
                {"titulo": "Informações da Compra", "campos": ["CNPJ Fornecedor", "Data", "Materia Prima", "Quantidade", "URL imagem (png)"]}
            ],
            "novo produto": [
                {"titulo": "Informações do Produto", "campos": ["Novo produto", "Previsao de entrega(dias)"]}
            ]
        }

        grupos_campos = campos_por_tipo.get(self.tipo_cadastro, [])

        conteudo_dialog = [
            ft.Row(
                controls=[
                    ft.Text(f"Cadastro de {self.tipo_cadastro.capitalize()}", color=ft.colors.BLACK, size=20, weight="bold"),
                    ft.IconButton(icon=ft.icons.CLOSE, icon_color=ft.colors.BLACK, on_click=self._fechar_dialog)
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            )
        ]

        self.datepicker_control = None

        # Ao clicar para adicionar a data, ele abre o datepicker e permite selecionar a data, porém ao tentar confirmar ou cancelar, o mesmo entra em loop e não fecha a page do datepicker.
        for grupo in grupos_campos:
            conteudo_dialog.append(ft.Text(grupo["titulo"], size=16, weight="bold", color=ft.colors.GREY))
            campos = grupo["campos"]

            for campo in campos:
                if campo in ("Data", "Data Inicio", "Data Fim", "Nascimento"):  # Verifica se o campo é "Data"
                    date_field_flag = {"is_open": False}  # Flag para controlar a abertura

                    def handle_focus(e, campo=campo):
                        if not date_field_flag["is_open"]:
                            date_field_flag["is_open"] = True
                            self.page.open(
                                ft.DatePicker(
                                    cancel_text='Cancelar',
                                    confirm_text='Confirmar',
                                    error_format_text='Data inválida',
                                    field_hint_text='MM/DD/YYYY',
                                    help_text='Selecione uma data no calendário',
                                    date_picker_entry_mode=ft.DatePickerEntryMode.CALENDAR_ONLY,
                                    on_change=lambda e: (
                                        setattr(self.inputs[campo], 'value', e.control.value.strftime('%Y-%m-%d')),
                                        self.page.update(),
                                        setattr(date_field_flag, 'is_open', False)  # Reseta a flag após seleção
                                    ),
                                    on_dismiss=lambda e: setattr(date_field_flag, 'is_open', False)  # Reseta a flag após cancelamento
                                )
                            )

                    date_field = ft.TextField(
                        label=campo,
                        width=250,
                        read_only=True,  # Apenas exibição
                        on_focus=handle_focus
                    )
                    self.inputs[campo] = date_field
                else:
                    # Cria campos normais
                    self.inputs[campo] = ft.TextField(label=campo, color=ft.colors.BLACK, width=250)

            for campo in campos:
                if campo == "Senha":
                    self.senha_input = ft.TextField(label="Senha", password=True)  # Cria um campo de senha
                    conteudo_dialog.append(self.senha_input)
                else:
                    conteudo_dialog.append(ft.TextField(label=campo))

            for i in range(0, len(campos), 2):
                linha = ft.Row(
                    controls=[self.inputs[campos[j]] for j in range(i, min(i + 2, len(campos)))],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                )
                conteudo_dialog.append(linha)




        botoes = ft.Row(
            controls=[
                ft.ElevatedButton("Salvar", color=ft.colors.WHITE, bgcolor="#13330D", on_click=self._salvar_dados)
            ],
            alignment=ft.MainAxisAlignment.END
        )

        conteudo_dialog.append(botoes)

        self.dialog = ft.AlertDialog(
            bgcolor=ft.colors.WHITE,
            modal=True,
            content=ft.Container(
                width=550,
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

    def abrir_registro(self, tipo_cadastro):
        """
        Abre um AlertDialog configurado com os campos apropriados para o tipo de cadastro fornecido.
        :param tipo_cadastro: String representando o tipo de cadastro (ex.: "fornecedor", "cliente", "produto").
        """
        self.tipo_cadastro = tipo_cadastro
        campos_por_tipo = {
            "iniciar producao": [
                {"titulo": "Dados da Produção", "campos": ["Nome Produção", "ID Matéria Prima", "Produto Final", "Quantidade", "Data Inicio", "Fase Atual"]}
            ],
            "finalizar producao": [
                {"titulo": "Dados da Produção", "campos": ["ID Plantio", "Data Fim"]}
            ],
            "pedido": [
                {"titulo": "Dados do Pedido", "campos": ["CNPJ do Cliente", "Data Pedido"]},
                {"titulo": "Itens do Pedido", "campos": ["Produto", "Quantidade"]}
            ],
            "atividade": [
                {"titulo": "Responsável da Atividade", "campos": ["Nome do Funcionario", "Nome Plantio"]},
                {"titulo": "Detalhes da Atividade", "campos": ["Descrição", "Prioridade(1 a 3)", "Data", "Duração", "Fase Atual"]}
            ]
        }

        grupos_campos = campos_por_tipo.get(self.tipo_cadastro, [])

        conteudo_dialog = [
            ft.Row(
                controls=[
                    ft.Text(f"{self.tipo_cadastro.capitalize()}", color=ft.colors.BLACK, size=20, weight="bold"),
                    ft.IconButton(icon=ft.icons.CLOSE, icon_color=ft.colors.BLACK, on_click=self._fechar_dialog)
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            )
        ]

        self.itens_pedido = []


        # Ao clicar para adicionar a data, ele abre o datepicker e permite selecionar a data, porém ao tentar confirmar ou cancelar, o mesmo entra em loop e não fecha a page do datepicker.
        for grupo in grupos_campos:
            conteudo_dialog.append(ft.Text(grupo["titulo"], size=16, weight="bold", color=ft.colors.GREY))
            campos = grupo["campos"]

            for campo in campos:
                if campo in ("Data", "Data Pedido", "Data Inicio", "Data Fim", "Nascimento"):  # Verifica se o campo é "Data"
                    date_field_flag = {"is_open": False}  # Flag para controlar a abertura

                    def pegar_data(e, campo=campo):
                        if not date_field_flag["is_open"]:
                            date_field_flag["is_open"] = True
                            self.page.open(
                                ft.DatePicker(
                                    cancel_text='Cancelar',
                                    confirm_text='Confirmar',
                                    error_format_text='Data inválida',
                                    field_hint_text='MM/DD/YYYY',
                                    help_text='Selecione uma data no calendário',
                                    date_picker_entry_mode=ft.DatePickerEntryMode.CALENDAR_ONLY,
                                    on_change=lambda e: (
                                        setattr(self.inputs[campo], 'value', e.control.value.strftime('%Y-%m-%d')),
                                        self.dialog.update(),
                                    ),
                                )
                            )

                    date_field = ft.TextField(
                        label=campo,
                        width=250,
                        read_only=True,  # Apenas exibição
                        on_focus=pegar_data
                    )
                    self.inputs[campo] = date_field
                elif campo == "Duração":
                    time_field_flag = {"is_open": False}

                    def pegar_hora(e, campo=campo):
                        if not time_field_flag["is_open"]:
                            time_field_flag["is_open"] = True
                            self.page.open(
                                ft.TimePicker(
                                    cancel_text='Cancelar',
                                    confirm_text='Confirmar',
                                    error_invalid_text='Hora inválida',
                                    hour_label_text='Hora',
                                    minute_label_text='Minutos',
                                    help_text='Selecione o tempo de duração da atividade',
                                    # value=0,
                                    on_change=lambda e: (
                                        setattr(self.inputs[campo], 'value', e.control.value.strftime('%H:%M:%S')),
                                        self.dialog.update()
                                    )

                                )
                            )
                    time_field = ft.TextField(
                        label=campo,
                        width=250,
                        read_only=True,
                        on_focus=pegar_hora
                    )
                    self.inputs[campo] = time_field
                else:
                    # Cria campos normais
                    self.inputs[campo] = ft.TextField(label=campo, color=ft.colors.BLACK, width=250)

            for i in range(0, len(campos), 2):
                linha = ft.Row(
                    controls=[self.inputs[campos[j]] for j in range(i, min(i + 2, len(campos)))],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                )
                conteudo_dialog.append(linha)

        self.dialog = ft.AlertDialog(
            bgcolor=ft.colors.WHITE,
            modal=True,
            content=ft.Container(
                width=550,
                content=ft.Column(
                    controls=conteudo_dialog,
                    alignment=ft.MainAxisAlignment.START,
                    scroll=ft.ScrollMode.AUTO
                )
            ),
            actions=[
                ft.ElevatedButton("Salvar", color=ft.colors.WHITE, bgcolor="#13330D", on_click=self._salvar_dados)

            ]
        )

        self.page.overlay.append(self.dialog)
        self.dialog.open = True
        self.page.update()

    def _salvar_dados(self, e):
        # Coleta os dados dos inputs e fecha o dialog
        self.dados_salvos = {campo: entrada.value for campo, entrada in self.inputs.items()}

        # Verificação do campo "Senha" e aplica hash
        if "Senha" in self.dados_salvos and self.dados_salvos["Senha"]:
            self.dados_salvos["Senha"] = self.hash_password(self.dados_salvos["Senha"])

        # Fecha o diálogo
        self.dialog.open = False
        self.page.update()

        # Insere os dados no banco e mostra o snackbar
        self.inserir_banco()

    def inserir_banco(self):
        banco = GerenciamentoBanco()
        sucesso, error_message = banco.cadastro(self.tipo_cadastro, self.dados_salvos)
        if sucesso:
            snackbar = ft.SnackBar(
                content=ft.Text("Cadastro realizado com sucesso!"),
                bgcolor=ft.colors.GREEN,
                duration=3000
            )
            self.page.overlay.append(snackbar)
            snackbar.open = True
            self.page.update()
            self.dados_salvos = None  # Limpa os dados salvos
        else:
            # Exibe um snackbar de erro
            snackbar = ft.SnackBar(
                content=ft.Text(f"Ocorreu um erro ao salvar os dados: {error_message}"),
                bgcolor=ft.colors.RED,
                duration=3000
            )
            self.page.overlay.append(snackbar)
            snackbar.open = True
            self.page.update()
            self.dados_salvos = None

    def _fechar_dialog(self, e):
        # Fecha o diálogo sem salvar
        self.dialog.open = False
        self.page.update()

    def hash_password(self, password):
        """
        Recebe uma senha e retorna o hash com um salt.
        :param password: String com a senha em texto puro.
        :return: String com o hash da senha.
        """
        hashed = hashlib.sha256(password.encode('utf-8')).hexdigest()
        return hashed



class Detalhes:
    def __init__(self, page, banco):
        """
        Inicializa a classe DetalhesDialog para exibir os detalhes de uma entidade.
        :param page: A página onde o dialog será mostrado.
        :param banco: Instância de GerenciamentoBanco para consultar os dados.
        """
        self.page = page
        self.banco = banco
        self.dialog = None
        self.em_edicao = False
        self.botoes = None
        self.campos = {}
        self.campos_nao_editaveis = ["ID", "Nome/Razão Social", "CNPJ", "CPF", "Cargo", "Data inicial"]





    



class Confirmacao:
    def __init__(self, page, mensagem, on_confirmar, on_cancelar=None):
        """
        Inicializa a classe ConfirmacaoDialog.
        :param page: A página onde o diálogo será exibido.
        :param mensagem: A mensagem a ser exibida no diálogo de confirmação.
        :param on_confirmar: Função a ser chamada quando o usuário confirmar.
        :param on_cancelar: Função a ser chamada quando o usuário cancelar (opcional).
        """
        self.page = page
        self.mensagem = mensagem
        self.on_confirmar = on_confirmar
        self.on_cancelar = on_cancelar

        # Criar o diálogo de confirmação
        self.dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Confirmação", size=18, weight="bold"),
            content=ft.Text(self.mensagem),
            actions=[
                ft.ElevatedButton("Sim", on_click=self._confirmar),
                ft.ElevatedButton("Cancelar", on_click=self._cancelar)
            ]
        )

    def exibir(self):
        """Exibe o diálogo de confirmação."""
        self.page.overlay.append(self.dialog)
        self.dialog.open = True
        self.page.update()

    def _confirmar(self, e):
        """Executa a função de confirmação e fecha o diálogo."""
        if self.on_confirmar:
            self.on_confirmar()
        self._fechar()

    def _cancelar(self, e):
        """Executa a função de cancelamento (se houver) e fecha o diálogo."""
        if self.on_cancelar:
            self.on_cancelar()
        self._fechar()

    def _fechar(self):
        """Fecha o diálogo e atualiza a página."""
        self.page.overlay.remove(self.dialog)
        self.dialog.open = False
        self.page.update()



        





