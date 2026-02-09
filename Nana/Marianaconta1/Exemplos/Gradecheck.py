print ("Bem vindo estudante! vamos checar sua nota final!")

portaverage = float(input("Qual foi sua nota final em português?"))
mathaverage = float(input("Qual foi sua nota final em matemática?"))
geoaverage = float(input("Qual foi a sua nota final em geografia?"))

finalaverage = (portaverage + mathaverage + geoaverage)/3

if finalaverage >= 7:
    print ("Parabéns você passou!")
elif finalaverage >= 4:
    print ("Recuperação")
else:
    print ("Você reprovou!")
