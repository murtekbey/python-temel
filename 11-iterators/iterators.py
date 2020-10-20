# liste = [1,2,3,4,5]
# # Liste objesi iterable bir obje olduğu için liste elemanlarını for döngüsüyle tek tek dolaşabiliyoruz.
# for i in liste: # for döngüsündeki liste elemanı aslında bir iterable obje. 
#     print(i)

# print(dir(liste)) # __iter__ methoduna sahip obje, bir iterable objedir.

##########################################################################################################################

# iterator = iter(liste) # liste objesini iter bir objeye çevirdik.

# print(next(iterator)) # 1
# print(next(iterator)) # 2
# print(next(iterator)) # 3
# print(next(iterator)) # 4
# print(next(iterator)) # 5 --> Her çağırdığımızda listenin içerisindeki her bir elemanı sıra sıra çağırır.
# # print(next(iterator)) # 6 --> çağıramayız bize 6. elemanın olmadığıyla ilgili bir hata verir.

# for i in liste:
#     print(i)

##########################################################################################################################

# liste = [1,2,3,4,5]
# iterator = iter(liste)

# while True:
#     try:
#         element = next(iterator)
#         print(element)
#     except StopIteration:
#         break

##########################################################################################################################

class MyNumbers:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start+=1
            return x
        else:
            raise StopIteration

list = MyNumbers(20,50)

myIter = iter(list)

while True:
    try:
        element = next(myIter)
        print(element)
    except StopIteration:
        break

# print(next(myIter))
# print(next(myIter))
# print(next(myIter))
# print(next(myIter))
# print(next(myIter))

# for x in list:
#     print(x)