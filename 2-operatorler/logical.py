x = 6
hak = 5
devam = 'e'

result = 5 < x < 10 # x değeri 5 ile 10 arasında olduğunu bu şekilde ifade edebiliriz.

# and
result = (x > 5) and (x < 10) # True, True => True --> Her iki ifadenin True olduğu durumda bize True değerini verir.
result = (hak > 0) and (devam == 'e')

# or
result = (x > 0) or (x % 2 == 0) # True, False => True --> Eşitliğin her iki tarafından sadece 1 tarafının True olması yeterli.

# not
result = not(x > 0) # not() komutu ile normalde vermesi gereken cevabın tam tersini verir.

# x, 5-10 arasında olan çift bir sayı mı?
result = ((x>5) or (x<10)) and (x%2==0) # iç parantez içindeki durumda(iç koşul) 2 durumdan birinin true olması yeterlidir. dış parantezde kalan yer de doğruysa cevap True gelir.

print(result)