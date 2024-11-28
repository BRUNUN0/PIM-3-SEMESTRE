import hashlib
import flet as ft
import pyodbc
from datetime import datetime
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
        
        try:
            if tipo_cadastro == 'fornecedor':
                self.cursor.execute('''{CALL InserirFornecedor (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)}''', 
                    (dados['Nome'], dados['Nome Fantasia'], dados['CNPJ'], dados['Email'], dados['Telefone'], 
                    dados['Rua'], dados['Número'], dados['Bairro'], dados['CEP'], dados['Cidade'], dados['Estado']))
                self.conn.commit()
                print("Fornecedor inserido com sucesso.")
                return True, None
            
            elif tipo_cadastro == 'cliente':
                self.cursor.execute('''{CALL InserirCliente (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)}''',
                    (dados['Nome'], dados['Nome Fantasia'], dados['CNPJ'], dados['Email'], dados['Rua'], dados['Numero'], 
                    dados['Bairro'], dados['CEP'], dados['Cidade'], dados['Estado']))
                self.conn.commit()
                return True, None

            elif tipo_cadastro == 'funcionario':
                self.cursor.execute('''{CALL CadastrarFuncionario (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)}''',
                    (dados['Nome'], dados["RG"], dados['CPF'], dados['Sexo'], dados['Cargo'], dados['Descricao'], dados['Salario'], 
                    dados['Senha'], dados['Nascimento'], dados['Email'], dados['Setor'], dados['Data Inicio']))
                self.conn.commit()
                return True, None

            elif tipo_cadastro == 'materia prima':
                self.cursor.execute('''{CALL RegistrarCompra (?, ?, ?, ?)}''',
                    (dados["CNPJ Fornecedor"], dados["Data"], dados["Materia Prima"], dados["Quantidade"]))
                self.conn.commit()
                return True, None

            elif tipo_cadastro == 'iniciar producao':
                self.cursor.execute('''{CALL IniciarProducao (?, ?, ?, ?, ?, ?)}''',
                    (dados["Nome Produção"], dados["ID Matéria Prima"], dados["Produto Final"], dados["Quantidade"], dados["Data Inicio"], dados["Fase Atual"]))
                self.conn.commit()
                return True, None

            elif tipo_cadastro == 'finalizar producao':
                self.cursor.execute('''{CALL Finaliza_Producao (?, ?)}''',
                    (dados["ID Plantio"], dados["Data Fim"]))
                self.conn.commit()
                return True, None

            elif tipo_cadastro == 'atividade':
                self.cursor.execute('''{CALL RegistrarAtividade (?, ?, ?, ?, ?, ?, ?)}''',
                    (dados["Nome do Funcionario"], dados["Nome Plantio"], dados["Descrição"], dados["Prioridade(1 a 3)"], dados["Data"], dados["Duração"], dados["Fase Atual"]))
                self.conn.commit()
                return True, None

            elif tipo_cadastro == "novo produto":
                self.cursor.execute('''INSERT INTO Produto (Produto, Quantidade, Previsao) VALUES (?, ?, ?)''',
                    (dados["Novo produto"], 0, dados["Previsao de entrega(dias)"]))
                self.conn.commit()
                return True, None

            elif tipo_cadastro == "pedido":
                self.cursor.execute('''{CALL RegistrarPedido (?, ?, ?, ?)}''',
                    (dados["CNPJ do Cliente"], dados["Data Pedido"], dados["Produto"], dados["Quantidade"]))
                self.conn.commit()
                return True, None

            elif tipo_cadastro == "finalizar pedido":
                self.cursor.execute('''{CALL FinalizarPedido (?)}''', dados['ID do Pedido'])
                self.conn.commit()
                return True, None

        except pyodbc.IntegrityError as e:
            self.conn.rollback()  # Realiza rollback em caso de erro
            return False, str(e.args[0])
        except pyodbc.ProgrammingError as e:
            self.conn.rollback()  # Realiza rollback em caso de erro
            return False, str(e.args[0])
        except pyodbc.Error as e:
            self.conn.rollback()  # Realiza rollback em caso de erro
            return False, str(e.args[0])
        except Exception as e:
            self.conn.rollback()  # Realiza rollback em caso de erro
            return False, str(e)
        
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
                {"titulo": "Informações do Funcionario", "campos": ["Nome", "RG", "CPF", "Sexo", "Nascimento", "Email", "Setor", "Senha"]},
                {"titulo": "Cargo", "campos": ["Cargo", "Descricao", "Salario", "Data Inicio"]}
            ],
            "materia prima": [
                {"titulo": "Informações da Compra", "campos": ["CNPJ Fornecedor", "Data", "Materia Prima", "Quantidade"]}
            ],
            "novo produto": [
                {"titulo": "Informações do Produto", "campos": ["Novo produto", "Previsao de entrega(dias)"]}
            ]
        }

        grupos_campos = campos_por_tipo.get(self.tipo_cadastro, [])

        self.campos_relevantes = [
            campo for grupo in grupos_campos for campo in grupo["campos"]
        ]


        conteudo_dialog = [
            ft.Row(
                controls=[
                    ft.Text(f"Cadastro de {self.tipo_cadastro.capitalize()}", color=ft.colors.BLACK, size=20, weight="bold"),
                    ft.IconButton(icon=ft.icons.CLOSE, icon_color=ft.colors.BLACK, on_click=self._fechar_dialog)
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            )
        ]

        def criar_campo(nome_campo):
            if nome_campo in ("Data", "Data Inicio", "Data Fim", "Nascimento"):
                campo_texto = ft.TextField(label=nome_campo, read_only=True, width=200)
                botao_calendario = ft.IconButton(
                    icon=ft.icons.CALENDAR_TODAY,
                    tooltip=f"Selecionar {nome_campo}",
                    on_click=lambda e, dest=campo_texto: abrir_datepicker(e, dest)
                )
                self.inputs[nome_campo] = campo_texto
                return ft.Row(
                    controls=[campo_texto, botao_calendario],
                    alignment=ft.MainAxisAlignment.START
                )
            else:
                campo_texto = ft.TextField(label=nome_campo, color=ft.colors.BLACK, width=250)
                self.inputs[nome_campo] = campo_texto
                return campo_texto

        # Função para abrir o DatePicker
        def abrir_datepicker(e, campo_destino):
            self.page.dialog = ft.DatePicker(
                on_change=lambda event: on_date_selected(event, campo_destino),
                cancel_text="Cancelar",
                confirm_text="Confirmar"
            )
            self.page.dialog.open = True
            self.page.update()

        # Função chamada ao selecionar uma data
        def on_date_selected(event, campo_destino):
            try:
                data = datetime.strptime(event.data.split('T')[0], '%Y-%m-%d')
                campo_destino.value = data.strftime('%d-%m-%Y')
            except Exception as e:
                print(f"Erro ao selecionar a data: {e}")
            self.page.dialog.open = False
            self.page.update()

        # Itera pelos grupos e organiza os campos em colunas
        for grupo in grupos_campos:
            conteudo_dialog.append(ft.Text(grupo["titulo"], size=16, weight="bold", color=ft.colors.GREY))
            campos = grupo["campos"]

            linhas = []
            for i in range(0, len(campos), 2):
                linha = []
                linha.append(criar_campo(campos[i]))
                if i + 1 < len(campos):
                    linha.append(criar_campo(campos[i + 1]))
                linhas.append(ft.Row(controls=linha, alignment=ft.MainAxisAlignment.START))

            conteudo_dialog.extend(linhas)

        # Botão de salvar
        conteudo_dialog.append(
            ft.Row(
                controls=[
                    ft.ElevatedButton("Salvar", color=ft.colors.WHITE, bgcolor="#13330D", on_click=self._salvar_dados)
                ],
                alignment=ft.MainAxisAlignment.END
            )
        )

        # Criar o diálogo
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
        print(self.dados_salvos)

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
            ],
            "finalizar pedido": [
                {"titulo": "Finalizar Pedido", "campos": ["ID do Pedido"]}
            ]
        }

        grupos_campos = campos_por_tipo.get(self.tipo_cadastro, [])

        self.campos_relevantes = [
            campo for grupo in grupos_campos for campo in grupo["campos"]
        ]

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


        def criar_campo(nome_campo):
            if nome_campo in ("Data", "Data Pedido", "Data Inicio", "Data Fim"):
                campo_texto = ft.TextField(label=nome_campo, read_only=True, width=200)
                botao_calendario = ft.IconButton(
                    icon=ft.icons.CALENDAR_TODAY,
                    tooltip=f"Selecionar {nome_campo}",
                    on_click=lambda e, dest=campo_texto: abrir_datepicker(e, dest)
                )
                self.inputs[nome_campo] = campo_texto
                return ft.Row(
                    controls=[campo_texto, botao_calendario],
                    alignment=ft.MainAxisAlignment.START
                )
            elif nome_campo == "Duração":
                campo_texto = ft.TextField(label=nome_campo, read_only=True, width=200)
                botao_relogio = ft.IconButton(
                    icon=ft.icons.ACCESS_TIME,
                    tooltip=f"Selecionar {nome_campo}",
                    on_click=lambda e, dest=campo_texto: abrir_timepicker(e, dest)
                )
                self.inputs[nome_campo] = campo_texto
                return ft.Row(
                    controls=[campo_texto, botao_relogio],
                    alignment=ft.MainAxisAlignment.START
                )
            else:
                campo_texto = ft.TextField(label=nome_campo, color=ft.colors.BLACK, width=250)
                self.inputs[nome_campo] = campo_texto
                return campo_texto

        # Função para abrir o DatePicker
        def abrir_datepicker(e, campo_destino):
            self.page.dialog = ft.DatePicker(
                on_change=lambda event: on_date_selected(event, campo_destino),
                cancel_text="Cancelar",
                confirm_text="Confirmar"
            )
            self.page.dialog.open = True
            self.page.update()

        # Função para abrir o TimePicker
        def abrir_timepicker(e, campo_destino):
            self.page.dialog = ft.TimePicker(
                on_change=lambda event: on_time_selected(event, campo_destino),
                cancel_text="Cancelar",
                confirm_text="Confirmar"
            )
            self.page.dialog.open = True
            self.page.update()

        # Função chamada ao selecionar uma data
        def on_date_selected(event, campo_destino):
            try:
                data = datetime.strptime(event.data.split('T')[0], '%Y-%m-%d')
                campo_destino.value = data.strftime('%d-%m-%Y')
            except Exception as e:
                print(f"Erro ao selecionar a data: {e}")
            self.page.dialog.open = False
            self.page.update()

        # Função chamada ao selecionar uma hora
        def on_time_selected(event, campo_destino):
            try:
                tempo = event.data
                campo_destino.value = tempo
            except Exception as e:
                print(f"Erro ao selecionar o tempo: {e}")
            self.page.dialog.open = False
            self.page.update()

        # Itera pelos grupos e organiza os campos em colunas
        for grupo in grupos_campos:
            conteudo_dialog.append(ft.Text(grupo["titulo"], size=16, weight="bold", color=ft.colors.GREY))
            campos = grupo["campos"]

            linhas = []
            for i in range(0, len(campos), 2):
                linha = []
                linha.append(criar_campo(campos[i]))
                if i + 1 < len(campos):
                    linha.append(criar_campo(campos[i + 1]))
                linhas.append(ft.Row(controls=linha, alignment=ft.MainAxisAlignment.START))

            conteudo_dialog.extend(linhas)

        # Botão de salvar
        conteudo_dialog.append(
            ft.Row(
                controls=[
                    ft.ElevatedButton("Salvar", color=ft.colors.WHITE, bgcolor="#13330D", on_click=self._salvar_dados)
                ],
                alignment=ft.MainAxisAlignment.END
            )
        )

        # Criar o diálogo
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

    def _salvar_dados(self, e): 
        from app.components.validacao import Validacao

        # Filtra os campos que são obrigatórios para o tipo de cadastro atual
        campos_invalidos = [
            campo for campo, entrada in self.inputs.items()
            if not entrada.value.strip() and campo in self.campos_relevantes
        ]

        if campos_invalidos:
            # Exibe a mensagem de erro de acordo com os campos faltantes
            snackbar = ft.SnackBar(
                content=ft.Text(f"Os campos {', '.join(campos_invalidos)} não podem estar vazios!"),
                bgcolor=ft.colors.RED
            )
            self.page.overlay.append(snackbar)
            snackbar.open = True
            self.page.update()
            return
        
        
        # Coleta os dados dos inputs e fecha o dialog
        self.dados_salvos = {campo: entrada.value for campo, entrada in self.inputs.items()}

        # Valida o CPF antes de continuar
        if "CPF" in self.dados_salvos:
            cpf = self.dados_salvos["CPF"]
            if not Validacao.validar_cpf(cpf):  # Valida o formato do CPF
                snackbar = ft.SnackBar(
                    content=ft.Text("CPF inválido. Por favor, insira um CPF válido."),
                    bgcolor=ft.colors.RED
                )
                self.page.overlay.append(snackbar)
                snackbar.open = True
                self.page.update()
                return
        # Verificação do campo "Senha" e aplica hash
        if "Senha" in self.dados_salvos and self.dados_salvos["Senha"]:
            self.dados_salvos["Senha"] = self.hash_password(self.dados_salvos["Senha"])

        self.dados_salvos = self.converter_datas(self.dados_salvos)

        # Fecha o diálogo
        self.dialog.open = False
        self.page.update()


        # Insere os dados no banco e mostra o snackbar
        self.inserir_banco()

    def inserir_banco(self):
        from app.routes import Rotas
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
            Rotas.recarregar_pagina(self.page)
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
            Rotas.recarregar_pagina(self.page)

    def _fechar_dialog(self, e):
        from app.routes import Rotas
        # Fecha o diálogo sem salvar
        self.dialog.open = False
        self.page.update()
        Rotas.recarregar_pagina(self.page)
        
    def hash_password(self, password):
        """
        Recebe uma senha e retorna o hash com um salt.
        :param password: String com a senha em texto puro.
        :return: String com o hash da senha.
        """
        hashed = hashlib.sha256(password.encode('utf-8')).hexdigest()
        return hashed

    def converter_datas(self, dados):
        """
        Função que converte as datas no dicionário para o formato 'YYYY-MM-DD'
        """
        for campo, valor in dados.items():
            if campo in ["Data", "Data Pedido", "Data Inicio", "Data Fim", "Nascimento"]:  # Liste os campos de data
                try:
                    # Tentativa de conversão para o formato esperado 'YYYY-MM-DD'
                    dados[campo] = datetime.strptime(valor, "%d-%m-%Y").strftime("%Y-%m-%d")
                except ValueError:
                    print(f"Erro ao converter a data do campo {campo}. Valor fornecido: {valor}")
                    dados[campo] = None  # Ou defina um valor padrão, se necessário
        return dados

