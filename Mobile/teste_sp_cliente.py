import pyodbc

def cadastrar_cliente(nome, cnpj, email, rua, numero, bairro, cep, cidade, estado):
    # Conectar ao banco de dados
    conn = pyodbc.connect('Driver=ODBC Driver 17 for SQL Server;'
                          'Server=BRUNO-NOTE\SQLEXPRESS;'
                          'Database=teste;'
                          'Trusted_Connection=yes;')
    cursor = conn.cursor()

    try:
        # Executar a stored procedure para cadastrar cliente
        cursor.execute("{CALL InserirCliente (?, ?, ?, ?, ?, ?, ?, ?, ?)}", 
                       (nome, cnpj, email, rua, numero, bairro, cep, cidade, estado))

        # Commitar as mudanças
        conn.commit()
        print("Cliente cadastrado com sucesso!")

    except Exception as e:
        # Caso ocorra algum erro, reverter as mudanças
        conn.rollback()
        print(f"Erro ao cadastrar o cliente: {e}")

    finally:
        # Fechar a conexão
        cursor.close()
        conn.close()

# Função para coletar as informações do cliente
def questionario_cliente():
    print("Bem-vindo ao cadastro de cliente!")
    
    # Coletar informações do cliente
    nome = input("Digite o nome do cliente: ")
    cnpj = input("Digite o CNPJ do cliente (apenas números): ")
    email = input("Digite o e-mail do cliente: ")
    rua = input("Digite a rua do cliente: ")
    numero = input("Digite o número do cliente: ")
    bairro = input("Digite o bairro do cliente: ")
    cep = input("Digite o CEP do cliente (apenas números): ")
    cidade = input("Digite a cidade do cliente: ")
    estado = input("Digite o estado do cliente (sigla): ")
    
    # Chamar a função para cadastrar o cliente no banco de dados
    cadastrar_cliente(nome, cnpj, email, rua, numero, bairro, cep, cidade, estado)

# Executar o questionário
questionario_cliente()
