import flet as ft

def tela_cadastro(page, titulo, campos):
    # Função para salvar os dados (adapte para salvar no banco de dados)
    def salvar_dados(e):
        dados = {campo['label']: campo['input'].value for campo in campos}
        print("Dados salvos:", dados)
        # Aqui você poderia chamar uma função para salvar os dados no banco
        page.snack_bar = ft.SnackBar(ft.Text("Cadastro salvo com sucesso!"))
        page.snack_bar.open = True
        page.update()
        
    # Criação do layout principal
    page.title = f"Cadastro de {titulo}"
    form_campos = [
        ft.TextField(label=campo['label'], hint_text=campo.get('hint', '')) 
        for campo in campos
    ]
    for i, campo in enumerate(campos):
        campos[i]['input'] = form_campos[i]
    
    # Container principal da tela de cadastro
    page.add(
        ft.Container(
            content=ft.Column(
                [
                    ft.Text(f"Cadastro de {titulo}", size=24, weight=ft.FontWeight.BOLD),
                    *form_campos,
                    ft.Row(
                        controls=[
                            ft.ElevatedButton("Salvar", on_click=salvar_dados),
                            ft.ElevatedButton("Cancelar", on_click=lambda e: page.go('/'))
                        ],
                        alignment=ft.MainAxisAlignment.END
                    )
                ],
                spacing=10,
                horizontal_alignment=ft.CrossAxisAlignment.START,
            ),
            padding=20,
            margin=20,
            border=ft.border.all(color=ft.colors.GREY),
            border_radius=10,
            width=400,
            bgcolor=ft.colors.WHITE
        )
    )

# Exemplo de uso da função `tela_cadastro`
def main(page):
    # Definindo os campos de cadastro para cada tipo
    campos_fornecedor = [
        {'label': 'Nome do Fornecedor', 'hint': 'Digite o nome do fornecedor'},
        {'label': 'CNPJ', 'hint': 'Digite o CNPJ'},
        {'label': 'Endereço', 'hint': 'Digite o endereço'},
        {'label': 'Telefone', 'hint': 'Digite o telefone de contato'},
        {'label': 'Email', 'hint': 'Digite o email'}
    ]

    campos_cliente = [
        {'label': 'Nome do Cliente', 'hint': 'Digite o nome do cliente'},
        {'label': 'CPF/CNPJ', 'hint': 'Digite o CPF ou CNPJ'},
        {'label': 'Endereço', 'hint': 'Digite o endereço'},
        {'label': 'Telefone', 'hint': 'Digite o telefone de contato'},
        {'label': 'Email', 'hint': 'Digite o email'}
    ]

    campos_materia_prima = [
        {'label': 'Nome da Matéria-Prima', 'hint': 'Digite o nome da matéria-prima'},
        {'label': 'Descrição', 'hint': 'Digite uma descrição da matéria-prima'},
        {'label': 'Unidade de Medida', 'hint': 'Ex: Kg, Litros, Unidade'},
        {'label': 'Preço por Unidade', 'hint': 'Digite o preço por unidade'}
    ]

    # Escolhendo qual tela abrir (para teste, você pode trocar entre as chamadas)
    tela_cadastro(page, "Fornecedor", campos_fornecedor)
    # tela_cadastro(page, "Cliente", campos_cliente)
    # tela_cadastro(page, "Matéria Prima", campos_materia_prima)

ft.app(target=main)
