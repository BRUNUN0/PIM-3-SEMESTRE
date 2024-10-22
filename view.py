import functions as fc
import os


f = False

while f != True:
    print("=== LOGIN ===\n\n")

    login = input("Login: ")
    senha = input("Senha: ")


    _ = fc.Login(login, senha)

    if(_ == True):
        print("Login feito ")
        f = True
    else: 
        print("Login ou senha incorretos. ")
        f = False




