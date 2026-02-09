##Monitorar saúde dos pacientes com IMC
user = input("Insira seu nome e sobrenome:")
gender = input("Qual é o seu gênero biológico?1Masculino, 2Feminino")

if gender == 1:
    print(f"Bem vindo!{user}")
else:
    print(f"Bem vinda!{user}")

weight = float(input("Qual é o seu peso atual?(centimetros)"))
height = float(input("Qual é a sua altura?"))

womanimc = weight / (height**2)

if womanimc >= 40:
    print ("Você está em estado de obesidade mórbida,\n por favor procurar uma nutricionista urgentemente!")
elif womanimc >= 35:
    print ("Você está em estado de obesidade tipo II, consulte um nutricionista")
elif womanimc >= 30:
    print ("Você está em estado de obesidade tipo I, consulte um nutricionista")
elif womanimc >= 25:
    print ("Você está em estado de sobre peso, consulte um nutricionista")
elif womanimc >= 18:
    print ("Você está com um IMC adequado, tudo bem por aqui!\n em caso de duvidas, uma nutricionista é sempre indicada!")
else:
    print ("Você está abaixo do peso! Consulte um nutricinista.")

