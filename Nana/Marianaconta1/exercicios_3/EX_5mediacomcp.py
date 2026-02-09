total = int(0)
contador = 0

while True:
    digit = int(input("Digite um número...(digite 0 para parar)"))
    contador = contador + 1
    if digit == 0:
        break
    
    total += digit 
    
print (f"a média é: {total/contador}")
