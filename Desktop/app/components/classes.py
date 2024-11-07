import flet as ft
import pyodbc

class Usuario:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome




class GerenciamentoBanco:
    def __init__(self):
        self.conn_str = (
            'Driver=ODBC Driver 17 for SQL Server;'
            'Server=BRUNO-NOTE\\SQLEXPRESS;'
            'Database=PIXFARM;'
            'Trusted_Connection=yes;'
        )

    def conectar(self):
        # Conecta ao banco de dados
        return pyodbc.connect(self.conn_str)

    def obter_plantas(self):
        # Obtém os dados das plantas
        conn = self.conectar()
        cursor = conn.cursor()
        query = '''SELECT Nome, URL FROM Materia_Prima'''
        # query = '''
        #     SELECT
	    #         Producao.Nome,
	    #         Materia_Prima.URL
        #     FROM Producao
        #     JOIN Materia_Prima ON Producao.fk_id_materia = Materia_Prima.id_materia
        #     '''
        cursor.execute(query)
        plantas = cursor.fetchall()
        conn.close()
        return plantas
    
    def obter_fornecedores(self):
        try:
            # Obtém os dados dos fornecedores
            conn = self.conectar()
            cursor = conn.cursor()
            query = '''SELECT id_fornecedor, Nome, CNPJ FROM Fornecedor'''
            cursor.execute(query)
            fornecedores = cursor.fetchall()
            conn.close()
            print(fornecedores)
            return fornecedores
        except Exception as e:
            print(f"Erro ao obter fornecedores: {e}")
            return None
        
    def obter_detalhes_fornecedores(self, id_fornecedor):
        try:
            # Obter os detalhes do fornecedor
            conn = self.conectar()
            cursor = conn.cursor()
            query = f'''SELECT * from Fornecedor WHERE id_fornecedor = {id_fornecedor}'''
            cursor.execute(query)
            detalhes_fornecedor = cursor.fetchone()
            conn.close()
            return detalhes_fornecedor
        except Exception as e:
            print(f"Erro ao obter detalhes do fornecedor: {e}")
            return None
        

    def obter_detalhes_plantio(self):
        conn = self.conectar()
        cursor = conn.cursor()
        query = '''
            SELECT
                id_plantio,
                Plantio,
                Data_Inicio,
                Nome,
                Quantidade
            FROM 
                Producao
        '''
        cursor.execute(query)
        detalhes = cursor.fetchall()
        conn.close()
        return detalhes

    def obter_clientes(self):
        try:
            conn = self.conectar()
            cursor = conn.cursor()
            query = '''SELECT id_cliente, Nome, CNPJ FROM Cliente'''
            cursor.execute(query)
            clientes = cursor.fetchall()
            conn.close()
            return clientes
        except Exception as e:
            print(f"Erro ao obter clientes: {e}")
            return None
        
    def obter_detalhes_clientes(self, id_cliente):
        try:
            # Obter os detalhes do fornecedor
            conn = self.conectar()
            cursor = conn.cursor()
            query = f'''SELECT * from Cliente WHERE id_cliente = {id_cliente}'''
            cursor.execute(query)
            detalhes_cliente = cursor.fetchone()
            conn.close()
            return detalhes_cliente
        except Exception as e:
            print(f"Erro ao obter detalhes do cliente: {e}")
            return None

    def cadastro(self, tipo_cadastro, dados):
        conn = self.conectar()
        cursor = conn.cursor()
        if tipo_cadastro == 'fornecedor':
            try:
                cursor.execute(
                    '''{CALL InserirFornecedor (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)}''', 
                        (dados['Nome'], dados['Nome Fantasia'], dados['CNPJ'], dados['Email'], dados['Telefone'], dados['Rua'], dados['Número'], dados['Bairro'], dados['CEP'], dados['Cidade'], dados['Estado'])
                        )
                conn.commit()
                print("Fornecedor inserido com sucesso.")
                return True
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
                cursor.close()
                conn.close()
                return False
            
        elif tipo_cadastro == 'cliente':
            try:
                cursor.execute(
                    '''{CALL InserirCliente (?, ?, ?, ?, ?, ?, ?, ?)}''',
                    (dados['Nome'], dados['CNPJ'], dados['Email'], dados['Rua'], dados['Numero'], dados['Bairro'], dados['CEP'], dados['Cidade'], dados['Estado'])
                    )
                conn.commit()
            except pyodbc.IntegrityError as e:
                print("Erro de integridade:", e)
            except pyodbc.ProgrammingError as e:
                print("Erro de programação:", e)
            except pyodbc.Error as e:
                print("Erro ao inserir fornecedor:", e)
            finally:
                cursor.close()
                conn.close()
            return False
        
        elif tipo_cadastro == 'compra':
            try:
                cursor.execute(
                    '''{CALL InserirCliente (?, ?, ?, ?, ?, ?, ?, ?)}''',
                    (dados['Nome'], dados['CNPJ'], dados['Email'], dados['Rua'], dados['Numero'], dados['Bairro'], dados['CEP'], dados['Cidade'], dados['Estado'])
                    )
                conn.commit()
            except pyodbc.IntegrityError as e:
                print("Erro de integridade:", e)
            except pyodbc.ProgrammingError as e:
                print("Erro de programação:", e)
            except pyodbc.Error as e:
                print("Erro ao inserir fornecedor:", e)
            finally:
                cursor.close()
                conn.close()
            return False
                
    

        


