name = 'Murat'
surname = 'Altınpınar'
age = 26

deneme = 'My name is '
greeting = deneme + name + ' ' + surname + '\nI am ' + str(age) + ' years old.' # \n komutu alt satıra kaymamızı sağlar.
length = len(greeting) # 46 karakter olduğunu söyler fakat 45 karakterdir çünkü 0 dan başlar.

print(greeting)  # --> tanımladığımız greeting değişkeni ile yazdırdık.
print(greeting[0]) # [0] kodu, string ifadesinde ki ilk harfe karşılık gelir. ve sadece "M" karakterini yazdırır.
print(greeting[3])
print(len(greeting)) # greeting ifadesinin kaç karakterden oluştuğunu bize söyler.
print(greeting[length-1]) # cümlenin son karakterindeki değeri bize söyler. -1 diyoruz çünkü 0'dan başlıyor.
print(greeting[-1]) # print(greeting[length-1]) komutuyla aynı işlevi görür.
print(greeting[3:7]) # 3 satırından başlar : ifadesinden sonraki yazılan sayı kadar yazdırmaya devam eder. (3 dahil degildir.)
print(greeting[3:]) # 3 satırından başlar, sonsuza kadar devam eder.
print(greeting[:16]) # ilk satırından başlar, 15 satırına kadar devam eder.
print(greeting[2:40:2]) # 2. satırdan başlar, 40'a kadar devam eder, 2 karakterde 1 al.
