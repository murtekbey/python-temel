# Inheritance (Kalıtım): Miras alma

# Person => name, lastname, age, eat(), run(), drink()
# Student, Teacher --> Personda olan tüm özelliklerin, Student ve Teacherda olmasını istiyorsak eğer -->
# Student(Person), Teacher(Person) --> Bu şekilde persondaki class özelliklerini miras alabiliriz.
# Persondan aldığımız özelliklere ek olarak Student ya da Teacher classlarına yeni özellikler de ekleyebilirim.
# Personu bir temel sınıf olarak kabul edip Student ve Teacheri, Personun alt sınıfı olarak tanımlayabiliriz.

# Animal => Dog(Animal), Cat(Animal) --> Dog ve Cat classları alt sınıf olarak ayarlanır.
# Bu şekilde Animal classından miras alarak tüm Animal özelliklerini Dog ve Cat'e aktarabiliriz.

class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print('Person Created')
    
    def who_am_i(self):
        print('I am a person.')
    
    def eat(self):
        print('I am eating.')

class Student(Person): 
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname) # Bu şekilde Person'un __init__ classınıda çalıştırmış oluruz. Eğer bunu kullanmazsak Student'in init fonksiyonu, Person'unkini ezer.
        self.studentNumber =  number
        print('Student Created')
    # Override
    def who_am_i(self): # aynı isimde bir method, temel sınıftaki methodu ezer.
        print('I am a student.')

    def sayHello(self): # sadece student üzerinden çağırabiliriz çünkü person classına ait bir metod değil. personun alt sınıfında olan bir method.
        print('Hello, I am a student.')

class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname, lname) # super dedikten sonra .__init__() çağırırsak, self'i göndermemize gerek kalmıyor. sadece parametreler yeterli
        self.branch = branch
    def who_am_i(self):
        print(f'I am a {self.branch} teacher.')


p1 = Person('Ali', 'Yılmaz')
s1 = Student('Çınar', 'Turan', 1256) # Student'da bir Person olduğundan dolayı yukarıdaki 'Person Created' ibaresini, Student classındada görmemiz mümkün olur.
t1 = Teacher('Serkan', 'Yılmaz','Math')

print(p1.firstName + ' ' + p1.lastName)
print(s1.firstName + ' ' + s1.lastName + ' ' + str(s1.studentNumber))

p1.who_am_i()
s1.who_am_i() 
p1.eat()
s1.eat()
s1.sayHello()
t1.who_am_i()