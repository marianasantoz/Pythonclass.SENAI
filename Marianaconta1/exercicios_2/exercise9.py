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
    smaller = n2

else:
    smaller = n1

if  n3 < smaller:
    smaller = n3

if n1 != bigger and n1 != smaller:
    middleone = n1

if n2 != bigger and n2 != smaller:
    middleone = n2

if n3 != bigger and n3 != smaller:
    middleone = n3

print(f"O maior é {bigger} | o do meio é {middleone} |e o menor é {smaller}")