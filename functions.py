import pyodbc 


# === Conexão Banco ===
def connect_to_sql_server():
    cnn_str = r'Driver={SQL Server};Server=TIN7069\SQLEXPRESS;Database=PIXFARM;'

    try:
        conn = pyodbc.connect(cnn_str)
        return conn
    except pyodbc.Error as e:
        print(f"Erro ao conectar ao SQL Server: {e}")
        return None
   



# === Funções Banco ===

def DbcLogin():
    comando_login = "SELECT 'Nome', 'Senha' FROM PIXFARM "
    
    return print(comando_login.tostring())


# === Funções back === 

def Login(login, senha):
    _ = False

    if(login):
        _ = True
    
    return _