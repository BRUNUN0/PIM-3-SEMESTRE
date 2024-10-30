import pyodbc

def registrar_atividade(fk_id_funcionario, fk_id_plantio, descricao, prioridade, duracao, fase_atual):
    # Conectar ao banco de dados
    conn = pyodbc.connect('Driver=ODBC Driver 17 for SQL Server;'
                          'Server=BRUNO-NOTE\SQLEXPRESS;'
                          'Database=PIXFARM;'
                          'Trusted_Connection=yes;')
    cursor = conn.cursor()

    try:
        # Executar a stored procedure para registrar a atividade
        cursor.execute("{CALL RegistrarAtividade (?, ?, ?, ?, ?, ?)}", 
                       (fk_id_funcionario, fk_id_plantio, descricao, prioridade, duracao, fase_atual))

        # Commitar as mudanças
        conn.commit()
        print("Atividade registrada com sucesso!")

    except Exception as e:
        # Caso ocorra algum erro, reverter as mudanças
        conn.rollback()
        print(f"Erro ao registrar a atividade: {e}")

    finally:
        # Fechar a conexão
        cursor.close()
        conn.close()

# Função para coletar os dados do usuário
def questionario_registrar_atividade():
    print("Bem-vindo ao sistema de registro de atividades!")
    
    # Coletar informações da atividade
    fk_id_funcionario = input("Digite o ID do funcionário: ")
    fk_id_plantio = input("Digite o ID do plantio: ")
    descricao = input("Digite a descrição da atividade: ")
    prioridade = int(input("Digite a prioridade da atividade (1 a 10): "))
    duracao = input("Digite a duração da atividade (HH:MM:SS): ")
    fase_atual = input("Digite a fase atual da produção: ")  # Coletando a nova fase atual
    
    # Chamar a função para registrar a atividade
    registrar_atividade(fk_id_funcionario, fk_id_plantio, descricao, prioridade, duracao, fase_atual)

# Executar o questionário
questionario_registrar_atividade()
