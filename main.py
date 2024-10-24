import functions as fc
import os


def main():

    if(Vlogin()):
        Vhome()


# ===== Login


def Vlogin():
    f = False

    while f != True:
        print("=== LOGIN ===\n\n")

        login = input("Login: ")
        senha = input("Senha: ")


        _ = fc.Login(login, senha)
        if( _ != False):
            f = True
            print("+++++ Logado!!! +++ ")
            return f

# ====== Home

def Vhome():

    r = input(""" 
        [1]Fornecedores\n
        [2]Funcionarios\n
        [3]Clientes 
        
 """)










# === Declaração 

if __name__ == "__main__":
    main()
