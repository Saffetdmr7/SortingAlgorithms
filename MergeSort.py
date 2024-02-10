def merge_sort(dizi):
    if len(dizi) > 1:
        orta = len(dizi) // 2  # Diziyi ikiye böl

        sol_kısım = dizi[:orta]
        sag_kısım = dizi[orta:]

        merge_sort(sol_kısım)  # Sol yarıyı sırala
        merge_sort(sag_kısım)  # Sağ yarıyı sırala

        i = j = k = 0

        # İki alt diziyi birleştir
        while i < len(sol_kısım) and j < len(sag_kısım):
            if sol_kısım[i] < sag_kısım[j]:
                dizi[k] = sol_kısım[i]
                i += 1
            else:
                dizi[k] = sag_kısım[j]
                j += 1
            k += 1

        # Sol yarıdaki olası elemanları ekleyin
        while i < len(sol_kısım):
            dizi[k] = sol_kısım[i]
            i += 1
            k += 1

        # Sağ yarıdaki olası elemanları ekleyin
        while j < len(sag_kısım):
            dizi[k] = sag_kısım[j]
            j += 1
            k += 1


# Örnek
dizi = [12, 11, 13, 5, 6, 7]
merge_sort(dizi)
print("Sıralanmış dizi:", dizi)
