'''
4- If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
        The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000.
    1000 in altında 3 ve 5 in katları olan sayıların toplamı kaçtır?
'''
toplam = 0
for sayi in range(3, 1000):
    if sayi % 3 == 0 or sayi % 5 == 0:
        toplam += sayi

print("Toplam :", toplam)

