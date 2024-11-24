import flet as ft
class ExemploApp(ft.UserControl):

    def __init__(self):
        self.inputs = {}
        self.dados_salvos = {}

        # Estrutura dos campos de cadastro
        self.dados_cadastro = {
            "funcionario": [
                {"titulo": "Informações do Funcionario", "campos": ["Nome", "RG", "CPF", "Sexo", "Nascimento", "Email", "Setor", "Senha"]},
                {"titulo": "Cargo", "campos": ["Cargo", "Descricao", "Salario", "Data Inicio"]}  # Data Inicio é o campo de data
            ]
        }

    def construir_inputs(self):
        # Construindo os campos de acordo com a estrutura de dados
        for categoria in self.dados_cadastro["funcionario"]:
            for campo in categoria["campos"]:
                if campo == "Data Inicio":
                    # Criando o DatePicker para 'Data Inicio'
                    self.inputs[campo] = ft.DatePicker(label=campo)
                else:
                    # Criando os campos de texto
                    self.inputs[campo] = ft.TextField(label=campo)

        # Adicionando os campos na interface
        for campo, campo_obj in self.inputs.items():
            self.page.add(campo_obj)

    def _salvar_dados(self, e):
        # Verificando a ordem dos dados
        print("Dados antes de salvar:", self.inputs)

        # Coletando os dados
        self.dados_salvos = {campo: entrada.value for campo, entrada in self.inputs.items()}

        # Verificando os dados coletados
        print('Dados coletados em _salvar_dados:', self.dados_salvos)

    def build(self):
        self.construir_inputs()
        botao_salvar = ft.ElevatedButton("Salvar", on_click=self._salvar_dados)
        self.page.add(botao_salvar)
