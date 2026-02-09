nome = str(input ("What's your name?"))
idade = int(input("What's your age?"))
possuicarteira = input("Possui carteira?")

if idade >= 18:
    if possuicarteira == "Sim" or "sim" or "yes" or "Yes":
       print ("Pode dirigir")
    else:
        print ("Não pode dirigir")
else:
    print ("Menor de idade")        


