import pandas as pd
import json 

#JSON dosyasını okuyoruz bu aşşağıdaki kod ile spoi geçmişini okicaz
with open("StreamHistory.json", encoding="utf-8") as f:
    data = json.load(f)

# veriyi DataFrame e çevirecez
df = pd.DataFrame(data)

print(df.head())
 
 # En çok dinlenen sanatçıyı bul
en_cok_dinlenen = df.groupby("artistName")["msPlayed"].sum().sort_values(ascending=False)
print("\nEn çok dinlenen sanatçılar (milisaniye bazında):")
print(en_cok_dinlenen)
 
 # Tüm müziklerin toplam çalma süresini saat cinsinden bul
toplam_ms = df["msPlayed"].sum()
toplam_saat = toplam_ms / (1000 * 60 * 60)

print(f"\nToplam dinleme süresi: {toplam_saat:.2f} saat")

import matplotlib.pyplot as plt

# En çok dinlenen ilk 5 sanatçıyı göster
ilk5 = en_cok_dinlenen.head(5)

plt.figure(figsize=(6,6))
plt.pie(ilk5, labels=ilk5.index, autopct='%1.1f%%', startangle=140)
plt.title("En Çok Dinlenen Sanatçılar (İlk 5)")
plt.axis('equal')  # Daireyi düzgün göster
plt.show()

# Bar grafik ile en çok dinlenen sanatçılar
ilk5.plot(kind='bar', color='skyblue')
plt.title("En Çok Dinlenen Sanatçılar (Bar Grafiği)")
plt.ylabel("Milisaniye")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Tüm şarkı adlarını birleştir
tum_sarkilar = " ".join(df["trackName"])

# Word Cloud oluştur
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(tum_sarkilar)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Dinlediğin Şarkıların Adlarında En Çok Kullanıan Kelimeler")
plt.show()
