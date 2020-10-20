# Identity Operator: is
x = y = [1, 2, 3]
z = [1, 2, 3]

print(x==y) # True -> İçeriği karşılaştırdığı için sonuç True
print(x==z) # True -> İçeriği karşılaştırdığı için sonuç True
print(x is y) # True -> Referans numarasını karşılaştırdığı için sonuç True (x = y olduğundan dolayı referans numaraları aynıdır.)
print(x is z) # False -> Referans numarasını karşılaştırdığı için sonuç False (x ile z nin referans numaraları farklıdır.) 

x = [1, 2, 3]
y = [2, 4]

del x[2] # 2. indeksdeki elemanı sildik.
y[1] = 1 # 1. indeksdeki elemanı '1' ile değiştirdik.
y.reverse() # y içerisindeki elemanları ters çevirdik.

print(x==y) # True -> içerisindeki elemanlar aynı olduğundan True yanıtını aldık.
print(x is y) # False -> x ile y farklı objeler olduğu için False yanıtını aldık.
print(x is not y) # True -> soruyu tersten sorduk. x ile y farklı objeler değil midir diye sorduğumuz için True yanıtını aldık.

###################################################################################################################################
# Membership Operator: in
x = ['apple', 'banana']
print('banana' in x)

name = 'Murat'
print('a' in name) # True -> 'a' karakteri name içerisinde var mı
print('a' not in name) # False -> soruyu tersten sorduk. ('a' karakteri name içerisinde yok mu)