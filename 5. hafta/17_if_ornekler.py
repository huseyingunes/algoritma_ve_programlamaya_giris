'''
Kullanıcıdan önce yaşını girmesini isteyiniz
Yaşı 18 den büyükse:
    Tercih etmek istediği işi
Yaşı 18 den küçükse:
    Tercih etmek istediği üniversiteyi
girmesini isteyiniz.
Tercihini ekrana düzenli bir şekilde yazdırınız
'''

yas = eval(input("Yaşınızı Giriniz : "))

if yas >18:
    isiniz = input("Tercih etmek istediğiniz iş : ")
    print("Siz", isiniz, " mesleğini tercih etmek istiyorsunuz")
else:
    universite = input("Tercih etmek istediğiniz üniversite : ")
    print("Siz", universite, " üniversitesini tercih etmek istiyorsunuz")