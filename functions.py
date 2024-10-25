import pyodbc 



con_bd = ()
# === Conexão Banco ===

cnn_str = r'Driver={SQL Server};Server=TIN7069\SQLEXPRESS;Database=PIXFARM;'

if(cnn_str):
    conn = pyodbc.connect(cnn_str)
    print("conexão com banco sucesso!! ")
else:
    print(f"Erro ao conectar ao SQL Server")
    
   

    
# === Funções Banco ===

def Dbc_Login(login):

    cursor = conn.cursor()
    cursor.execute(f"SELECT Nome, Senha, id_login FROM Funcionario WHERE id_login = ?", login)
    con_bd = cursor.fetchone() # Retorna uma tupla com a seguinte sequencia (Nome | Senha | Login)
    print(con_bd)
    return con_bd




#==== Funcionario =======
def Dbc_Funcionario_View():

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Funcionario")
    colunas = [desc[0] for desc in cursor.description]
    
    print(*colunas, sep='\t')# Imprimindo o cabeçalho da tabela
    for row in cursor:
        print(*row, sep='\t')# Imprimindo os dados
    


def Dbc_Funcionario_Add(nome, cpf, sexo, senha, nascimento, email, setor, data, login):

    cursor = conn.cursor()
    cursor.execute("INSERT INTO Funcionario (Nome, CPF, Sexo, Senha, Nascimento, Email, Setor, fk_Data_Inicio, id_login) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", nome, cpf, sexo, senha, nascimento, email, setor, data, login)
    cursor.commit()


def Dbc_Funcionario_Del(cpf):

    cursor = conn.cursor()
    cursor.execute("DELETE FROM Funcionario WHERE CPF = ?", cpf)
    cursor.commit()


# === Funções back === 


def Login(login, senha):
    r = False
    nome_senha = Dbc_Login(login)


    print("Nome: ", nome_senha[0], " Login: ", nome_senha[2] ,' Senha: ', nome_senha[1] )
    print("\n---------\n")

    if(login == nome_senha[2] and senha == nome_senha[1]):
        r = True
        return r
    else: print("Senha ou Lgoin incorretos.")


def Existe_Funcionario(cpf):

    cursor = conn.cursor()
    cursor.execute("SELECT Nome, Senha, id_login FROM Funcionario WHERE id_login = ?", cpf)
    

