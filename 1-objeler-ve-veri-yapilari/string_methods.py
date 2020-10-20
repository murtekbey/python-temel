message = 'Hello There. My name is Murat Altınpınar'

message = message.upper() # Tüm mesajı Büyük Harflerle yazar.
message = message.lower() # Tüm mesajı Küçük Harflerle yazar.
message = message.title() # Başlık gibi her kelimenin ilk harfini büyük yazar. 
message = message.capitalize() # String ifadenin sadece ilk harfini büyük yazar.
message = message.strip() # String ifadenin başındaki boşluk karakterini kaldırır.
message = message.split() # String ifadedeki kelimelerin her 1 tanesi boşluk karakterlerinden itibaren bölünür. Cümleyi parçalarına ayırır. Karakter dizisi olarak gelir.
message = message.split('.') # yine Split işlemi uygular fakat her '.' ifadesinden sonra ayırır.
message = '-'.join(message) # parçalara bölünen string ifadeyi birleştirir.

index = message.find('Murat') # String içerisinde o ifadenin olup olmadığını arar.
print(index) # eğer pozitif bi sayı geliyorsa o cümlenin içinde o ifadenin olduğuna işaret eder. Eğer -1 değeri geliyorsa o kelime string ifadenin içinde geçmiyodur.

isFound = message.startswith('H') # string içerisindeki ifadenin H ile başlayıp başlamadığını denetler. Başlıyorsa 'True' başlamıyorsa 'False'.
isFound = message.endswith('r') # string içerisindeki ifadenin r ile bitip bitmediğini denetler.
message = message.replace('Murat', 'Efe') # string içerisinde arama yapar. 1. parametreye yazdığınız ifadeyi 2. parametredeki ifadeyle değiştirir.
message = message.replace('ç', 'c').replace('ö', 'o').replace(' ', '-') # art arda ekleyerek gidebiliriz.

message = message.center(50,'*') # string için bir placeholder, bir container oluşturur ve yazdığımız şeyi ortalar. Boşluk yerine * veya başka bişey eklenebilir.

print(message[0]) # Split ile böldüğümüz ifadedeki her cümleden parçalanmış kelimeyi kullandığımız sıraya göre getirir. (0'dan başlar.)

print(message)
