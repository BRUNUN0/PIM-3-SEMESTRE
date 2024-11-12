import hashlib
import flet as ft
import pyodbc
from hashlib import sha256

class GerenciamentoBanco:
    def __init__(self):
        # self.conn_str = (
        #     # BRUNO PC
        #     'Driver=ODBC Driver 17 for SQL Server;'
        #     'Server=BRUNUN;'
        #     'Database=PIXFARM;'
        #     'Trusted_Connection=yes;'
        # )
        self.conn_str = r'Driver=ODBC Driver 17 for SQL Server;Server=facu-pixfarm.czwmyguc4vet.sa-east-1.rds.amazonaws.com;Database=PIXFARM;UID=admin;PWD=pixfarm2024;'
        try:# testa para ver se o banco esta conectando ou não 
            conn = pyodbc.connect(self.conn_str)
            # ... (seu código para executar consultas)
        except pyodbc.Error as err:
            print("Error: ", err)
        finally:
            if conn:
                conn.close()
        self.conn = None
        self.cursor = None

    def conectar(self):
        # Conecta ao banco de dados
        if self.conn is None:
            self.conn = pyodbc.connect(self.conn_str)
            self.cursor = self.conn.cursor()

    def fechar_conexao(self):
        if self.conn:
            self.conn.close()
            self.conn = None
            self.cursor = None

    def grafico(self):
        try:
            self.conectar()
            query = '''SELECT 
                            FORMAT(Data_Inicio, 'MMM') AS Mes, 
                            SUM(Quantidade) AS Total_Quantidade
                        FROM 
                            Producao
                        GROUP BY 
                            FORMAT(Data_Inicio, 'MMM'), DATEPART(MONTH, Data_Inicio)
                        ORDER BY 
                            DATEPART(MONTH, Data_Inicio);'''
            self.cursor.execute(query)
            grafico = self.cursor.fetchall()
            return grafico
        except Exception as e:
            print(f"Erro ao obter grafico")
            self.fechar_conexao()
            return []




    def obter_funcionarios(self):
        try:
            self.conectar()
            query = '''SELECT 
                        f.id_funcionario AS id,
                        f.nome AS nome,
                        c.cargo AS cargo
                    FROM 
                        Funcionario f
                    INNER JOIN Cargo c ON f.fk_id_cargo = c.id_cargo;'''
            self.cursor.execute(query)
            clientes = self.cursor.fetchall()
            return clientes
        except Exception as e:
            print(f"Erro ao obter clientes: {e}")
            self.fechar_conexao()
            return None
    




    def obter_atividades(self):
        try:
            self.conectar()
            query = '''SELECT 
                        a.id_atividade,
                        p.Plantio AS nome_plantio,
                        a.Data
                    FROM 
                        Atividade a
                    INNER JOIN 
                        Funcionario f ON a.fk_id_funcionario = f.id_funcionario
                    INNER JOIN 
                        Producao p ON a.fk_id_Plantio = p.id_plantio;'''
            self.cursor.execute(query)
            atividades = self.cursor.fetchone()
            return atividades
        except Exception as e:
            print(f"Erro ao obter atividades: {e}")
            self.fechar_conexao()
            return None





    def atualizar_funcionario(self, dados_atualizados, id_funcionario):
        print(dados_atualizados)
        try:
            self.conectar()
            query = f'''UPDATE Funcionario SET  Nome = ?, Sexo = ?, Senha = ?, Nascimento = ?, Email = ?, Setor = ? WHERE id_funcionario = ?'''
            parametros = (
            dados_atualizados["Nome"],
            dados_atualizados["Sexo"],
            dados_atualizados["Senha"],
            dados_atualizados["Nascimento"],
            dados_atualizados["Email"],
            dados_atualizados["Setor"],
            id_funcionario
            )
            self.cursor.execute(query, parametros)
            self. conn.commit()
            return True
        except Exception as e:
            print(f"Erro ao atualizar dados do fornecedor {e}")
            self.fechar_conexao()
            return str(e)




        


    def obter_detalhes_funcionario(self, id_funcionario):
        try:
            # Obter detalhes do funcionario
            self.conectar()
            query = f'''SELECT
                            f.id_funcionario as id,
                            f.nome as nome,
                            f.CPF as cpf,
                            f.Sexo as sexo,
                            c.cargo as cargo,
                            f.senha as senha,
                            f.Nascimento as nascimento,
                            f.Email as email,
                            f.Setor as setor,
                            hc.Data_Inicio as data_inicio
                            FROM
                        Funcionario f
                        INNER JOIN Cargo c ON c.Cargo = c.Cargo
                        INNER JOIN Historico_Cargo hc ON hc.Data_Inicio = hc.Data_Inicio
                        WHERE id_funcionario = {id_funcionario}'''
            self.cursor.execute(query)
            detalhes_funcionario = self.cursor.fetchone()
            return detalhes_funcionario
        except Exception as e:
            print(f"Erro ao obter detalhes do funcionario: {e}")
            self.fechar_conexao()
            return None

    def obter_detalhes_materia_prima(self, id_materia):
        try:
            self.conectar()
            query = f'''SELECT
                        c.id_compra as id,
                        f.Nome_Fantasia as fornecedor,
                        f.CNPJ as cnpj,
                        mp.Nome as nome,
                        mp.Quantidade as quantidade,
                        c.Data_compra as data_compra,
                        mp.URL as url
                    FROM
                        Materia_Prima mp
                    INNER JOIN Compra c ON c.id_compra = c.id_compra
                    INNER JOIN Fornecedor f ON f.Nome_Fantasia = f.Nome_Fantasia
                    WHERE id_materia = {id_materia}'''
            self.cursor.execute(query)
            detalhes_materia_prima = self.cursor.fetchone()
            print(detalhes_materia_prima)
            return detalhes_materia_prima()
        except Exception as e:
            print(f"Erro ao obter detalhes da materia prima: {e}")
            self.fechar_conexao()
            return None

    def obter_detalhes_atividade(self, id_atividade):
        try:
            self.conectar()
            query = f'''SELECT 
                        a.id_atividade,
                        f.nome AS nome_funcionario,
                        p.Plantio AS nome_plantio,
                        a.Descricao,
                        a.Prioridade,
                        a.Duracao,
                        p.Fase_Atual
                    FROM 
                        Atividade a
                    INNER JOIN 
                        Funcionario f ON a.fk_id_funcionario = f.id_funcionario
                    INNER JOIN 
                        Producao p ON a.fk_id_Plantio = p.id_plantio
                    WHERE id_atividade = {id_atividade}'''
            self.cursor.execute(query)
            detalhes_atividade = self.cursor.fetchone()
            return detalhes_atividade
        except Exception as e:
            print(f"Erro ao obter detalhes da atividade: {e}")
            self.fechar_conexao()
            return None



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

    def obter_funcionario_login(self, cpf):

        try:
            self.conectar()
            print(cpf)
            self.cursor.execute( '''SELECT Senha, CPF, id_funcionario FROM Funcionario WHERE cpf = ?''', (cpf,))
            dados_login = self.cursor.fetchone()
            print(dados_login)
            return dados_login
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

        self.conectar()
        self.cursor.execute( '''SELECT senha, cpf, id_funcionario FROM Funcionario WHERE cpf = ?''', (cpf,))
        dados_login = self.cursor.fetchone()
        if dados_login:
            return dados_login
        return None  # Caso não encontre o CPF






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
    def __init__(self, page):
        """
        Inicializa a classe DetalhesDialog para exibir os detalhes de uma entidade.
        :param page: A página onde o dialog será mostrado.
        :param banco: Instância de GerenciamentoBanco para consultar os dados.
        """
        self.page = page
        self.dialog = None
        self.em_edicao = False
        self.botoes = None
        self.campos = {}
        self.campos_nao_editaveis = ["ID", "Nome/Razão Social", "CNPJ", "CPF", "Cargo", "Data inicial"]
