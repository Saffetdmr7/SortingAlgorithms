def insertion_sort(dizi):
    for i in range(1, len(dizi)):
        min_sayı = dizi[i]
        j = i - 1
        while j >= 0 and min_sayı < dizi[j]:
            dizi[j + 1] = dizi[j]
            j -= 1
        dizi[j + 1] = min_sayı

# Örnek
dizi = [12, 11, 13, 55, 61,65,78,99,6,4,21,37,1,5,28,3,4,444]
insertion_sort(dizi)
print("Sıralanmış dizi:", dizi)
