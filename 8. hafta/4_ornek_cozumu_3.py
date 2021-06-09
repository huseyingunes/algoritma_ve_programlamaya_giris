'''
3- Kendisine parametre olarak bir dikdörtgenin uzun ve kısa kenarın uzunlukları verildiğinde
    aynı anda hem alan hem de çevre değerini hesaplayarak geri döndüren fonksiyonu yazınız.
'''

def dikdortgen_hesap(kisa, uzun):
    alan = kisa * uzun
    cevre = (kisa + uzun) * 2
    return alan, cevre

print("Kısa kenar uzunluğu :2")
print("Uzun kenar uzunluğu :8")
print("Alan ve Çevresi:", dikdortgen_hesap(2, 8))
alan, cevre = dikdortgen_hesap(2, 8)
print("Alan ve Çevresi:", alan, " - ", cevre)


