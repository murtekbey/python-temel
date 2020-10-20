# value types => string, integer, float (Numbers)
x = 5 
y = 25 
x = y 
y = 10

print(x,y) # x değeri hala 25 olarak kalır.

# reference types => list
a = ["apple", "banana", "lemon"] # a'ya elemanları ekledik.
b = ["apple", "peach", "cherry"] # b'ye elemanları ekledik
a = b # a'daki listeyi b'deki liste ile eşitleyerek değiştirdik. 
b[0] = "grape" # b üzerinden 0. indexdeki elemanın değerini "grape" olarak değiştirdik.

print(a,b) # bu sefer b değerindeki elemanların üzerinde bir değişiklik yapmamız 
# a'nın elemanlarınıda etkiledi ve 'apple' elemanı 'grape' olarak değişti.