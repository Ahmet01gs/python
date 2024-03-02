import random
import time

# Oyun alanı boyutları
ALAN_GENISLIK = 10
ALAN_YUKSEKLIK = 5

# Oyuncu ve düşmanlar
oyuncu = [ALAN_GENISLIK // 2, ALAN_YUKSEKLIK - 1]
dusmanlar = [[x, 0] for x in range(ALAN_GENISLIK)]

# Oyun döngüsü
oyun_sonu = False
skor = 0

while not oyun_sonu:
    # Oyun alanını oluşturma
    oyun_alani = [['.' for _ in range(ALAN_GENISLIK)] for _ in range(ALAN_YUKSEKLIK)]

    # Oyuncu ve düşmanları alan üzerinde gösterme
    oyun_alani[oyuncu[1]][oyuncu[0]] = 'P'
    for dusman in dusmanlar:
        oyun_alani[dusman[1]][dusman[0]] = 'D'

    # Oyun alanını yazdırma
    for satir in oyun_alani:
        print(' '.join(satir))
    print(f"Skor: {skor}")

    # Kullanıcıdan giriş almak
    hamle = input("Sol (S), Sağ (D): ").upper()

    if hamle == 'S':
        oyuncu[0] -= 1
    elif hamle == 'D':
        oyuncu[0] += 1

    # Düşmanları hareket ettirme
    for dusman in dusmanlar:
        dusman[1] += 1

    # Düşmanların rastgele yeniden başlaması
    for dusman in dusmanlar:
        if dusman[1] == ALAN_YUKSEKLIK:
            dusman[1] = 0
            dusman[0] = random.randint(0, ALAN_GENISLIK - 1)
            skor += 1

    # Oyunun sona erip ermediğini kontrol etme
    for dusman in dusmanlar:
        if dusman == oyuncu:
            oyun_sonu = True
            break

    # Oyun hızını kontrol etme
    time.sleep(0.5)

print(f"Oyun Bitti! Toplam Skor: {skor}")
