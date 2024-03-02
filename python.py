import pandas as pd

# Tarih aralığını oluşturun (örneğin, 30 gün)
start_date = pd.to_datetime("2023-10-01")
end_date = pd.to_datetime("2023-10-30")
date_range = pd.date_range(start=start_date, end=end_date)

# 4 kişiyi temsil eden bir liste oluşturun
personel_listesi = ["Personel 1", "Personel 2", "Personel 3", "Personel 4"]

# Boş bir DataFrame oluşturun
vardiya_programi = pd.DataFrame(columns=["Tarih", "Nöbetçi Kişi", "Durum"])

# Vardiya programını doldurun
nöbetçi_index = 0
for tarih in date_range:
    nöbetçi_kişi = personel_listesi[nöbetçi_index]
    vardiya_programi = vardiya_programi.append({"Tarih": tarih, "Nöbetçi Kişi": nöbetçi_kişi, "Durum": ""}, ignore_index=True)
    nöbetçi_index = (nöbetçi_index + 1) % len(personel_listesi

# İzinli günleri belirleyin (her kişi nöbet sonrası bir gün izinli)
vardiya_programi["Durum"] = vardiya_programi["Nöbetçi Kişi"] != vardiya_programi["Nöbetçi Kişi"].shift(1)
vardiya_programi.loc[0, "Durum"] = "İzinli"

# Excel dosyasına kaydedin
vardiya_programi.to_excel("vardiya_programi.xlsx", index=False)
print("Vardiya programı başarıyla 'vardiya_programi.xlsx' dosyasına kaydedildi.")
