def calciomedia(n1,n2,n3):
    calculo = (n1 + n2 + n3)/3
    if calculo >= 7:
        print("A média é maior ou igual a 7!")
        print (f"A média é {calculo:.0f}")
    else:
        print("A media é menor que sete, uma pena.")
        
    return not(print(calculo))

n1 = float(input("Digite um número:..."))
n2 = float(input("Digite um número:..."))
n3 = float(input("Digite um número:..."))
ohana = calciomedia(n1,n2,n3)
print (ohana)
