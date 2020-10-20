# # global scope
x = 'global x'

def function():
    # local scope # eğer x için herhangi bir tanımlama yapmazsak bir üstteki x tanımını fonksiyon kullanır.
    x = 'local x' # fonksiyon kapsamında tanımlandığından dolayı fonksiyon içerisinde x'i değiştirip local x yapar.
    print(x)

function()
print(x) # fakat fonksiyon dışında çalıştırmak istersek x'in değeri fonksiyonun içerisindekiyle değişmez ve x = 'global x' olarak kalmaya devam eder.

##########################################################################################################################################################
# global
name = 'Murat'

def changeName(new_name):
    global name
    name = new_name
    print(name) # local

changeName('Gurur') # local
print(name) # global

##########################################################################################################################################################
name = 'global string'

def greeting():
    name = 'Murat'
    def hello():
        name = 'Gurur' # burada bir fonksiyon çağırırsam Murat yerine bu sefer Gurur yazar. hiyerarşik düzen de olmalı.
        print('Hello, '+ name) # hiyerarşik düzen oluşturduk. 
# en yukarıda ki name bilgisini almaktansa bi üstteki fonksiyonun içerisinden def bilgisini alır 
# fonksiyonun içerisinde bir fonksiyon olduğu için.

    hello() # fonksiyon içerisinde çağırılmış bir fonksiyon.

greeting() # en dışarıdan çağırılan fonksiyon.

##########################################################################################################################################################

x = 50
def test():
    global x # bu komutu kullanırsak eğer dışarıda global olan x bilgisi üzerinde doğrudan işlem yapar
    print(f'x {x}') # x değişkeni 50

    x = 100
    print(f'changed x to {x}') # x değişkeni fonksiyon içerisinde 100 değeri ile değiştirildi.

test()
print(x) 
# fonksiyon içerisinde global x kullandığımız için x değişkeni dışardada fonksiyon içerisinde tanımlanan değer ile değişti. 
# global x'i kaldırırsak fonksiyon dışında yapılan işlemler, fonksiyon içinde yapılan işlemleri kapsamaz.