#
    def detalhes_fornecedor(self, id_fornecedor):
        self.id_fornecedor_atual = id_fornecedor
        self._alternar_modo_edicao(None, tipo_entidade="fornecedor")
        banco = Fornecedor()
        """
        Abre um AlertDialog configurado para exibir detalhes do fornecedor com o ID fornecido.
        :param id_fornecedor: ID do fornecedor para buscar detalhes.
        """
        # Obter detalhes do fornecedor pelo ID
        detalhes = banco.obter_detalhes_fornecedores(id_fornecedor)

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
#
    def detalhes_cliente(self, id_cliente):
        self.id_cliente_atual = id_cliente
        self._alternar_modo_edicao(None, tipo_entidade="cliente")
        banco = Cliente()

        # Obter detalhes do fornecedor pelo ID
        detalhes = banco.obter_detalhes_clientes(id_cliente)

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

    def detalhes_materia_prima(self, id_materia):
        self.id_materia_atual = id_materia
        self._alternar_modo_edicao(None, tipo_entidade="materia_prima")
        banco = GerenciamentoBanco()

        # Obter detalhes do fornecedor pelo ID
        detalhes = banco.obter_detalhes_materia_prima(id_materia)

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

        # Obter detalhes do fornecedor pelo ID
        detalhes = banco.obter_detalhes_funcionario(id_funcionario)

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

    def detalhes_atividade(self, id_atividade):
        self.id_atividade_atual = id_atividade
        self._alternar_modo_edicao(None, tipo_entidade='atividade')
        banco = GerenciamentoBanco()

        detalhes = banco.obter_detalhes_atividade(id_atividade)
        print(detalhes)

        if detalhes is None:
            snackbar = ft.SnackBar(ft.Text("Erro ao obter detalhes da atividade."), bgcolor=ft.colors.RED)
            self.page.overlay.append(snackbar)
            snackbar.open = True
            self.page.update()
            return
        
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
        print(dados)

    def detalhes_producao(self, id_plantio):
        self.id_plantio_atual = id_plantio
        self._alternar_modo_edicao(None, tipo_entidade='producao')
        banco = Producao()

        detalhes = banco.obter_detalhes_plantio(id_plantio)

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

    def detalhes_pedido(self, id_pedido):
        self.id_pedido_atual = id_pedido
        self._alternar_modo_edicao(None, tipo_entidade='pedido')
        pedido = Pedido()

        detalhes = pedido.obter_detalhes_pedido(id_pedido)
        print(detalhes)

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

