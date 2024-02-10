def bubble_sort(dizi):
    n = len(dizi)

    # Tüm elemanları kontrol etmek için döngü
    for i in range(n):
        # Her geçişte son i eleman sıralı hale gelir, bu yüzden sadece ilk n-i elemanı kontrol etmeliyiz
        for j in range(0, n-i-1):
            # Elemanları karşılaştır ve yer değiştirme işlemi
            if dizi[j] > dizi[j+1]:
                dizi[j], dizi[j+1] = dizi[j+1], dizi[j]

# Örnek
dizi = [64, 45, 44, 25, 12, 22, 11]
bubble_sort(dizi)

print("Sıralanmış liste:", dizi)
