'''
Soru: Girilen bir sayının asal olup olmadığını bulun.
** Asal sayı 1 ve kendisi hariç tam böleni olmayan sayılara denir.
** '1' Sayısı asal sayı değildir.
'''

sayi = int(input('Bir sayı giriniz: ')) # Kullanıcıdan herhangi bir sayı girmesini istedik.
asalMi = True # ilk başta girdiğimiz sayıyı asal olarak kabul edicez ve if döngüsüyle asal olmadığı durumda değeri false olarak değiştiricez.

if sayi == 1: # eğer sayı 1 ise bunu ekstra bir durum olarak algıla ve sayıyı asal olarak kabul etme.
    print(f'{sayi} sayısı ne yazık ki asal sayı değildir.')

for i in range(2, sayi): # 2'den başlayarak yazılan sayıya gidene kadar her sayıyı for döngüsüyle döndürecektir.
    if (sayi % i == 0): # Eğer sayı, kullanıcının girdiği sayıya varana kadar herhangi bir sayıya kalansız bir şekilde bölünürse
        asalMi = False # asalMi değerini True'dan False olarak değiştiririz. Çünkü sayı kendisi dışında herhangi bir sayıya kalansız olarak bölünüyorsa Asal değildir.
        break # ve döngüyü durdurur aşağıdaki if koşuluna geçeriz.

if asalMi: # eğer asalMi değeri True olarak gelirse, koşulu sağlar ve sayı asal diyebiliriz.
    print(f'{sayi} sayısı asal bir sayıdır.')
else: # eğer asalMi değeri True olarak gelmezse, koşulu sağlamaz ve sayı asal değildir deriz.
    print(f'{sayi} sayısı asal bir sayı değildir.')