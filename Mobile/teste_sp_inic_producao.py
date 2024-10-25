import pyodbc

def iniciar_producao(plantio, id_materia, nome, quantidade, data_inicio):
    # Conectar ao banco de dados
    conn = pyodbc.connect('Driver=ODBC Driver 17 for SQL Server;'
                          'Server=BRUNO-NOTE\SQLEXPRESS;'
                          'Database=teste;'
                          'Trusted_Connection=yes;')
    cursor = conn.cursor()

    try:
        # Verificar se o id_materia existe na tabela Materia_Prima
        cursor.execute("SELECT Quantidade FROM Materia_Prima WHERE id_materia = ?", (id_materia,))
        resultado = cursor.fetchone()
        
        if resultado:
            quantidade_disponivel = resultado[0]
            
            # Verificar se há quantidade suficiente
            if quantidade_disponivel >= quantidade:
                # Inserir os dados na tabela Item_Producao
                cursor.execute("""
                    INSERT INTO Producao (Plantio, fk_id_materia, Nome, Quantidade, Data_Inicio, Fase_Atual)
                    VALUES (?, ?, ?, ?, ?, 'Iniciada')
                """, (plantio, id_materia, nome, quantidade, data_inicio))

                # Subtrair a quantidade da tabela Materia_Prima
                cursor.execute("""
                    UPDATE Materia_Prima
                    SET Quantidade = Quantidade - ?
                    WHERE id_materia = ?
                """, (quantidade, id_materia))

                # Commitar as mudanças
                conn.commit()
                print("Produção iniciada com sucesso!")

            else:
                print("Quantidade insuficiente na matéria-prima. Operação cancelada.")
        
        else:
            print("ID da matéria-prima não encontrado. Operação cancelada.")

    except Exception as e:
        # Caso ocorra algum erro, reverter as mudanças
        conn.rollback()
        print(f"Erro ao iniciar a produção: {e}")

    finally:
        # Fechar a conexão
        cursor.close()
        conn.close()

# Função para coletar as informações da nova produção
def questionario_producao():
    print("Bem-vindo ao cadastro de nova produção!")

    # Coletar informações da nova produção
    plantio = input("Digite o nome da produção: ")
    id_materia = int(input("Digite o ID da matéria-prima: "))
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade a ser utilizada: "))
    data_inicio = input("Digite a data de início (AAAA-MM-DD): ")

    # Chamar a função para iniciar a produção no banco de dados
    iniciar_producao(plantio, id_materia, nome, quantidade, data_inicio)

# Executar o questionário
questionario_producao()
