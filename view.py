import functions as fc


def main():
    return fc.connect_to_sql_server()



def Vlogin():
    print("=== LOGIN ===\n\n")
    login = input(print("Login: "))
    senha = input(print("Senha: "))
    
    _ = fc.Login(login, senha)

    if(_ == True):
        print("Login")
    else: print("Login ou senha incorretos. ")