#HESAP MAKİNESİ

sayi1= int(input("İlk sayıyı giriniz: "))
sayi2= int(input("İkinci sayıyı giriniz: "))

islem= input("""Yapmak istediğiniz işlemi giriniz: 
             (Toplama: +, Çıkarma: -, Çarpma: *, Bölme: /)""")

if islem== "+":
    print("Sonuç: " + str(sayi1+sayi2))

elif islem== "-":
    print("Sonuç: " + str(sayi1-sayi2))

elif islem=="*":
    print("Sonuç: " + str(sayi1*sayi2))
    
elif islem=="/":
    print("Sonuç: " + str(sayi1/sayi2))
    