try:
    value1  = float(input("Digite um número: "))
    print(5/value1)

except ZeroDivisionError:
    print("Não é possível dividir um número por zero. ")
    value1 = 1
except Exception as error:
    print("Ocorreu o erro:",error)
