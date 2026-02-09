payment = float(input("Qual é o seu pagamento por hora?: "))
dayhour = float(input("Quantas horas você tabalha por mês?:"))

print (f"Seu ganho por mês é: {payment*dayhour}")

paydaytwo = float(input("Se não sabe quanto ganha por hora, escreva aqui quanto ganha por mês:"))

print (f"Seu ganho por hora é: {paydaytwo/dayhour:.1f}")