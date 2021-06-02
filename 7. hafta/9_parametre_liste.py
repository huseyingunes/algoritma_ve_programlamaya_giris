def topla(*sayilar):
    toplam = 0
    for sayi in sayilar:
        toplam += sayi
    return toplam


print("Sayıların Toplamı :", topla(1, 3, 5, 7, 10, 15, 20, 65, 15))
