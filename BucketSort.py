def bucket_sort(dizi):
    if not dizi:
        return dizi

    # Liste içindeki en büyük ve en küçük elemanları bul
    max_deger = max(dizi)
    min_deger = min(dizi)

    # Farkı bul ve bu fark kadar aralık sayısı seç
    kova_aralıgı = (max_deger - min_deger) / len(dizi)

    # Boş kovalar (buckets) oluştur
    kovalar = [[] for _ in range(len(dizi))]

    # Her elemanı uygun kova içine yerleştir
    for i in range(len(dizi)):
        index = min(int((dizi[i] - min_deger) // kova_aralıgı), len(dizi) - 1)
        kovalar[index].append(dizi[i])

    # Her kovadaki elemanları sırala (örneğin, başka bir sıralama algoritması kullanabilirsiniz)
    for kova in kovalar:
        kova.sort()

    # Sıralanmış kovaları birleştir
    sıralı_dizi = []
    for kova in kovalar:
        sıralı_dizi.extend(kova)

    return sıralı_dizi

# Örnek
dizi = [64, 88, 96, 65, 25, 12, 22, 11]
dizi = bucket_sort(dizi)

print("Sıralanmış liste:", dizi)
