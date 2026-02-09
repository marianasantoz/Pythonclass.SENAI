name = input("Digite o nome:  ")
email = input("Digite o seu email: ")

with open("./person.text", "a", encoding='utf-8') as arquivo:
    arquivo.write(f"Nome: ♪{name:<20} | E-mail: {email:<20}|\n")