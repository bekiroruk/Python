bakiye = 1000

while True:
    işlem = input("İşlemi seçiniz: ")
    
    if(işlem=="q"):
        print("Yine bekleriz")
        break
        
        
    elif(işlem =="1"):
        print("Bakiyeniz {} tl'dir".format(bakiye))
        
        
    elif(işlem =="2"):
        miktar = int(input("Miktar giriniz:"))
        bakiye +=miktar
        
        
    elif(işlem =="3"):
        miktar = int(input("Miktar giriniz:"))
        if(bakiye - miktar < 0):
            print("Böyle bir miktar çekemezsiniz")
            continue
        bakiye -=miktar
        
    else:
        print("Geçersiz işlem...")
        