'''
Bir dikdörtgenin uzun ve kısa kenar uzunluklarını kullanıcıdan isteyin
Bu dikdörrtgenin kare olup olmadığını yazdırın
    Eğer kare ise alanını
    Eğer kare değilse çevresini ekrana yazdırın
'''

kisa_kenar = eval(input("Kısa Kenarın Uzunluğu : "))
uzun_kenar = eval(input("Uzun Kenarın Uzunluğu : "))

if kisa_kenar == uzun_kenar:
    print("Bu bir karedir")
    print("Karenin Alanı : ", kisa_kenar**2)
else:
    print("Bu bir kare değildir")
    print("Dikdörtgenin Çevresi : ", (kisa_kenar+uzun_kenar) * 2)
