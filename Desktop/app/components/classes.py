from operator import truediv
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

    def inserir_fornecedor(self, nome, nome_fantasia, cnpj, email, telefone, rua, numero, bairro, cep, cidade, estado):
        conn = self.conectar()
        cursor = conn.cursor()
        try:
            cursor.execute('''
                CALL InserirFornecedor
                    @Nome = ?,
                    @Nome_Fantasia = ?,
                    @CNPJ = ?,
                    @Email = ?,
                    @Telefone = ?,
                    @Rua = ?,
                    @Numero = ?,
                    @Bairro = ?,
                    @CEP = ?,
                    @Cidade = ?,
                    @Estado = ?;
            ''', (nome, nome_fantasia, cnpj, email, telefone, rua, numero, bairro, cep, cidade, estado)
            )
            conn.commit()
            print("Fornecedor inserido com sucesso.")
        except pyodbc.IntegrityError as e:
            print("Erro de integridade:", e)
        except pyodbc.ProgrammingError as e:
            print("Erro de programação:", e)
        except pyodbc.Error as e:
            print("Erro ao inserir fornecedor:", e)
        finally:
            cursor.close()
            conn.close()
    

        

import flet as ft

class Cadastro:
    def __init__(self, page):
        """
        Inicializa a classe Cadastro com a página onde o dialog será exibido.
        :param page: A página do aplicativo onde o dialog será mostrado.
        """
        self.page = page
        self.dialog = None
        self.inputs = {}

    def abrir_dialog(self, tipo_cadastro):
        """
        Abre um AlertDialog configurado com os campos apropriados para o tipo de cadastro fornecido.
        :param tipo_cadastro: String representando o tipo de cadastro (ex.: "fornecedor", "cliente", "produto").
        """
        # Definição de campos para diferentes tipos de cadastro com subtítulos
        campos_por_tipo = {
            "fornecedor": [
                {"titulo": "Informações Básicas", "campos": ["Nome", "Nome Fantasia", "CNPJ", "Email", "Telefone"]},
                {"titulo": "Endereço", "campos": ["Rua", "Número", "Bairro", "CEP", "Cidade", "Estado"]}
            ],
            "cliente": [
                {"titulo": "Informações Básicas", "campos": ["Nome", "CPF", "Email", "Telefone"]},
                {"titulo": "Endereço", "campos": ["Endereço", "Cidade", "Estado"]}
            ],
            "produto": [
                {"titulo": "Informações do Produto", "campos": ["Nome", "Código", "Descrição", "Preço", "Estoque"]}
            ]
        }

        # Obter os campos específicos para o tipo de cadastro
        grupos_campos = campos_por_tipo.get(tipo_cadastro, [])

        # Criar campos de entrada organizados com subtítulos para cada seção
        conteudo_dialog = [
            ft.Text(f"Cadastro de {tipo_cadastro.capitalize()}", size=20, weight="bold")
        ]

        for grupo in grupos_campos:
            # Adicionar subtítulo para cada grupo
            conteudo_dialog.append(ft.Text(grupo["titulo"], size=16, weight="bold", color=ft.colors.GREY))
            
            # Organizar os campos de entrada para cada grupo em linhas de dois elementos
            campos = grupo["campos"]
            self.inputs.update({campo: ft.TextField(label=campo, width=250) for campo in campos})
            for i in range(0, len(campos), 2):
                linha = ft.Row(
                    controls=[self.inputs[campos[j]] for j in range(i, min(i+2, len(campos)))],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                )
                conteudo_dialog.append(linha)

        # Botões para salvar e fechar o diálogo
        botoes = ft.Row(
            controls=[
                ft.ElevatedButton("Salvar", on_click=self._salvar_dados),
                ft.TextButton("Fechar", on_click=self._fechar_dialog)
            ],
            alignment=ft.MainAxisAlignment.END
        )

        conteudo_dialog.append(botoes)

        # Criar o AlertDialog com tamanho e organização controlados
        self.dialog = ft.AlertDialog(
            modal=True,
            content=ft.Container(
                width=550,  # Largura controlada do diálogo
                content=ft.Column(
                    controls=conteudo_dialog,
                    alignment=ft.MainAxisAlignment.START,
                    scroll=ft.ScrollMode.AUTO  # Adiciona scroll para campos extras
                )
            )
        )

        # Exibir o diálogo
        self.page.dialog = self.dialog
        self.dialog.open = True
        self.page.update()

    def _salvar_dados(self, e):
        # Coleta os dados dos inputs e fecha o dialog
        dados = {campo: entrada.value for campo, entrada in self.inputs.items()}
        print("Dados coletados:", dados)
        
        self.dialog.open = False
        self.page.update()

    def _fechar_dialog(self, e):
        # Fecha o diálogo sem salvar
        self.dialog.open = False
        self.page.update()
