
numero = int(input("Digite o número da tabuada que deseja: "))
inicio_tabuada = int(input("Digite o início da tabuada: "))
fim_tabuada = int(input("Digite o final da tabuada: "))


while inicio_tabuada <= fim_tabuada:
    print(f"{numero * inicio_tabuada}")
    inicio_tabuada += 1
