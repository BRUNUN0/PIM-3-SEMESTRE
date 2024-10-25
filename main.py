import functions as fc
import os


def main():

    if(Vlogin()):
        Vhome()



# ==== Viwer

def Vlogin():
    f = False

    while f != True:
        print("=== LOGIN ===\n\n")

        login = input("Login: ")
        senha = input("Senha: ")


        _ = fc.Login(login, senha)
        if( _):
            f = True
            print("+++++ Logado!!! +++ ")
            return f
        else: ("não foi dessa vez")


def vFornecedores():
    
    _ = input(""" 
        [1]Vizualizar Fuornecedores
        [2]ADD Fornecedores
        [3]delete Fornecedores

""")
    if _ == 1:
        return 
    elif _ == 2:
        return 
    elif _ == 3:
        return 
    else:
        return "Valor inválido"
#---
    



def vFuncionario():
    
    t = input(""" 
        [1]Vizualizar Funcionarios
        [2]ADD Funcionario
        [3]delete Funcionario

""")
    if t == 1:
        return 
    elif t == 2:
        return 
    elif t == 3:
        return 
    else:
        return "Valor inválido"
#---



def vCliente():
    
    _ = input(""" 
        [1]Vizualizar FCliente
        [2]ADD Cliente
        [3]delete Cliente

""")
    if _ == 1:
        return 
    elif _ == 2:
        return 
    elif _ == 3:
        return 
    else:
        return "Valor inválido"

#---


# ====== Home

def Vhome():

    r = input(""" 
        [1]Fornecedores
        [2]Funcionarios
        [3]Clientes 
        
 """)
    if r == 1:
        return vFornecedores()
    elif r == 2:
        return vCliente()
    elif r == 3:
        return 
    else:
        return "Valor inválido"

        
        

#====

def deletar_funcionario():
    cpf = input("CPF: ")
    return fc.Dbc_Funcionario_Del(cpf)








# === Declaração 

if __name__ == "__main__":
    main()
