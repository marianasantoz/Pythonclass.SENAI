##Sexo
usersex = input("Qual é o seu sexo biológico?(F-Feminino, M-Masculino)").upper()

if usersex == "F":
    print("Feminino, reconhecido pelo sistema.")
elif usersex == "M":
    print("Masculino, reconhecido pelo sistema.")
else:
    print("Sexo inválido \ não reconhecido")