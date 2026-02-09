n1 = float(input("Hello please insert one number:"))
n2 = float(input("Hello please insert one number:"))
n3 = float(input("Hello please insert one number:"))

if n1 == n2 and n3:
    print("São valores iguais!")
elif n1 > n2 and n3:
    print(f"O maior número entre os três é {n1}!")
elif n2 > n1 and n3:
    print(f"O maior número entre os três é {n2}!")
elif n3 > n1 and n2:
    print(f"O maior número entre os três é {n3}!")
else:
    print(f"O maior número é n3!")
    