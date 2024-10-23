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

def DbcLogin(login):

    cursor = conn.cursor()
    cursor.execute(f"SELECT Nome, Senha, id_login FROM Funcionario WHERE id_login = ?", login)
    con_bd = cursor.fetchone() # Retorna uma tupla com a seguinte sequencia (Nome | Senha | Login)
    print(con_bd)
    return con_bd


# === Funções back === 


def Login(login, senha):
    r = False
    nome_senha = DbcLogin(login)


    print("Nome: ", nome_senha[0], " Login: ", nome_senha[2] ,' Senha: ', nome_senha[1] )
    print("\n---------\n")

    if(login == nome_senha[2] and senha == nome_senha[1]):
        r = True
        return r
    else: print("Senha ou Lgoin incorretos.")
    