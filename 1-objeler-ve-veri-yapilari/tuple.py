# list = [1, 2, 3]

# tuple = (1, 'iki', 3)

# print(type(list))
# print(type(tuple))

# print(list[2])
# print(tuple[2])

# print(len(list))
# print(len(tuple))

list = ['ali', 'veli']
tuple = ('damla', 'ayşe', 'ayşe')
names = ('demet', 'emel', 'ayşe') + tuple # list ile tuple birleştiremezsin.

print(tuple.count('ayşe')) # kaç tane olduğunu söyler.
print(tuple.index('ayşe')) # hangi index numarasında olduğunu söyler.

list[0] = 'ahmet' # burda değişiklik yapılabilir.
# tuple[0] = 'ayse' # tuple ile liste oluşturursan, listenin elemanlarında değişiklik yapamazsın.
print(list)
print(tuple)

print(names)