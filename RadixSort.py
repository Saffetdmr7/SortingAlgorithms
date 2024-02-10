def counting_sort(dizi, exp):
    dizi_boyutu = len(dizi)
    cıkıs = [0] * dizi_boyutu
    sayac = [0] * 10

    for i in range(dizi_boyutu):
        index = dizi[i] // exp
        sayac[index % 10] += 1

    for i in range(1, 10):
        sayac[i] += sayac[i - 1]

    i = dizi_boyutu - 1
    while i >= 0:
        index = dizi[i] // exp
        cıkıs[sayac[index % 10] - 1] = dizi[i]
        sayac[index % 10] -= 1
        i -= 1

    for i in range(dizi_boyutu):
        dizi[i] = cıkıs[i]

def radix_sort(dizi):
    enBuyukEleman = max(dizi)
    exp = 1

    while enBuyukEleman // exp > 0:
        counting_sort(dizi, exp)
        exp *= 10

# Örnek
dizi = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(dizi)

print("Sıralanmış liste:", dizi)
