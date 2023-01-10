def obeb_bulma(sayi1,sayi2):
    
    i = 1
    obeb = 1
    
    while (i <= sayi1 and i <= sayi2):
        
        if( not (sayi1 % i) and not (sayi2 % i)):
            obeb = i
    
        i+=1
    return obeb




sayi1 = int(input("Sayi1: "))
sayi2 = int(input("Sayi2: "))

print("Obeb",obeb_bulma(sayi1,sayi2))