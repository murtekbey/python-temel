message = 'Hello There. My name is Murat Altınpınar'.split() 
# Mesajı string bir şekilde yazdık ve .split() komutu ile ögelerine ayırdık.

print(message[0])

# my_list = [1,2,3]
# my_list = ['bir',2, True, 5.6]
# print(my_list)

list1 = ['one','two','there'] # liste 1'i oluşturduk
list2 = ['four','five','six'] # liste 2'yi oluşturduk

numbers = list1 + list2 # numbers değeri üzerinden list1 ile list2 yi birbirine ekledik.
print(numbers) # tüm listeyi yazdırdık.
print(len(numbers)) # listenin kaç tane ögesi olduğunu söyler.
print(message) # split ile ayırdığımız message ' i yazdırdık.
print(message[0]) # split ile ayırdığımız message'daki 0. indexdeki elemanı aldık.
print(numbers[2]) # 2. indexdeki elemanı aldık.

userA = ['Murat', 26]
userB = ['Gurur', 19]

users = [userA, userB]

print(userA)
print(userB)
print(users)

print(users[0][0]) # users değeri içerisinden 0. indexindeki elemanın 0. indexdeki ögesini aldık yani sadece 'Murat' ifadesini aldık.



