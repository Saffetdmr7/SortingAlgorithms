def selection_sort(dizi):
    n = len(dizi)

    for i in range(n):
        # İlk elemanı minimum olarak seç
        min_sayı = i
        for j in range(i + 1, n):
            if dizi[j] < dizi[min_sayı]:
                min_sayı = j

        # Minimum elemanı bulunan elemanla değiştir
        dizi[i], dizi[min_sayı] = dizi[min_sayı], dizi[i]

# Örnek
dizi = [64, 25, 12, 22, 11]
selection_sort(dizi)
print("Sıralanmış dizi:", dizi)
