# class

class Person:
    # class attributes
    adress = 'NULL' # classımıza adress bilgisini de ekledik. eğer objeye özel olarak bir adress bilgisi verilmediyse yerine 'NULL' yazıcak.

    # constructor (yapıcı metod)
    def __init__(self, name, year): # buradaki 'self' classdan türetilen herhangi bir objeyi temsil etmesi için kullanılır.
    # __init__ metodunun özelliği oluşturulan her bir obje için çalıştırılmasını sağlar.
        # object attributes
        self.name = name
        self.year = year
        print('init metodu çalıştı.')

        # methods

# object (instance)
p1 = Person(name='Murat',year=1994) # p1 = Person('Murat', 1994)
p2 = Person(name='Gurur',year=2001) # p2 = Person('Gurur', 2001)

# updating
p1.name = 'Ahmet'
p1.adress = 'Antalya'

# accessing object attributes
print(f'p1 name: {p1.name}, year: {p1.year} adress: {p1.adress}')
print(f'p2 name: {p2.name}, year: {p2.year} adress: {p2.adress}')

print(p1)
print(p2)
print(type(p1))
print(type(p2))
print(p1 == p2)