class Excluir:
    def __init__(self, page):
        """
        Inicializa a classe Excluir com a página onde o diálogo será exibido.
        :param page: A página do aplicativo onde o diálogo será mostrado.
        """
        self.page = page
        self.dialog_input = None
        self.dialog_confirmacao = None
        self.id_input = None
        self.nome_input = None
        self.tipo_entidade = None

    def abrir_dialogo_exclusao(self, tipo_entidade):
        """
        Abre um diálogo solicitando o ID para exclusão e configura a entidade correspondente.
        :param tipo_entidade: String representando o tipo de entidade a ser excluída (ex.: "fornecedor", "cliente").
        """
        self.tipo_entidade = tipo_entidade

        self.id_input = ft.TextField(label=f"ID do {tipo_entidade.capitalize()} a ser excluído", width=300, dense=True)

        self.dialog_input = ft.AlertDialog(
            bgcolor=ft.colors.WHITE,
            modal=True,
            title=ft.Text(f"Excluir {tipo_entidade.capitalize()}", size=20, color=ft.colors.BLACK, weight="bold"),
            content=ft.Column(
                [self.id_input],
                tight=True,
                spacing=10
            ),
            actions=[
                ft.TextButton("Próximo", on_click=self.confirmar_exclusao),
                ft.ElevatedButton("Cancelar", color=ft.colors.WHITE, bgcolor="#13330D", on_click=self.fechar_dialogo)
            ],
            actions_alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )

        self.page.overlay.append(self.dialog_input)
        self.dialog_input.open = True
        self.page.update()

    def confirmar_exclusao(self, e):
        from app.components.estoque import Estoque
        """
        Verifica o ID e abre um diálogo de confirmação antes de realizar a exclusão.
        :param e: Evento de clique.
        """
        id_para_excluir = self.id_input.value.strip()
        
        # Valida o Produto no Banco
        try:
            # Verificar se o ID foi fornecido
            if not id_para_excluir:
                mensagem = "Por favor, insira um ID válido."
            else:
                # Validar o produto no banco
                gb = GerenciamentoBanco()
                banco = Estoque(gb)
                produto = banco.validar_produto(id_produto=id_para_excluir)

                if not produto:
                    mensagem = f"Produto com ID {id_para_excluir} não encontrado."
                else:
                    # Produto encontrado, seguir com o diálogo de confirmação
                    self.dialog_confirmacao = ft.AlertDialog(
                        modal=True,
                        title=ft.Text("Confirmação de Exclusão", size=20, weight="bold"),
                        content=ft.Text(f"Tem certeza de que deseja excluir o {self.tipo_entidade.capitalize()} com ID {id_para_excluir}?"),
                        actions=[
                            ft.ElevatedButton("Excluir", on_click=lambda e: self.excluir_registro(e, id_para_excluir)),
                            ft.ElevatedButton("Cancelar", color=ft.colors.WHITE, bgcolor="#13330D", on_click=self.fechar_dialogo),
                        ],
                        actions_alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    )

                    self.fechar_dialogo()  # Fecha o diálogo anterior
                    self.page.overlay.append(self.dialog_confirmacao)
                    self.dialog_confirmacao.open = True
                    self.page.update()
                    return  # Sai da função para evitar exibir o Snackbar

                # Exibir Snackbar com a mensagem de erro
            snack_bar = ft.SnackBar(ft.Text(mensagem), bgcolor=ft.colors.RED)
            self.page.overlay.append(snack_bar)
            snack_bar.open = True
            self.page.update()

        except Exception as e:
            print(f"Erro ao validar produto: {e}")
            snack_bar = ft.SnackBar(
                ft.Text("Ocorreu um erro inesperado."), bgcolor=ft.colors.RED
            )
            self.page.overlay.append(snack_bar)
            snack_bar.open = True
            self.page.update()

    def excluir_registro(self, e, id_para_excluir):
        from app.components.estoque import Estoque
        from app.routes import Rotas
        """
        Realiza a exclusão do registro com base no tipo de entidade e ID fornecido.
        :param e: Evento de clique.
        :param id_para_excluir: ID do registro a ser excluído.
        """
        if self.tipo_entidade == "produto":
            gb = GerenciamentoBanco()
            banco = Estoque(gb)
            resultado = banco.excluir_produto(id_para_excluir)
        else:
            snack_bar = ft.SnackBar(ft.Text("Tipo de entidade desconhecido!"), bgcolor=ft.colors.RED)
            self.page.overlay.append(snack_bar)
            snack_bar.open = True
            self.page.update()
            return

        if resultado is True:
            snack_bar = ft.SnackBar(ft.Text(f"{self.tipo_entidade.capitalize()} com ID {id_para_excluir} excluído com sucesso!"), bgcolor=ft.colors.GREEN)
            Rotas.recarregar_pagina(self.page)
        else:
            snack_bar = ft.SnackBar(ft.Text(f"Erro ao excluir {self.tipo_entidade.capitalize()} com ID {id_para_excluir}!"), bgcolor=ft.colors.RED)
            Rotas.recarregar_pagina(self.page)

        self.page.overlay.append(snack_bar)
        snack_bar.open = True
        self.fechar_dialogo()
        self.page.update()

    def fechar_dialogo(self, e=None):
        from app.routes import Rotas
        """
        Fecha qualquer diálogo aberto.
        :param e: Evento de clique (opcional).
        """
        if self.dialog_input:
            self.dialog_input.open = False
        if self.dialog_confirmacao:
            self.dialog_confirmacao.open = False
        self.page.update()
        Rotas.recarregar_pagina(self.page)



