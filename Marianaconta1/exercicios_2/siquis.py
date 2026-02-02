def contarpares(inicio,fim):
    contador = 0 
    for numero in range(inicio,fim+1):
        if numero % 2 == 0:
            contador += 1 
            print(contador)

contarpares(1,10)