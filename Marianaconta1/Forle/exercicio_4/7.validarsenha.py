from getpass import getpass
def passverify(senha):
    if len(senha) >= 8:
        print("Senha válida.")
        return True
    else:
        print("Senha inválida")
        return False
    

def cadastro_terminal():
    user = input("Digite o nome do usuário:")
    password = input("Digite uma senha de 8 digitos ou mais:")

    while not passverify(password):
        password = input("Digite uma senha de 8 digitos ou mais:")
    print("Cadastro realizado com sucesso!")

cadastro_terminal()   
   