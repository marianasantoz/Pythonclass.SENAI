def ehpar(numero):

    number = numero % 2 == 0
    if number:
        print("ehpar")
    else:
        print("ehpreda")
    return(numero)#

oqdf = int(input("qual o numero q vc quer?"))
ehpareimpah = ehpar(oqdf)

print(ehpareimpah)

