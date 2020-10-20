# def usalma(number): # bir fonksiyon tanımladık.

#     def inner(power): # altta bir fonksiyon daha tanımladık.
#         return number ** power

#     return inner # usalma fonksiyonu inner fonksiyonunu çağırıcak.
    
# two = usalma(2) # burada usalma fonksiyonu içerisine bir number atıyoruz ve direk us alma fonksiyonundan etkileniyor.
# print(two(3))   # burada (3) sayısı direk power ile bağlantılı oluyor çünkü biz zaten two fonksiyonunu çağırdığımızda 2 sayısını çağırıyoruz.
#                 # yani burada yaptığımız işlem usalma fonksiyonundaki number değerini power fonksiyonu ile üssü çarpımı yapıyoruz.

# three = usalma(3)
# print(three(4))


# def yetki_sorgula(page):
#     def inner(role):
#         if role == 'Admin':
#             return "{0} rolü {1} sayfasına ulaşabilir.".format(role,page)
#         else:
#             return "{0} rolü {1} sayfasına ulaşamaz.".format(role,page)
#     return inner

# user1 = yetki_sorgula('Product Edit')
# print(user1('Admin'))
# print(user1('User'))


def islem(islem_adi):
    def toplam(*args):
        toplam = 0
        for i in args:
            toplam+=i
        return toplam

    def carpma(*args):
        carpim = 1
        for i in args:
            carpim*=i
        return carpim
    
    if islem_adi == "toplama":
        return toplam
    else:
        return carpma

toplama = islem('toplama')
print(toplama(1,3,5,7,9))

carpma = islem('carpma')
print(carpma(1,3,5,7,5))