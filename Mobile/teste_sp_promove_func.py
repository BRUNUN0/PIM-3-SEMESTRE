import pyodbc
from datetime import datetime

def promover_funcionario(id_funcionario, novo_cargo, descricao, salario, data_promocao):
    # Conectar ao banco de dados
    conn = pyodbc.connect('Driver=ODBC Driver 17 for SQL Server;'
                          'Server=BRUNO-NOTE\SQLEXPRESS;'
                          'Database=teste;'
                          'Trusted_Connection=yes;')
    cursor = conn.cursor()

    try:
        # Executar a stored procedure para promover o funcionário
        cursor.execute("{CALL PromoverFuncionario (?, ?, ?, ?, ?)}", 
                       (id_funcionario, novo_cargo, descricao, salario, data_promocao))

        # Commitar as mudanças
        conn.commit()
        print("Funcionário promovido com sucesso!")

    except Exception as e:
        # Caso ocorra algum erro, reverter as mudanças
        conn.rollback()
        print(f"Erro ao promover o funcionário: {e}")

    finally:
        # Fechar a conexão
        cursor.close()
        conn.close()

# Função para coletar as informações da promoção
def questionario_promocao():
    print("Bem-vindo ao sistema de promoção de funcionário!")
    
    id_funcionario = int(input("Digite o ID do funcionário: "))
    novo_cargo = input("Digite o novo cargo: ")
    descricao = input("Digite a descrição do novo cargo: ")
    salario = float(input("Digite o salário do novo cargo: "))
    
    # Coletar a data de promoção
    data_promocao = input("Digite a data da promoção (YYYY-MM-DD): ")
    
    # Validar a data de promoção
    try:
        data_promocao = datetime.strptime(data_promocao, "%Y-%m-%d").date()
    except ValueError:
        print("Data inválida. Use o formato YYYY-MM-DD.")
        return

    # Chamar a função para promover o funcionário no banco de dados
    promover_funcionario(id_funcionario, novo_cargo, descricao, salario, data_promocao)

# Executar o questionário
questionario_promocao()
