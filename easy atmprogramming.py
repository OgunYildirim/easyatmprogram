
print(""" ATM PROGRAMI YAPACAĞIZ 
      İŞLEMLER 
1- PARA ÇEKME
2- PARA YATIRMA (MİNİMUM 10 TL YATIRILMAKTADIR)
3 - BAKİYE SORGULAMA
Çıkmak için ^q^ basın
 !          """)
print("Mevcut bakiyeniz 1000 YTL ")

Bakiyemiz=1000

while True :

    x=(input("Yapacağınız işlem numarasını seçiniz :"))


    if  x == "q" :        
        print("İşleminiz sonlandırılıyor ...")
        break
    
    elif x == "1" :
        çekilcek_tutar=int(input("çekmek istediğiniz tutarı giriniz :"))
        if çekilcek_tutar > Bakiyemiz :
            print("Bakiyeniz yetersizdir daha düşük miktar çekmeyi deneyin !")
        else:
            print("{} YTL çekiliyor".format(çekilcek_tutar))
            Bakiyemiz = Bakiyemiz - çekilcek_tutar
            print( "Yeni bakiyeniz :",Bakiyemiz)
    

    elif x == "2" :
        yatırılacak_tutar=int(input("Yatırmak istediğiniz miktarı giriniz :"))
        if yatırılacak_tutar < 10 :
            print("Minumum yatırma tutarına uymamaktasınız işleminiz gerçekleştiriilemedi")
            break
        else:
            Bakiyemiz = yatırılacak_tutar + Bakiyemiz
            print("Yeni bakiyeniz :",Bakiyemiz)

    
    elif x == "3" :
        print("Bakiyeniz {} YTL ' dir ".format(Bakiyemiz))
    
    else :
        print("Seçenekler arasında böyle bir tuşlama yoktur")
        