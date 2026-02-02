print (" Bem-vindo a calculadora novo tech!")

n1 = int(input ("Insira um número:")) 
n2 = int(input("Insira outro número:"))
#Menu intereativo
choose = input("Escolha uma operação: [1]-Multiplicação\n[2]-Divisão\n[3]Adição\n[4]Subtração.")
nivel = input("Escolha o seu nível de entendimento:\n[1]-Adulto-Adolescente(+13)\n[2]-Crianças(2-12)...")
#ifelses
if choose == "1" and nivel == "2":
    print (f"O resultado é:{n1*n2}\n*Passo a passo*: Primeiro desenhe casas( a quantidade seria o segundo valor),\n e depois desenhe pessoas dentro das casas(quantidade equivalente ao primeiro numero)\nSome as pessoas de todas as casas e aí estará seu resultado")

elif choose == "2" and nivel == "2":
    print (f"O resultado é:{n1/n2}\n*Passo a passo*: Primeiro transforme o numero que deseja dividir em balas(maças, ovos e etc), em seguida, transforme o divisor em pessoas(ou qualquer coisa que desejar) e divida as balas entre as pessoas, se necessário corte a bala no meio, assim terá seu resultado")

elif choose == "3" and nivel == "2":
    print (f"O resultado é:{n1+n2}\n*Passo a passo*: Primeiro desenhe o primeiro valor(numero), como bolas de sorvete, em seguida desenhe o segundo número como mais bolas de sorvete,\n recorte todas as bolas de sorvete e empilhe,\n em seguida, conte quantas bolas tem no total, e tá pronto o sorvetinho! ")

elif choose == "4" and nivel == "2":
    print (f"O resultado é:{n1-n2}\n*Passo a passo*: Primeiro desenhe o primeiro valor(numero), como ursinhos, em seguida retire a quantidade de ursinhos equivalente ao segundo numero,\n exemplo: tenho {n1} ursinhos, se eu pegar {n2} ursinhos, vão ficar no papel apenas {n1-n2} ursinhos!\n porém, se você precisar de 10 ursinhos e só desenhou 11 ursinhos,\n então falta um ursinho, e você deve um urso, o resultado, neste caso seria -1\n pois você tem um ursinho a menos!")

elif choose == "1" and nivel == "1":
    print (f"O resultado é:{n1*n2}*Passo a passo*: multiplique o dividendo(neste caso o número {n1}) pelo multiplicador (neste caso o número {n2}) e obtenha o resultado. )")

elif choose == "2" and nivel == "1":
    print (f"O resultado é:{n1/n2}*Passo a passo*: repartir igualmente / separar em grupos.\nVocê usa quando quer dividir uma quantidade em partes iguais.\nExemplo:\n12 balas para 3 crianças:\n➡️ 12 ÷ 3 = 4\n(cada uma recebe 4)")

elif choose == "3" and nivel == "1":
    print (f"O resultado é:{n1+n2}*Passo a passo*:juntar / aumentar.\nVocê usa quando quer saber o total depois de colocar coisas juntas.\nExemplo:\nSe você tem 5 reais e ganha mais 3:\n➡️ 5 + 3 = 8")

elif choose == "4" and nivel == "1":
    print (f"O resultado é:{n1-n2}*Passo a passo*: tirar / diminuir / comparar diferença.\nVocê usa quando algo é retirado ou quando quer saber quanto falta ou qual a diferença entre dois valores.\nExemplo(tirar):\nVocê tinha 10 balas e comeu 4:\n➡️ 10 − 4 = 6")

else:
    print("erro!")