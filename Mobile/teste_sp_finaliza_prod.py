import pyodbc

def finaliza_producao(id_plantio, data_fim, validade):
    # Conectar ao banco de dados
    conn = pyodbc.connect('Driver=ODBC Driver 17 for SQL Server;'
                          'Server=BRUNO-NOTE\SQLEXPRESS;'
                          'Database=teste;'
                          'Trusted_Connection=yes;')
    cursor = conn.cursor()

    try:
        # Executar a stored procedure para finalizar a produção
        cursor.execute("{CALL Finaliza_Producao (?, ?, ?)}", (id_plantio, data_fim, validade))

        # Commitar as mudanças
        conn.commit()
        print("Produção finalizada com sucesso!")

    except Exception as e:
        # Caso ocorra algum erro, reverter as mudanças
        conn.rollback()
        print(f"Erro ao finalizar a produção: {e}")

    finally:
        # Fechar a conexão
        cursor.close()
        conn.close()

# Função para coletar os dados do usuário
def questionario_finaliza_producao():
    print("Bem-vindo ao sistema de finalização de produção!")
    
    # Coletar informações do plantio
    id_plantio = input("Digite o ID do plantio: ")
    data_fim = input("Digite a data de finalização (YYYY-MM-DD): ")
    validade = int(input("Digite a validade do produto (em dias): "))
    
    # Chamar a função para finalizar a produção
    finaliza_producao(id_plantio, data_fim, validade)

# Executar o questionário
questionario_finaliza_producao()
