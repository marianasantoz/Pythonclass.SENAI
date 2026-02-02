def tabuada_app(numero):
    for otafumiga in range (1,11):
        
        print(f"A tabuada do numero é: {numero} X {otafumiga} = {numero*otafumiga}")
    return(numero)
    
    

julioprestes = int(input("quantas furmigas subiram na sua coxa?\nDigite o número da tabuada que você deseja saber.."))
print({tabuada_app(julioprestes)})