class Pedido(GerenciamentoBanco):
    def __init__(self):
        super().__init__()

    def obter_pedidos_abertos(self):
        try:
            self.conectar()
            query = '''SELECT
                        pe.id_pedido,
                        c.Nome AS Nome_Cliente,
                        pd.Produto,
                        i.Quantidade
                    FROM
                        Pedido pe
                    INNER JOIN Item_Pedido i ON pe.id_pedido = i.fk_id_pedido
                    INNER JOIN Produto pd ON pd.id_produto = i.fk_id_produto
                    INNER JOIN Cliente c ON pe.fk_id_cliente = c.id_cliente
                    WHERE
                        pe.Status = 'Em andamento';'''
            self.cursor.execute(query)
            pedidos = self.cursor.fetchall()
            return pedidos
        except Exception as e:
            print(f"Erro ao obter pedidos: {e}")
            return None
        finally:
            self.fechar_conexao()

    def obter_pedidos_finalizados(self):
        try:
            self.conectar()
            query = '''SELECT
                        pe.id_pedido,
                        c.Nome AS Nome_Cliente,
                        pd.Produto,
                        i.Quantidade
                    FROM
                        Pedido pe
                    INNER JOIN Item_Pedido i ON pe.id_pedido = i.fk_id_pedido
                    INNER JOIN Produto pd ON pd.id_produto = i.fk_id_produto
                    INNER JOIN Cliente c ON pe.fk_id_cliente = c.id_cliente
                    WHERE
                        pe.Status = 'Finalizado';'''
            self.cursor.execute(query)
            pedidos = self.cursor.fetchall()
            return pedidos
        except Exception as e:
            print(f"Erro ao obter pedidos: {e}")
            self.fechar_conexao()
            return None
        
    def obter_detalhes_pedido(self, id_pedido):
        try:
            self.conectar()
            query = '''SELECT
                            pe.id_pedido,
                            c.Nome AS Nome_Cliente,
                            pe.Data_Pedido,
                            pd.Produto,
                            i.Quantidade AS Quantidade_Produto,
                            pd.Previsao AS Previsao_Entrega,
                            pe.Status AS Status_Pedido
                        FROM
                            Pedido pe
                        INNER JOIN Cliente c ON pe.fk_id_cliente = c.id_cliente
                        INNER JOIN Item_Pedido i ON pe.id_pedido = i.fk_id_pedido
                        INNER JOIN Produto pd ON pd.id_produto = i.fk_id_produto
                        WHERE
                            pe.id_pedido = ?;'''
            self.cursor.execute(query,(id_pedido))
            detalhes_pedido = self.cursor.fetchone()
            return detalhes_pedido
        except Exception as e:
            print(f"Erro ao obter detalhes do pedido: {e}")
            self.fechar_conexao()
            return None
        
