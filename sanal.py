# Öğrenci Bilgileri
class Ogrenci:
    def __init__(self, ad, soyad, numara):
        self.ad = ad
        self.soyad = soyad
        self.numara = numara

# Kütüphane Kitapları
class Kitap:
    def __init__(self, ad, yazar):
        self.ad = ad
        self.yazar = yazar

# Öğrenci ve Kitap Listeleri
ogrenci_listesi = []
kitap_listesi = []

# Sesli yanıt için bir motor oluşturun
import pyttsx3

# Sesli yanıt verme fonksiyonu
def speak_text(text):
    speak.say(text)
    speak.runAndWait()

speak = pyttsx3.init('sapi5')
voices = speak.getProperty('voices')
speak.setProperty('voice', voices[0].id)

# Kullanıcıdan adını al
ad = input("Adınızı girin: ")

# Kullanıcıya selam ver
speak_text(f"Merhaba, {ad}!")

# Kullanıcıdan yaşını al
yas = input("Yaşınızı girin: ")

# Yaşınızı ekranda göster
speak_text(f"{ad}, {yas} yaşındasınız.")

# Öğrenci Ekleme Fonksiyonu
def ogrenci_ekle():
    ad = input("Öğrenci adı: ")
    soyad = input("Öğrenci soyadı: ")
    numara = input("Öğrenci numarası: ")
    ogrenci = Ogrenci(ad, soyad, numara)
    ogrenci_listesi.append(ogrenci)
    speak_text(f"{ad} {soyad} öğrencisi eklendi.")

# Kitap Ekleme Fonksiyonu
def kitap_ekle():
    ad = input("Kitap adı: ")
    yazar = input("Kitap yazarı: ")
    kitap = Kitap(ad, yazar)
    kitap_listesi.append(kitap)
    speak_text(f"{ad} kitabı eklendi.")

# Öğrenci Listeleme Fonksiyonu
def ogrenci_listele():
    for ogrenci in ogrenci_listesi:
        print(f"Ad: {ogrenci.ad}, Soyad: {ogrenci.soyad}, Numara: {ogrenci.numara}")

# Kitap Listeleme Fonksiyonu
def kitap_listele():
    for kitap in kitap_listesi:
        print(f"Kitap Adı: {kitap.ad}, Yazar: {kitap.yazar}")

# Ana Menü
while True:
    print("\nOkul ve Kütüphane Programı")
    print("1. Öğrenci Ekle")
    print("2. Kitap Ekle")
    print("3. Öğrenci Listele")
    print("4. Kitap Listele")
    print("5. Öğrenci Kitap Alma")
    print("6. Öğrenci Kitap Teslim Etme")
    print("7. Çıkış")

    secim = input("Seçiminizi girin: ")

    if secim == '1':
        ogrenci_ekle()
    elif secim == '2':
        kitap_ekle()
    elif secim == '3':
        ogrenci_listele()
    elif secim == '4':
        kitap_listele()
    elif secim == '5':
        # Öğrenci kitap alma işlemi
        ogrenci_numara = input("Öğrenci numarasını girin: ")
        kitap_ad = input("Almak istediğiniz kitabın adını girin: ")
        # Burada öğrencinin kitap alma işlemini yapabilirsiniz
    elif secim == '6':
        # Öğrenci kitap teslim etme işlemi
        ogrenci_numara = input("Öğrenci numarasını girin: ")
        kitap_ad = input("Teslim etmek istediğiniz kitabın adını girin: ")
        # Burada öğrencinin kitap teslim etme işlemini yapabilirsiniz
    elif secim == '7':
        # Öğrenci ve kitap bilgilerini bir metin dosyasına kaydetmek için buraya kod ekleyebilirsiniz.
        # Örneğin, verileri bir metin dosyasına yazma:
        with open("okul_kutuphane_verileri.txt", "w") as dosya:
            dosya.write("Öğrenciler:\n")
            for ogrenci in ogrenci_listesi:
                dosya.write(f"Ad: {ogrenci.ad}, Soyad: {ogrenci.soyad}, Numara: {ogrenci.numara}\n")
            dosya.write("\nKitaplar:\n")
            for kitap in kitap_listesi:
                dosya.write(f"Kitap Adı: {kitap.ad}, Yazar: {kitap.yazar}\n")
        print("Programdan çıkılıyor.")
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
