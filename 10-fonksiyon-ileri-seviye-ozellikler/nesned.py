# def greeting(name):
#     print('Hello ', name)

# print(greeting('Ali'))
# print(greeting)

# sayHello = greeting # Fonksiyon adreslerinin aynı olmasını sağlar.

# print(sayHello) # burda sayHello'yu çağırmakla greeting'i çağırmak arasında bir fark yok. Aynı adresden bilgiyi alır.
# print(greeting)

# del sayHello # sayHello'yu silmiş olmam adresi silmiş olduğum anlamına gelmez. greeting komutu hala aynı adresden çalışır durumda olur.
# print(sayHello) # sayHello'yu sildiğim için çağıramam fakat greeting'i çağırabilirim.


# encapsulation --> Kapsülleme işlemi. İçerideki fonksiyon kendisine yeni bir (scope)çalışma alanı tanımlıyor ve dışda dönen işler içdeki fonksiyonu ilgilendirmez.
# def outer(num1):
#     print('outer')
#     def inner_increment(num1): # outerdan aldığı num1 parametresini fonksiyon içinde oluşturduğumuz fonksiyonun içerisine gönderelim. inner_increment'a sadece outer fonksiyonuyla ulaşabiliriz.
#         print('inner') # içeride inner fonksiyonunu dışardan outer ile çağırsak bile print işlemini görmeyiz çünkü çalışmaz.
#         return num1 + 1
#     num2= inner_increment(num1) # inner_increment fonksiyonunu outer fonksiyonundan çağırmamız gerekiyo. yani içerideki fonksiyonu bir dışarıdaki fonksiyondan çağırmak gerekiyor.
#     print(num1, num2) # bir içerideki fonksiyonu bu şekilde çağırabiliriz.

# outer(10)
# inner_increment(10) # tanımlayan bir değer hatası alırız. çünkü iç fonksiyonu dışardan outer olmadan çağıramayız.


def factorial(number):
    if not isinstance(number, int): # isinstance fonksiyonu gönderdiğimiz ilgili classın bir objesi olup olmadığını söyler.
        raise TypeError('Number must be an  integer')

    if not number >= 0:
        raise ValueError('Number must be zero or positive')

    def inner_factorial(number): # kendi scope içerisinde işlemleri hallediyor. dışardan müdahale etmiyoruz.
        if number <= 1:
            return 1
        
        return number * inner_factorial(number - 1)
    
    return inner_factorial(number)
try:
    print(factorial(5))
except Exception as ex:
    print(ex)
