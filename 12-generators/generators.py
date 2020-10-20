# Generators bizim için bellek de yer işgal etmeyen bir iterator üretiyor.

# def cube():
#     for i in range(5):  # 50000 tane eleman bile oluştursan bizim için bellekde bir yer tahsil edilmicek ve bellekden tasarruf etmiş olucaz.
#         yield i ** 3    # yield bir değer üretir bunu bize gönderir ve daha sonra bu değer saklanmaz. Gösterdikten sonra silinir.
#                         # bu değere 2. defa ulaşmak istersek bu değere bir daha ulaşamayız çünkü yield ile üretildi. amaç ekrana yazdırmak.
#                         # buradaki önemli olan şey oluşturduğumuz bir liste yok. dolayısıyla bize üretilecek olan her bir değeri o an alıyoruz ve aldığımız andada ekrana yazdırıyoruz.
#                         # değer o anda üretilecek ve o anda ekrana yazdırılacak.

# for i in cube():
#     print(i)

####################################################################################################################################

generator = (i**3 for i in range(5)) # [] parantez yerine () parantez kullanırsak karşımıza bir generator objesi gelir.

print(generator)

# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))

for i in generator:
    print(i)