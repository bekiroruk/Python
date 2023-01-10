def okek_bulma(sayi1,sayi2):
    
    i = 1
    okek = 1
    
    while (i <= sayi1 and i <= sayi2):
        
        if( not (sayi1 % i) or not (sayi2 % i)):
            okek += i
    
        i+=1
    return okek






sayi1 = int(input("Sayi1: "))
sayi2 = int(input("Sayi2: "))

print("Obeb",okek_bulma(sayi1,sayi2))