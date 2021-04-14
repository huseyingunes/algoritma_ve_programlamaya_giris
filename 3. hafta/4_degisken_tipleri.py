"""
Python da çeşitli değişken tipleri vardır.
Bunlar;
    int -> tam sayı tipi
    float -> ondalıklı sayı tipi
    str -> metin(string) tipi
    bool -> doğru yanlış (boolean) tipi
    NoneType -> hiçbirşey(None) ifade etmeyen değişken tipi (Boş değer için kullanılır)
    list, tuple, dictionary -> dizi tipleri -> daha sonra anlatılacak
"""
a = 15000
print(a)
print(type(a))
print(a*10)

a = "15000"
print(a)
print(type(a))
print(a*10)

a = 15.15
print(a)
print(type(a))
print(a*10)

a = True  # True ya da False değeri alabilir
print(a)
print(type(a))
a = 10 < 5  # 10 değeri 5 değerinden küçük olmadığı için False (Yanlış) değeri döner
print(a)
print(type(a))

a = None
print(a)
print(type(a))
# print(a*10) # hiçbirşeyi 10 ile çarpamazsınız.

