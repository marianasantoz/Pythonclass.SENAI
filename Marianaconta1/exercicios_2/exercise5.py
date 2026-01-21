aluno = input ("Olá! aluno(a), por favor digite seu nome para averiguar sua média:")

escolas = ("Dagmar Ribas Trindade" or "Cristina Goldstein Barreiros" or "Maria Theodora Pedreira de Freitas")

escola = input("Digite sua escola:")
if escola != escolas:
    print("Escola não encontrada!")
else:
    medip = float(input("Qual sua nota final em português?"))
    medim = float(input("Qual sua nota final em matemática?"))
    finalmedia = (medip + medim)/2
if finalmedia == 10:
        print("Parabéns, você atingiu menção honrosa!")
elif finalmedia >=7:
        print ("Aprovado!")
else:
    print("Reprovado!")