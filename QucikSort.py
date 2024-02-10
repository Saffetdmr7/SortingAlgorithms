def quick_sort(dizi):
    if len(dizi) <= 1:
        return dizi
    else:
        pivot = dizi[0]
        pivottan_kucuk = [x for x in dizi[1:] if x <= pivot]
        pivottan_buyuk = [x for x in dizi[1:] if x > pivot]
        return quick_sort(pivottan_kucuk) + [pivot] + quick_sort(pivottan_buyuk)

# Örnek
liste = [64, 88, 69, 25, 12, 22, 11]
sıralı_liste = quick_sort(liste)

print("Sıralanmış liste:", sıralı_liste)
