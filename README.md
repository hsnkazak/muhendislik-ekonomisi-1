# MÜHENDİSLİK EKONOMİSİ: Prensipler ve Uygulamalar (C4)

Bu depo, [Prof. Dr. Osman Okka, Doç. Dr. Hasan Kazak, Dr. Melahat Karadağ] tarafından yazılan *Mühendislik Ekonomisi: Prensipler ve Uygulamalar (C4)* kitabındaki örneklere ait Python kodlarını içermektedir. Kodlar kitaptaki sonuçların öğrenciler tarafından yeniden üretilebilmesi ve incelenebilmesi amacıyla paylaşılmaktadır.

Kitap: [Nobel Yayınevi, 2026]

## İçerik

| Klasör | Bölüm | Örnek | Dosya |
|---|---|---|---|
| `bolum-11` | 11. Bölüm: Veri Tabanlı Maliyet ve Nakit Akımı Tahmini: Ekonometrik Yöntemler, Öğrenme Eğrileri ve Yapay Zekâ | Örnek 11.18. Veri tabanlı bir yatırım projesinin bütünleşik analizi (Monte Carlo simülasyonu) | `ornek_11_18_monte_carlo.py`, `ornek_11_18_monte_carlo.ipynb` |

## Kodu çalıştırma

### Google Colab ile (kurulum gerektirmez)

Aşağıdaki bağlantıya tıklayarak kodu doğrudan tarayıcıda açabilir ve çalıştırabilirsiniz:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hsnkazak/muhendislik-ekonomisi-1/blob/main/bolum-11/ornek_11_18_monte_carlo.ipynb)

Colab açıldıktan sonra **Çalışma zamanı → Tümünü çalıştır** seçeneğini kullanın.

### Kendi bilgisayarınızda

Python ve NumPy kurulu olmalıdır:

    pip install numpy
    python ornek_11_18_monte_carlo.py

## Test edilen ortam

Kitaptaki sonuçlar aşağıdaki ortamda elde edilmiştir:

- Google Colab
- Python 3.13
- NumPy 2.4.6

Rastgele sayı üretimi tohum değeriyle (`seed = 42`) sabitlendiği için kod aynı ortamda her çalıştırıldığında aynı sonuçları verir. Farklı bir NumPy sürümü veya farklı bir bilgisayar kullanıldığında ikinci ondalık basamakta küçük farklar görülebilir. Bu farklar simülasyonun yorumunu değiştirmez.

## Beklenen çıktı: Örnek 11.18

Kod iki simülasyon çalıştırır. Değerler milyon TL cinsindendir. Python ondalık ayırıcı olarak nokta kullandığından ekrandaki 28.04 değeri kitaptaki 28,04 milyon TL'ye karşılık gelir.

**1. Temel simülasyon** (satış fiyatı ile satış miktarı arasındaki korelasyon −0,40):

    Ortalama NBD: 28.04
    Medyan NBD: 27.47
    %5 yüzdelik: -19.83
    %95 yüzdelik: 77.53
    P(NBD > 0): 82.8 %

**2. Karşılaştırma** (satış fiyatı ile satış miktarı arasındaki korelasyon sıfır):

    Ortalama NBD: 29.2
    Medyan NBD: 28.02
    %5 yüzdelik: -31.5
    %95 yüzdelik: 93.66
    P(NBD > 0): 77.6 %

Bu sonuçlar kitaptaki Tablo 11.30 ve VI.6.5 kısmındaki karşılaştırmayla aynıdır.

## Lisans

Kodlar MIT Lisansı ile paylaşılmaktadır. Ayrıntılar için `LICENSE` dosyasına bakınız.