class Cadastro:
    def __init__(self, page):
        """
        Inicializa a classe Cadastro com a página onde o dialog será exibido.
        :param page: A página do aplicativo onde o dialog será mostrado.
        """
        self.page = page
        self.dialog = None
        self.inputs = {}
        self.dados_salvos = None  # Armazena temporariamente os dados salvos para possível reversão

    def abrir_dialog(self, tipo_cadastro):
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
                {"titulo": "Informações Básicas", "campos": ["Nome", "CNPJ", "Email"]},
                {"titulo": "Endereço", "campos": ["Rua", "Numero", "Bairro", "CEP", "Cidade", "Estado"]}
            ],
            "funcionario": [
                {"titulo": "Informações do Produto", "campos": ["Nome", "Código", "Descrição", "Preço", "Estoque"]}
            ],
            "teste": [
                {"titulo": "Informações do Produto", "campos": ["Nome", "Código", "Descrição", "Preço", "Estoque"]}
            ]
        }

        grupos_campos = campos_por_tipo.get(self.tipo_cadastro, [])

        conteudo_dialog = [
            ft.Row(
                controls=[
                    ft.Text(f"Cadastro de {self.tipo_cadastro.capitalize()}", size=20, weight="bold"),
                    ft.IconButton(icon=ft.icons.CLOSE, icon_color=ft.colors.BLACK, on_click=self._fechar_dialog)
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            )
        ]

        for grupo in grupos_campos:
            conteudo_dialog.append(ft.Text(grupo["titulo"], size=16, weight="bold", color=ft.colors.GREY))
            campos = grupo["campos"]
            self.inputs.update({campo: ft.TextField(label=campo, width=250) for campo in campos})
            for i in range(0, len(campos), 2):
                linha = ft.Row(
                    controls=[self.inputs[campos[j]] for j in range(i, min(i + 2, len(campos)))],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                )
                conteudo_dialog.append(linha)

        botoes = ft.Row(
            controls=[
                ft.ElevatedButton("Salvar", on_click=self._salvar_dados)
            ],
            alignment=ft.MainAxisAlignment.END
        )

        conteudo_dialog.append(botoes)

        self.dialog = ft.AlertDialog(
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
        print(f'Tipo de self.page: {type(self.page)}')

        self.page.overlay.append(self.dialog)
        self.dialog.open = True
        self.page.update()

    def _salvar_dados(self, e):
        # Coleta os dados dos inputs e fecha o dialog
        self.dados_salvos = {campo: entrada.value for campo, entrada in self.inputs.items()}
        print("Dados coletados:", self.dados_salvos)

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
                duration=3000
            )
            self.page.overlay.append(snackbar)
            snackbar.open = True
            self.page.update()

    def _fechar_dialog(self, e):
        # Fecha o diálogo sem salvar
        self.dialog.open = False
        self.page.update()




class Detalhes:
    def __init__(self, page):
        """
        Inicializa a classe DetalhesDialog para exibir os detalhes de uma entidade.
        :param page: A página onde o dialog será mostrado.
        :param banco: Instância de GerenciamentoBanco para consultar os dados.
        """
        self.page = page
        self.dialog = None
        self.em_edicao = False
        self.campos = {}



    def detalhes_fornecedor(self, id_fornecedor):
        banco = GerenciamentoBanco()
        """
        Abre um AlertDialog configurado para exibir detalhes do fornecedor com o ID fornecido.
        :param id_fornecedor: ID do fornecedor para buscar detalhes.
        """
        # Obter detalhes do fornecedor pelo ID
        detalhes = banco.obter_detalhes_fornecedores(id_fornecedor)

        if detalhes is None:
            self.page.snack_bar = ft.SnackBar(ft.Text("Erro ao obter detalhes do fornecedor"), bgcolor=ft.colors.RED)
            self.page.snack_bar.open = True
            self.page.update()
            print("Erro ao obter os detalhes do fornecedor.")
            return


        
        # Organizar os detalhes em um dicionário para exibição
        dados = {
            "ID": detalhes[0],
            "Nome": detalhes[1],
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
            campo = ft.TextField(value=str(valor), read_only=True)
            self.campos[titulo] = campo
            conteudo_dialog.append(
                ft.Row(
                    controls=[
                        ft.Text(f"{titulo}:", size=14, weight="bold"),
                        campo
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                )
            )

        botoes = ft.Row(
            controls=[
                ft.ElevatedButton("Editar", on_click=self._alternar_modo_edicao),
                ft.ElevatedButton("Fechar", on_click=self._fechar_dialog)
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )

        conteudo_dialog.append(botoes)

        # Configurar o diálogo com o conteúdo
        self.dialog = ft.AlertDialog(
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

        # Exibe o dialog
        self.page.overlay.append(self.dialog)
        self.dialog.open = True
        self.page.update()

    def detalhes_cliente(self, id_cliente):
        banco = GerenciamentoBanco()
        """
        Abre um AlertDialog configurado para exibir detalhes do fornecedor com o ID fornecido.
        :param id_fornecedor: ID do fornecedor para buscar detalhes.
        """
        # Obter detalhes do fornecedor pelo ID
        detalhes = banco.obter_detalhes_clientes(id_cliente)

        if detalhes is None:
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
                    ft.Text(f"Detalhes do Cliente", size=18, weight="bold"),
                    ft.IconButton(icon=ft.icons.CLOSE, icon_color=ft.colors.BLACK, on_click=self._fechar_dialog)
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            )
        ]

        # Adicionar os campos do dicionário `dados` ao diálogo
        for titulo, valor in dados.items():
            campo = ft.TextField(value=str(valor), read_only=True)
            self.campos[titulo] = campo
            conteudo_dialog.append(
                ft.Row(
                    controls=[
                        ft.Text(f"{titulo}:", size=14, weight="bold"),
                        campo
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                )
            )

        botoes = ft.Row(
            controls=[
                ft.ElevatedButton("Editar", on_click=self._alternar_modo_edicao),
                ft.ElevatedButton("Fechar", on_click=self._fechar_dialog)
            ],
            alignment=ft.MainAxisAlignment.END
        )

        conteudo_dialog.append(botoes)

        # Configurar o diálogo com o conteúdo
        self.dialog = ft.AlertDialog(
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

    def _alternar_modo_edicao(self, e):
        print("função editar ativando")
        """Alterna o modo de edição dos campos."""
        self.em_edicao = not self.em_edicao
        for campo in self.campos.values():
            campo.read_only = not self.em_edicao  # Alterna entre modo de edição e leitura
            campo.update()
        self.page.update()

    def _fechar_dialog(self, e=None):
        # Fecha o diálogo sem salvar
        self.dialog.open = False
        self.page.update()

    



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