class Fornecedor(GerenciamentoBanco):
    def __init__(self):
        super().__init__()

    def obter_fornecedores(self):
        try:
            # Obtém os dados dos fornecedores
            self.conectar()
            query = '''SELECT id_fornecedor, Nome_Fantasia, CNPJ FROM Fornecedor'''
            self.cursor.execute(query)
            fornecedores = self.cursor.fetchall()
            return fornecedores
        except Exception as e:
            print(f"Erro ao obter fornecedores: {e}")
            self.fechar_conexao()
            return None

    def obter_detalhes_fornecedores(self, id_fornecedor):
        try:
            # Obter os detalhes do fornecedor
            self.conectar()
            query = f'''SELECT * from Fornecedor WHERE id_fornecedor = {id_fornecedor}'''
            self.cursor.execute(query)
            detalhes_fornecedor = self.cursor.fetchone()
            return detalhes_fornecedor
        except Exception as e:
            print(f"Erro ao obter detalhes do fornecedor: {e}")
            self.fechar_conexao()
            return None

    def atualizar_fornecedor(self, dados_atualizados, id_fornecedor):
        try:
            self.conectar()
            query = '''UPDATE Fornecedor SET Nome_Fantasia = ?, Email = ?, Telefone = ?, Rua = ?, Numero = ?, Bairro = ?, CEP = ?, Cidade = ?, Estado = ? WHERE id_fornecedor = ?'''
            parametros = (
            dados_atualizados["Nome Fantasia"],
            dados_atualizados["Email"],
            dados_atualizados["Telefone"],
            dados_atualizados["Rua"],
            dados_atualizados["Número"],
            dados_atualizados["Bairro"],
            dados_atualizados["CEP"],
            dados_atualizados["Cidade"],
            dados_atualizados["Estado"],
            id_fornecedor  # Aqui é onde o ID do fornecedor é passado
            )
            self.cursor.execute(query, parametros)
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Erro ao atualizar dados do fornecedor: {e}")
            self.fechar_conexao()
            return str(e)
        
