n1 = float(input("Hello please insert one number:"))
n2 = float(input("Hello please insert one number:"))
n3 = float(input("Hello please insert one number:"))

if n1 >= n2:
    bigger = n1

else:
    bigger = n2

if  n3 > bigger:
    bigger = n3
if n1 <= n2:
    smallest = n2

else:
    smallest = n1

if  n3 < smallest:
    smallest = n3


print(f"O maior número entre os três é {bigger} e o menor é {smallest}!")

