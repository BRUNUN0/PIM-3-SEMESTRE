import pyodbc
from datetime import datetime

def cadastrar_funcionario(nome, cpf, sexo, nome_cargo, descricao, salario, senha, nascimento, email, setor, data_inicio):
    # Conectar ao banco de dados
    conn = pyodbc.connect('Driver=ODBC Driver 17 for SQL Server;'
                          'Server=BRUNO-NOTE\SQLEXPRESS;'
                          'Database=teste;'
                          'Trusted_Connection=yes;')
    cursor = conn.cursor()

    try:
        # Executar a stored procedure para cadastrar funcionário
        cursor.execute("{CALL CadastrarFuncionario (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)}", 
                       (nome, cpf, sexo, nome_cargo, descricao, salario, senha, nascimento, email, setor, data_inicio))

        # Commitar as mudanças
        conn.commit()
        print("Funcionário cadastrado com sucesso!")

    except Exception as e:
        # Caso ocorra algum erro, reverter as mudanças
        conn.rollback()
        print(f"Erro ao cadastrar o funcionário: {e}")

    finally:
        # Fechar a conexão
        cursor.close()
        conn.close()

# Função para coletar as informações do funcionário
def questionario_funcionario():
    print("Bem-vindo ao cadastro de funcionário!")
    
    # Coletar informações do funcionário
    nome = input("Digite o nome do funcionário: ")
    cpf = input("Digite o CPF do funcionário (apenas números): ")
    sexo = input("Digite o sexo do funcionário (M/F): ")
    nome_cargo = input("Digite o nome do cargo: ")
    descricao = input("Digite a descrição do cargo: ")
    salario = float(input("Digite o salário do cargo: "))
    senha = input("Digite a senha: ")
    
    # Coletar a data de nascimento
    data_nascimento = input("Digite a data de nascimento do funcionário (YYYY-MM-DD): ")
    
    # Validar a data de nascimento
    try:
        data_nascimento = datetime.strptime(data_nascimento, "%Y-%m-%d").date()
    except ValueError:
        print("Data inválida. Use o formato YYYY-MM-DD.")
        return

    email = input("Digite o e-mail do funcionário: ")
    setor = input("Digite o setor do funcionário: ")
    
    # Coletar a data de início
    data_inicio = input("Digite a data de início do funcionário (YYYY-MM-DD): ")
    
    # Validar a data de início
    try:
        data_inicio = datetime.strptime(data_inicio, "%Y-%m-%d").date()
    except ValueError:
        print("Data inválida. Use o formato YYYY-MM-DD.")
        return

    # Chamar a função para cadastrar o funcionário no banco de dados
    cadastrar_funcionario(nome, cpf, sexo, nome_cargo, descricao, salario, senha, data_nascimento, email, setor, data_inicio)

# Executar o questionário
questionario_funcionario()
