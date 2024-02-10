def heapify(dizi, n, i):
    en_buyuk = i  # En büyük elemanı kök olarak kabul et
    sol_cocuk = 2 * i + 1
    sag_cocuk = 2 * i + 2

    # Sol çocuk kökten daha büyükse
    if sol_cocuk < n and dizi[sol_cocuk] > dizi[en_buyuk]:
        en_buyuk = sol_cocuk

    # Sağ çocuk kökten daha büyükse
    if sag_cocuk < n and dizi[sag_cocuk] > dizi[en_buyuk]:
        en_buyuk = sag_cocuk

    # Eğer en büyük eleman kök değilse, değişiklik yap
    if en_buyuk != i:
        dizi[i], dizi[en_buyuk] = dizi[en_buyuk], dizi[i]  # Elemanları değiştir

        # Yapılan değişiklik sonrasında alt ağaçları kontrol et
        heapify(dizi, n, en_buyuk)

def heap_sort(dizi):
    n = len(dizi)

    # Max heap oluştur
    for i in range(n // 2 - 1, -1, -1):
        heapify(dizi, n, i)

    # Heap yapısını kullanarak sırala
    for i in range(n - 1, 0, -1):
        dizi[i], dizi[0] = dizi[0], dizi[i]  # Kök ile son elemanı değiştir
        heapify(dizi, i, 0)

# Örnek
dizi = [64, 69, 88, 47, 48, 25, 12, 22, 11]
heap_sort(dizi)

print("Sıralanmış liste:", dizi)
