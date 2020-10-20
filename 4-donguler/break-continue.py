name = 'Murat Altınpınar'

for letter in name:
    if letter == 'a':
        break # break komutu ile for döngüsünde her bir harfi döndürürken 'a' ya geldiği zaman durmasını sağlarız.
    print(letter)

for letter in name:
    if letter == 't':
        continue # continue komutu ile for döngüsünde her bir harfi döndürürken 't' ye geldiği zaman 't' yi es geçer ve döndürmeye devam eder.
    print(letter)

x = 0

while x < 5:
    if x == 2:
        break # 2 ye geldiğinde while döngüsünden çıkmamızı sağlar.
    print(x)
    x += 1
'''
while x < 5:
    x += 1 # Burada x += 1 komutunu döngüye başladığımızda if ve continue'dan önce almamız gerekiyo çünkü continue'dan sonra yazılan kod blogları işletilmiyor.
    if x == 2:
        continue # 2 ye geldiğinde while döngüsünden çıkmamızı sağlar.
    print(x)
'''
###################################################################################################################################
# 1-100'e kadar tek sayıların toplamı.
x = 0
result = 0
while x <= 100: # koşula x <= 100 olana kadar devam et.
    x += 1 # x değerini her seferinde 1 arttırdık.
    if x % 2 == 0: # eğer x'in 2 ye bölümünden kalan 0 ise
        continue # o sayıyı atla.
    result += x # x'den gelen her değeri result içerisine attık.


print(f'toplam: {result}')