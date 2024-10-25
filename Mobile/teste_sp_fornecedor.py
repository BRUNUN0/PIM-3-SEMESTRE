import pyodbc

def cadastrar_fornecedor(nome, nome_fantasia, cnpj, email, telefone, rua, numero, bairro, cep, cidade, estado):
    # Conectar ao banco de dados
    conn = pyodbc.connect('Driver=ODBC Driver 17 for SQL Server;'
                          'Server=BRUNO-NOTE\SQLEXPRESS;'
                          'Database=teste;'
                          'Trusted_Connection=yes;')
    cursor = conn.cursor()

    try:
        # Executar a stored procedure para cadastrar fornecedor
        cursor.execute("{CALL InserirFornecedor (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)}", 
                       (nome, nome_fantasia, cnpj, email, telefone, rua, numero, bairro, cep, cidade, estado))

        # Commitar as mudanças
        conn.commit()
        print("Fornecedor cadastrado com sucesso!")

    except Exception as e:
        # Caso ocorra algum erro, reverter as mudanças
        conn.rollback()
        print(f"Erro ao cadastrar o fornecedor: {e}")

    finally:
        # Fechar a conexão
        cursor.close()
        conn.close()

# Função para coletar as informações do fornecedor
def questionario_fornecedor():
    print("Bem-vindo ao cadastro de fornecedor!")
    
    # Coletar informações do fornecedor
    nome = input("Digite o nome do fornecedor: ")
    nome_fantasia = input("Digite o nome fantasia do fornecedor: ")
    cnpj = input("Digite o CNPJ do fornecedor (apenas números): ")
    email = input("Digite o e-mail do fornecedor: ")
    telefone = input("Digite o telefone do fornecedor: ")
    rua = input("Digite a rua do fornecedor: ")
    numero = input("Digite o número do fornecedor: ")
    bairro = input("Digite o bairro do fornecedor: ")
    cep = input("Digite o CEP do fornecedor (apenas números): ")
    cidade = input("Digite a cidade do fornecedor: ")
    estado = input("Digite o estado do fornecedor (sigla): ")
    
    # Chamar a função para cadastrar o fornecedor no banco de dados
    cadastrar_fornecedor(nome, nome_fantasia, cnpj, email, telefone, rua, numero, bairro, cep, cidade, estado)

# Executar o questionário
questionario_fornecedor()
