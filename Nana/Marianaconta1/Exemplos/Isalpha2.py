def iselfo(n1):
    n1.strip()
    check = n1.isalpha()
    if check == True:
        not(True)
    else: 
        print("Caractéres especiais e números não são aceitos!")

octable = input("Digite um nome:")
check = iselfo(octable)