usertime = input("Qual o período em que você estuda? M-matutino, V-vespertino, N-noturno...").upper()

if usertime == "v" or usertime == "V":
    print("Boa tarde!")
elif usertime == "m" or usertime == "M":
    print("Bom dia!")
elif usertime == "n"or usertime == "N":
    print("Boa noite")
else:
    print("Invalidez.")