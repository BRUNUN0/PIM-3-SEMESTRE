import pyodbc
from datetime import datetime

def registrar_compra(cnpj_fornecedor, data_compra, itens_compra):
    # Conectar ao banco de dados
    conn = pyodbc.connect('Driver=ODBC Driver 17 for SQL Server;'
                          'Server=BRUNO-NOTE\SQLEXPRESS;'
                          'Database=PIXFARM;'
                          'Trusted_Connection=yes;')
    cursor = conn.cursor()

    try:
        # Executar a stored procedure para registrar a compra
        cursor.execute("{CALL RegistrarCompra (?, ?, ?, ?)}", 
                       (cnpj_fornecedor, data_compra, itens_compra[0]['nome'], itens_compra[0]['quantidade']))
        
        # Para cada item na lista de itens de compra, chamar a stored procedure novamente
        for item in itens_compra[1:]:  # Ignorar o primeiro item, pois já foi usado na chamada anterior
            cursor.execute("{CALL RegistrarCompra (?, ?, ?, ?)}", 
                           (cnpj_fornecedor, data_compra, item['nome'], item['quantidade']))

        # Commitar as mudanças
        conn.commit()
        print("Compra cadastrada com sucesso!")

    except Exception as e:
        # Caso ocorra algum erro, reverter as mudanças
        conn.rollback()
        print(f"Erro ao cadastrar a compra: {e}")

    finally:
        # Fechar a conexão
        cursor.close()
        conn.close()

# Função para coletar as informações da compra
def questionario_compra():
    print("Bem-vindo ao cadastro de compras!")
    
    # Coletar informações do fornecedor
    cnpj_fornecedor = input("Digite o CNPJ do fornecedor: ")  # Modificado para CNPJ
    data_compra = input("Digite a data da compra (YYYY-MM-DD): ")
    
    # Validar a data da compra
    try:
        data_compra = datetime.strptime(data_compra, "%Y-%m-%d").date()
    except ValueError:
        print("Data inválida. Use o formato YYYY-MM-DD.")
        return

    # Coletar informações dos itens comprados
    itens_compra = []
    while True:
        nome_materia = input("Digite o nome da matéria-prima: ")
        quantidade = int(input(f"Digite a quantidade de '{nome_materia}': "))

        itens_compra.append({'nome': nome_materia, 'quantidade': quantidade})

        # Perguntar se deseja adicionar mais itens
        mais_itens = input("Deseja adicionar outro item? (s/n): ").lower()
        if mais_itens != 's':
            break

    # Chamar a função para registrar a compra no banco de dados
    registrar_compra(cnpj_fornecedor, data_compra, itens_compra)

# Executar o questionário
questionario_compra()
