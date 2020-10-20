# list = [1,2,3]
# for item in list: # her zamanki kullandığımız for döngüsü.
#     print(item)

###################################################################################################################################
# range() metodu

for item in range(10): # 0. indexden başlar, 10. indexe kadar yazar. bizim için bir liste oluşturur.
    print(item)

for item in range(10,50): # 10. indexden başlar, 50. indexe kadar yazar. bizim için bir liste oluşturur.
    print(item)

for item in range(0,100,10): # 0. indexden başlar, 100. indexe kadar, 10'ar 10'ar yazar. bizim için bir liste oluşturur.
    print(item)

print(list(range(0,100,10))) # tür dönüşümü yapıp liste içerisine ekledik ve range methoduyla oluşturduğumuz değerleri liste aktardık.

###################################################################################################################################
# enumerate metodu

index = 0
greeting = 'Hello there'

for letter in greeting: # normalde yaptığımız for metodu ile index numarasıyla, index numarasına karşılık gelen harfi karşılıklı yazdık.
    print(f'index: {index},\t letter: {greeting[index]}')
    index += 1

# enumerate metodu ile yazmak istersek.

greeting = 'Hello there'
for index,letter in enumerate(greeting): # enumerate kullanarak harfe karşılık gelen index numarasını bu şekilde yazdırabiliriz.
    print(f'index: {index},\t letter: {letter}') # ayrı ayrı düzenli bir şekilde yazdırmak istersem böyle yazdırabilirim.

greeting = 'Hello there'
for item in enumerate(greeting): # enumerate kullanarak harfe karşılık gelen index numarasını bu şekilde yazdırabiliriz.
    print(item) # Bu şekilde de index numarasına karşılık gelen letter bilgisin yazdırabilirim.

greeting = 'Hello there'
for index,letter in enumerate(greeting): # enumerate kullanarak harfe karşılık gelen index numarasını bu şekilde yazdırabiliriz.
    print(index) # sadece index numarasını yazdırmak istersem bu şekilde for index,letter dedikten sonra yazdırmak istediğim değeri seçip yazdırabilirim.
###################################################################################################################################
# zip methodu

list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']
list3 = [100,200,300,400,500]

print(list(zip(list1, list2, list3))) # zip komutu ile listeleri birbirlerine index numarasına karşılık gelen değerler ile birleştirebiliriz.

for a,b,c in zip(list1, list2, list3): # zip komutu ile birleştirdiğimiz listeleri for döngüsü ile alt alta yazdırabiliriz.
    print(a,b,c)