class Cliente(GerenciamentoBanco):
    def __init__(self):
        super().__init__()

    def obter_clientes(self):
        try:
            self.conectar()
            query = '''SELECT id_cliente, Nome, CNPJ FROM Cliente'''
            self.cursor.execute(query)
            clientes = self.cursor.fetchall()
            return clientes
        except Exception as e:
            print(f"Erro ao obter clientes: {e}")
            self.fechar_conexao()
            return None

    def obter_detalhes_clientes(self, id_cliente):
        try:
            # Obter os detalhes do cliente
            self.conectar()
            query = f'''SELECT * from Cliente WHERE id_cliente = {id_cliente}'''
            self.cursor.execute(query)
            detalhes_cliente = self.cursor.fetchone()
            return detalhes_cliente
        except Exception as e:
            print(f"Erro ao obter detalhes do cliente: {e}")
            self.fechar_conexao()
            return None

    def atualizar_cliente(self, dados_atualizados, id_cliente):
        try:
            self.conectar()
            query = '''UPDATE Funcionario SET  Nome_Fantasia = ?, Email = ?, Rua = ?, Numero = ?, Bairro = ?, CEP = ?, Cidade = ?, Estado = ? WHERE id_cliente = ?'''
            parametros = (
            dados_atualizados["Nome Fantasia"],
            dados_atualizados["Email"],
            dados_atualizados["Rua"],
            dados_atualizados["Número"],
            dados_atualizados["Bairro"],
            dados_atualizados["CEP"],
            dados_atualizados["Cidade"],
            dados_atualizados["Estado"],
            id_cliente  # Aqui é onde o ID do fornecedor é passado
        )
            self.cursor.execute(query, parametros)
            self.conn.commit()
        except Exception as e:
            print(f"Erro ao atualizar dados do fornecedor {e}")
            self.fechar_conexao()
            return str(e)

class Producao(GerenciamentoBanco):
    def __init__(self):
        super().__init__()

    def obter_producao(self):
        try:
            self.conectar()
            query = '''SELECT
                        p.id_plantio,
                        p.Plantio,
                        p.Nome,
                        p.Quantidade,
                        mp.URL
                    FROM Producao p
                    JOIN Materia_Prima mp ON p.fk_id_materia = mp.id_materia
                    WHERE p.Data_Fim IS NULL;'''
            self.cursor.execute(query)
            producao = self.cursor.fetchall()
            return producao
        except Exception as e:
            print(f"Erro ao obter producao: {e}")
            self.fechar_conexao()
            return []

    def obter_detalhes_plantio(self, id_plantio):
        try:
            self.conectar()
            query = f'''
                SELECT
                    id_plantio,
                    Plantio,
                    Data_Inicio,
                    Nome,
                    Quantidade
                FROM 
                    Producao
                WHERE id_plantio = {id_plantio}
            '''
            self.cursor.execute(query)
            detalhes = self.cursor.fetchone()
            return detalhes
        except Exception as e:
            print(f"Erro ao obter fornecedores: {e}")
            self.fechar_conexao()
            return None

class Estoque(GerenciamentoBanco):
    def __init__(self):
        super().__init__()

    def obter_produtos(self):
        try:
            self.conectar()
            query = '''SELECT
                        p.id_produto,
                        p.Produto,
                        p.Quantidade,
                        p.Previsao
                    FROM Produto p'''
            self.cursor.execute(query)
            produtos = self.cursor.fetchall()
            return produtos
        except Exception as e:
            print(f"Erro ao obter produtos: {e}")
            self.fechar_conexao()
            return None

    def obter_materia_prima(self):
        try:
            self.conectar()
            query = '''SELECT
                        mp.id_materia,
                        mp.Nome,
                        mp.Quantidade,
                        mp.URL
                    FROM Materia_Prima mp'''
            self.cursor.execute(query)
            materias_primas = self.cursor.fetchall()
            return materias_primas
        except Exception as e:
            print(f"Erro ao obter materias primas: {e}")
            self.fechar_conexao()
            return None



