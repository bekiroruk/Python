sys_kullanici_adi ="bekir"
sys_parola ="12345"

giris_hakki = 3

while True:
    kullanici_adi = input("Kullanici adi giriniz: ")
    parola = input("Parola giriniz: ")
    
    if(kullanici_adi != sys_kullanici_adi and parola == sys_parola):
        print("Kullanıcı adı hatalı...")
        giris_hakki -=1
    elif(kullanici_adi == sys_kullanici_adi and parola != sys_parola):
        print("Parola yanlış...")
        giris_hakki -=1
    elif(kullanici_adi != sys_kullanici_adi and parola != sys_parola):
        print("Kullanici adi ve parola yanlış...")
        giris_hakki -=1
    else:
        print("Sisteme başarıyla giriş yapıldı....")
        break
    if(giris_hakki==0):
        print("Giriş hakkınız kalmamıştır...")
        break
