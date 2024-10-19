import pyodbc 


# === Conexão Banco ===
dados_conexao = {
    "Driver={SQL Server};"
    "Server=TIN7069;"
    "Database=PIXFARM;"
}
conexao = pyodbc.connect(dados_conexao, autocommit= True)
print("conexão efetuada")
cursor = conexao.cursor()

# === Funções Banco ===

def DbcLogin():
    comando_login = "SELECT * FROM PIXFARM "
    
    return print(comando_login.tostring())


# === Funções back === 

def Login(login, senha):
    _ = False

    if(login):
        _ = True
    
    return _