# YÖNTEM 1

# import math # math.py dosyamızın içerisine hazır python kütüphanesinden math modülünü dahil ettik.
# import math as islem # islem takma ismini vererek math modülüne islem takma adıyla ulaşabiliriz.

# value = dir(math) # bütün math modülünde kullanabileceğimiz seçenekleri bize gösterir.
# value = help(math) # bütün math modülünün içerisindeki fonksiyonların ne işe yaradığını söyler.
# value = help(math.factorial) # spesifik olarak bi modül yazıp hakkında bilgi alabiliriz.
# value = math.sqrt(49) # parantez içerisindeki sayının karekökünü alır.
# value = math.factorial(5) # sayının faktöriyelini söyler.
# value = math.floor(5.9) # sayıyı aşağıya doğru yuvarlar. --> 5
# value = math.ceil(5.9) # sayıyı yukarı doğru yuvarlar. --> 6

# value = islem.factorial(5) # math modülüne islem takma adıyla ulaşabiliriz.

#####################################################################################################################
# YÖNTEM 2
# from math import * # mathden her şeyi import eder * kullandığımız için.


from math import factorial, sqrt

# def sqrt(x): # eğer fonksiyon tanımlayıp bunu import'un altında kullanırsak, en son tanımlanan sqrt değeri işlem görür.
#     print('x : '+ str(x))

value = factorial(5)
value = sqrt(9)
# value = ceil(5.8) # ceil metodunu import etmezsen bu komut çalışmaz.


print(value)