class Atualizar:
    def __init__(self, page):
        """
        Inicializa a classe Atualizar com a página onde o diálogo será exibido.
        :param page: A página do aplicativo onde o diálogo será mostrado.
        """
        self.page = page
        self.dialog_atualizar = None
        self.rg_input = None
        self.senha_atual_input = None
        self.nova_senha_input = None
        self.confirma_nova_senha_input = None
        self.funcionario = None

    def abrir_dialogo_atualizar(self):
        """
        Abre um diálogo solicitando o RG, senha atual, nova senha e confirmação da nova senha para atualização.
        """
        self.rg_input = ft.TextField(label="RG do Funcionário", width=300, dense=True)
        self.senha_atual_input = ft.TextField(label="Senha Atual", width=300, password=True, dense=True)
        self.nova_senha_input = ft.TextField(label="Nova Senha", width=300, password=True, dense=True)
        self.confirma_nova_senha_input = ft.TextField(label="Confirmar Nova Senha", width=300, password=True, dense=True)
        
        # Diálogo para inserir RG e dados para atualização
        self.dialog_atualizar = ft.AlertDialog(
            bgcolor=ft.colors.WHITE,
            modal=True,
            title=ft.Text("Redefinir Senha", size=20, color=ft.colors.BLACK, weight="bold"),
            content=ft.Column([self.rg_input, self.senha_atual_input, self.nova_senha_input, self.confirma_nova_senha_input], tight=True, spacing=10),
            actions=[
                ft.ElevatedButton("Atualizar", on_click=self.verifica_senha),
                ft.ElevatedButton("Cancelar", color=ft.colors.WHITE, bgcolor="#13330D", on_click=self.fechar_dialogo)
            ],
            actions_alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )

        self.page.overlay.append(self.dialog_atualizar)
        self.dialog_atualizar.open = True
        self.page.update()

    def verifica_senha(self, e):
        from app.components.funcionario import Funcionario
        """
        Atualiza a senha do funcionário após validação dos campos.
        """
        rg = self.rg_input.value.strip()
        senha_atual = self.senha_atual_input.value.strip()
        nova_senha = self.nova_senha_input.value.strip()
        confirma_nova_senha = self.confirma_nova_senha_input.value.strip()

        print(f'RG do Funcionario: {rg}')
        print(f'Senha Atual: {senha_atual}')
        print(f'Nova senha: {nova_senha}')
        print(f'Confirma Nova Senha: {confirma_nova_senha}')

        # Validações
        if not rg or not senha_atual or not nova_senha or not confirma_nova_senha:
            self.exibir_snack_bar("Todos os campos devem ser preenchidos.", ft.colors.RED)
            return
        print('Todos os campos preenchidos')

        if nova_senha != confirma_nova_senha:
            self.exibir_snack_bar("A nova senha e a confirmação não coincidem.", ft.colors.RED)
            return
        print('Nova senha confirmada')
        print('Iniciando verificação do RG e Senha no banco de dados')

        banco = GerenciamentoBanco()
        funcionario = Funcionario(banco)

        senha_atual_hash = self.hash_password(senha_atual)
        # Consulta o funcionário pelo RG
        self.verificacao = funcionario.verifica_rg_senha(rg, senha_atual_hash)

        if not self.verificacao:
            self.exibir_snack_bar(f"Funcionário com RG {rg} não encontrado.", ft.colors.RED)
            return
        print('Verificação realizada com sucesso')

        # Criptografa a nova senha antes de salvar no banco
        nova_senha_hash = self.hash_password(nova_senha)
        print(f'Nova senha a ser cadastrada: {nova_senha_hash}')

        # Atualiza a senha no banco de dados
        sucesso = funcionario.atualizar_senha(rg, senha_atual_hash, nova_senha_hash)
        if sucesso:
            self.exibir_snack_bar("Senha atualizada com sucesso!", ft.colors.GREEN)
        else:
            self.exibir_snack_bar("Erro ao atualizar a senha.", ft.colors.RED)

        # Fecha o diálogo após atualização
        self.fechar_dialogo()

    def exibir_snack_bar(self, mensagem, cor):
        """
        Exibe uma mensagem de feedback na tela.
        :param mensagem: Mensagem a ser exibida no snackbar.
        :param cor: Cor de fundo do snackbar.
        """
        snack_bar = ft.SnackBar(ft.Text(mensagem), bgcolor=cor)
        self.page.overlay.append(snack_bar)
        snack_bar.open = True
        self.page.update()

    def fechar_dialogo(self, e=None):
        from app.routes import Rotas
        """
        Fecha o diálogo aberto.
        :param e: Evento de clique (opcional).
        """
        if self.dialog_atualizar:
            self.dialog_atualizar.open = False
        self.page.update()
        Rotas.recarregar_pagina(self.page)

    def hash_password(self, password):
        hashed = hashlib.sha256(password.encode('utf-8')).hexdigest()
        return hashed
    
    