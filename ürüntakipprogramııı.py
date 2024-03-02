class Ürün:
    def __init__(self, ad, açıklama, fiyat, miktar):
        self.ad = ad
        self.açıklama = açıklama
        self.fiyat = fiyat
        self.miktar = miktar

    def __str__(self):
        return f"Ad: {self.ad}, Açıklama: {self.açıklama}, Fiyat: {self.fiyat:.2f} TL, Miktar: {self.miktar} adet"

class ÜrünTakip:
    def __init__(self):
        self.ürünler = []

    def ürün_ekle(self, ad, açıklama, fiyat, miktar):
        ürün = Ürün(ad, açıklama, fiyat, miktar)
        self.ürünler.append(ürün)

    def ürünleri_listele(self):
        for i, ürün in enumerate(self.ürünler, start=1):
            print(f"{i}. {ürün}")

    def ürün_güncelle(self, indeks, ad, açıklama, fiyat, miktar):
        if indeks >= 1 and indeks <= len(self.ürünler):
            ürün = self.ürünler[indeks - 1]
            ürün.ad = ad
            ürün.açıklama = açıklama
            ürün.fiyat = fiyat
            ürün.miktar = miktar
            print(f"{indeks}. ürün güncellendi.")
        else:
            print("Geçersiz ürün indeksi.")

    def ürün_sil(self, indeks):
        if indeks >= 1 and indeks <= len(self.ürünler):
            silinen_ürün = self.ürünler.pop(indeks - 1)
            print(f"Silinen ürün: {silinen_ürün}")
        else:
            print("Geçersiz ürün indeksi.")

    def toplam_değeri_hesapla(self):
        toplam_değer = sum(ürün.fiyat * ürün.miktar for ürün in self.ürünler)
        return toplam_değer

    def verileri_dosyaya_kaydet(self, dosya_adı):
        veriler = [str(ürün) for ürün in self.ürünler]
        with open(dosya_adı, 'w') as dosya:
            dosya.write("\n".join(veriler))
            print(f"Ürünler '{dosya_adı}' adlı dosyaya kaydedildi.")

def main():
    takipçi = ÜrünTakip()

    while True:
        print("\nÜrün Takip Menüsü:")
        print("1. Ürün Ekle")
        print("2. Ürünleri Listele")
        print("3. Ürün Güncelle")
        print("4. Ürün Sil")
        print("5. Verileri Dosyaya Kaydet")
        print("6. Toplam Değeri Hesapla")
        print("7. Çıkış")

        seçim = input("Seçiminizi girin: ")

        if seçim == '1':
            ad = input("Ürün adını girin: ")
            açıklama = input("Ürün açıklamasını girin: ")
            fiyat = float(input("Ürün fiyatını girin: "))
            miktar = int(input("Ürün miktarını girin: "))
            takipçi.ürün_ekle(ad, açıklama, fiyat, miktar)
        elif seçim == '2':
            takipçi.ürünleri_listele()
        elif seçim == '3':
            indeks = int(input("Güncellenecek ürünün indeksini girin: "))
            ad = input("Güncellenmiş ürün adını girin: ")
            açıklama = input("Güncellenmiş ürün açıklamasını girin: ")
            fiyat = float(input("Güncellenmiş ürün fiyatını girin: "))
            miktar = int(input("Güncellenmiş ürün miktarını girin: "))
            takipçi.ürün_güncelle(indeks, ad, açıklama, fiyat, miktar)
        elif seçim == '4':
            indeks = int(input("Silinecek ürünün indeksini girin: "))
            takipçi.ürün_sil(indeks)
        elif seçim == '5':
            dosya_adı = input("Verileri kaydetmek için dosya adını girin: ")
            takipçi.verileri_dosyaya_kaydet(dosya_adı)
        elif seçim == '6':
            toplam_değer = takipçi.toplam_değeri_hesapla()
            print(f"Ürünlerin toplam değeri: {toplam_değer:.2f} TL")
        elif seçim == '7':
            break
        else:
            print("Geçersiz seçenek. Lütfen geçerli bir seçenek seçin.")

if __name__ == "__main__":
    main()
