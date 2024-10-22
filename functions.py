import pyodbc 



con_bd = []
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
    cursor.execute("SELECT Nome, Senha, Login FROM Funcionario WHERE Login = ?", login)
    cursor.fetchone()# Retorna uma tupla com a seguinte sequencia (Nome | Senha | Login)
    for row in cursor:
        con_bd.append({'Nome': row[0], 'Senha': row[1], 'Login': row[2]})

    if con_bd:
        return Login(con_bd), print(con_bd)
    else: 
        for msg in cursor.messages:
            if msg.severity > 30:  # Ajustar o nível de severidade conforme necessário
                return str(msg)
        return None


# === Funções back === 


def Login(senha, login):
    r = False
    nome_senha = DbcLogin(login)
    print(nome_senha)
    