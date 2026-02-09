from funçãosomar import countmore
from euachoquedeveserpar import ehpareimpah
def menu():
    opcao = input("[1] - somar\n[2] - Verificação de par\[0] - Sair\n")
    if opcao == "1":
        v1 = int(input("Digite o primeiro valor:"))
        v2 = int(input("Digite o segundo valor:"))
        print (countmore(v1, v2))
    elif opcao == "2":
        v1 = int(input("Digite o primeiro valor:"))
        if ehpareimpah(v1):
            print(ehpareimpah)
        else:
            print("Ímpar!")
    
    while opcao == "0":
        continueornot = input("Deseja continuar? 1 - sim 2 - não") 
        if continueornot == "1":
            menu()
        else:
            break
            print ("Sair")      
    return opcao

menu()                                                                   