def somapositiva():
    acumulador = 0
    valueuser = -1 
    while valueuser != 0:
        valueuser= int(input("Digite um valor para somar(0 - parar)"))
        if valueuser > 0:
            acumulador_antes = acumulador
            acumulador += valueuser
            print (f"A soma de {valueuser} + {acumulador_antes} é = {acumulador}")
    return acumulador
       
                   
total = somapositiva()
print ("O total é:", total)