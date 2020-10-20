# Decarator fonksiyonları bir fonksiyona bir özellik eklemek istediğimiz zaman kullanırız.
# Bir özelliği bir kaç yerde kullanmak istiyorsak, bir decorator fonksiyonu oluşturup, oluşturmuş olduğumuz decorator fonksiyonunu bir çok fonksiyon ile ilişkilendirebiliriz.
# Buradaki amaç daha az kod yazmak ve yazdığımız kodları daha düzenli bir şekilde yazmak.

# def my_decorator(func): # yarattığımız fonksiyon, dışarıdan bir fonksiyon parametresi alıcak.
#     def wrapper(name): # bu yarattığımız decorator fonksiyonu içerde bir wrapper fonksiyonu tanımlıcak ve belirli işlemler yapıcak.
#         print('Fonksiyondan önce olan işlemler') # dışardan çağırıcağımız fonksiyondan önce yapılacak işlemler.
#         func(name) # Dışardan gönderdiğimiz fonksiyon parametresini çağırıcak.
#         print('Fonksiyondan sonra olan işlemler') # dışardan çağıracağımız fonksiyondan sonra yapılacak işlemler.
#     return wrapper

# def sayHello(): # sayHello fonksiyonunu çağırdığımızda my_decorator fonksiyonu içerisinde çağırılan fonksiyonların tetiklenmesini istiyoruz.
#     print('Hello')

# sayHello = my_decorator(sayHello) # sayHello diye bir parametre tanımladık ve bu parametreden my_decorator fonksiyonunu çağırıp dışardan sayHello fonksiyonunu aldık.
# sayHello() # my_decorator fonksiyonunu sayHello fonksiyonu ile birlikte çağırdık ve işleme soktuk.

# @my_decorator # bu şekilde de yapabilirsin. @my_decoratoru çağırdığımız zaman def_sayHello()'yu my_decorator içerisine gönderir.
# def sayHello(name): # my_decorator fonksiyonuna sayHello fonksiyonunu göndermiş oluyoruz.
#     print('Hello', name)

# sayHello('Murat')

#######################################################################################################################################
import math
import time

def calculate_time(func):
    def wrapper(*args,**kwargs):
        start = time.time() # şimdiki saniye bilgisi verir.
        time.sleep(5) # işlem başladıktan time.sleep(1) diyerek fonksiyonu 1 saniye uyutabiliriz.

        func(*args,**kwargs)

        finish = time.time() # işlemin bittiği süreyi söylüyecektir.
        print('Fonksiyon '+func.__name__+ ' ' + str(finish-start) + " saniye sürdü.")
    return wrapper

@calculate_time
def usalma(a,b):
    print(math.pow(a,b)) # üssü hesaplama modülü

@calculate_time
def faktoriyel(num):
    print(math.factorial(num)) # faktöriyel hesaplama modülü.

@calculate_time
def toplama(*args):
    toplam = 0
    for i in args:
        toplam+=i
    print(toplam)



usalma(2,3)
faktoriyel(4)
toplama(30,50,60,40)
