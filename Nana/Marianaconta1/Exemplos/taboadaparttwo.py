print("bem-vindo a TABO, seu app de taboada para preguiçosos, favorita!")
tabunumber = int(input("Digite um número e saiba sua tabuada:"))
i = 5

while i <= 100:
    add = tabunumber * i
    print(f"{tabunumber} X {i} = {add}")
    i = i + 1 #incremento de 1 em 1
## or you could do like: print(f"{tabunumber} X {i} = {tabunumber * i}")

print("Finaldatabuada")