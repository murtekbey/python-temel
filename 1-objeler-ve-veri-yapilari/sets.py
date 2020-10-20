fruits = {'orange', 'apple', 'banana'} # {} parantezleri kullandığımız için indexleme yapmadı. 

# print(fruits[0]) indexlenemez.

for x in fruits: # indexlenemez fakat döngü işlemiyle içindeki elemanlar listelenebilir.
    print(x)

fruits.add('cherry')
fruits.update(['mango', 'grape', 'apple']) # 'apple' elemani listenin içine eklenmedi. çünkü daha önce vardı. aynı elemanı ekleyemeyiz.

fruits.remove('mango') # 'mango' elemanı siler.
fruits.discard('apple') # 'apple' elemanı liste üzerinden siler.

fruits.pop() # liste indexlenmediği için hangi elemanın silindiğini bilemeyiz. son sıradaki elemanı silmez. rasgele siler.
fruits.clear() # tüm elemanlar silinir.

print(fruits)

# myList = [1,2,5,4,4,2,1]
# print(myList) # tekrarlanan elemanlar liste içerisinde gözükür.
# print(set(myList)) # tekrarlanan elemanlat 'set()' komutunu kullandığımız takdirde silinir.