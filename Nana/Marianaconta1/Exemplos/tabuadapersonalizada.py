
number = int(input("digite um numero:"))
vi = int(input("Digite um numero para iniciar a tabuada:"))
vf = int(input("Digite um número para finalizar a tabuada:"))

for multiplicador in range (vi,(vf + 1)):
    vi = vi + 1
    print (number * multiplicador)
