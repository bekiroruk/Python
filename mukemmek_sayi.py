sayi = int(input("Bir sayı giriniz: "))

i =1
toplam = 0

while(i<sayi):
    if(sayi % i == 0):
        toplam +=i
    i+=1
    
if(toplam==sayi):
    print(sayi,"Mükemmel bir sayıdır.")
else:
    print(sayi,"Mükemmel bir sayı değildir.")