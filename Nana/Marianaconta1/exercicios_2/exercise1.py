##Biggest number
n1 = float(input("Insert one number:"))
n2 = float(input("Insert one number:"))

if n1 > n2:
    if n1 == n2:
        print ("The numbers are the same.")
    else:
        print (f"The biggest number is {n1}")
        
else:
    print (f"The biggest number is {n2}")

