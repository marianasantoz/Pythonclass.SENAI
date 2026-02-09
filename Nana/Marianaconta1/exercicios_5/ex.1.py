##conversão de moedas
usd_to_brl = 5.19
usd_to_jyp = 153.09

def conversor(valor):
    decision = input("Deseja converter que moeda?\n-----------------------------------------------------------\n Digite [1]  -  Real-->Dolar\n Digite [2] - Real-->Iene\n-----------------------------------------------------------\n Digite [3] - Dolar-->Real\n[4] - Dolar-->Iene\n[5] - Iene-->Dolar\n-----------------------------------------------------------\n [6]Iene-->Real\n-----------------------------------------------------------\n Escolha:...")
    if decision == "1":
        print(f"{valor/usd_to_brl:.2f}")
    elif decision == "2":
        print(f"{valor*(usd_to_jyp/usd_to_brl):.2f}")
    elif decision == "3":
        print(f"{valor*usd_to_brl:.2f}")
    elif decision == "4":
        print(f"{valor*usd_to_jyp:.2f}")
    elif decision == "5":
        print(f"{valor/usd_to_jyp:.2f}")
    elif decision == "6":
        print(f"{valor*(usd_to_brl/usd_to_jyp):.2f}")
    
    return decision

print("Bem vindo ao Atlas, o conversor para todo mundo!")
userchoose = float(input("Digite um valor:"))
conversor(userchoose)
desejac = input ("Deseja continuar? 0 - não")
    
while desejac != "0":
    print("Bem vindo ao Atlas, o conversor para todo mundo!")
    userchoose = float(input("Digite um valor:"))
    conversor(userchoose)
    desejac = input ("Deseja continuar? 0 - não, 1 - sim...")
    if desejac == "0":
        print("Fim de app")

