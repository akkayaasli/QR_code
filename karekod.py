
import urllib.parse
import urllib.request 
try:    
    size=input("Görsel Boyutu:")  
    veriAdress=input("Karekoda dönüştürmek istediğiniz içeriği giriniz:(Örnek:www.vackerlite.com):") 
    imageName=input("Hangi isimle kayıt edilsin:")
    imageName=imageName+".png"
     #API linki 
    veriler={ 
        'size':size+"x"+size,
        'data':veriAdress
    } 
    #Url e uygun veri şifrelenmesi 
    parametreler=urllib.parse.urlencode(veriler) 
    #API linki oluşturuluyor. 
    apiAdress="https://api.qrserver.com/v1/create-qr-code/?"+parametreler 
    #Resim dosyasını indirmek.   
    urllib.request.urlretrieve(apiAdress,imageName) 
    print("\n")
    print("Kare kod başarıyla oluşturuldu.")
    print("Kare kodunuz "+ imageName +" isimli dosya olarak kayıt edildi.") 
except:
    print("Bir Hata Oluştu")

# / ASCII'de=>%2F
