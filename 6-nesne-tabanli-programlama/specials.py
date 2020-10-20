myList = [1,2,3]
# myString = 'my string'

# print(len(myList)) # len metodu her bir obje için farklı çalışır.
# print(len(myString))
# print(type(myList))
# print(type(myString))

class Movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print('Movie objesi oluşturuldu.') 

    def __str__(self):
        return f"{self.title} by {self.director}"

    def __len__(self):
        return self.duration
    
    def __del__(self): # del fonksiyonu objeyi silmesen bile obje bir süre kullanılmadığı zaman otomatik olarak siliniyor ve silindiği zaman bize aşağıdaki mesajı veriyor.
        print('Film silindi.')

m = Movie('Film Adı', 'Yönetmen Adı', 120)

# print(str(myList))
# print(str(m)) # def __str__, fonksiyonunu classa tanımlamazsak, movienin ram üzerinde hangi konumda oluşturulduğunu söyleyen bir mesaj gelir.
#               # Tanımladıktan sonra bize string bir ifade yazdırır.
# print(len(myList)) # bize listedeki eleman sayısını veriyor her zaman olduğu gibi çünkü list classından çağırdık.
# print(len(m)) # len fonksiyonunu filmin süresi olarak tanımladığımız için artık bize len metodu bize Movie classından filmin süresini göstericektir.

del m # eğer del metodunu kullanırsam m objesi silinir ve printle yazdıramazsın.

print(m)
