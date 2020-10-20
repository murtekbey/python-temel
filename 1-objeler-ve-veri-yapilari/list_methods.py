# List Methods.

numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ['a', 'g', 's', 'b', 'y', 'a', 's']

val = min(numbers)
val = max(numbers)
val = min(letters)
val = max(letters)

val = numbers[:3]
val = numbers[4:]

numbers[4] = 40

numbers.append(49) # ekleme islemi .append
numbers.append(59)
numbers.insert(3, 78) # istediğimiz index numarasından önceye(3) istediğimiz rakamı(78) ekler.
numbers.insert(-1, 52) # sondan başlayarak istediğimiz index numarasından öncesine ekler.
numbers.pop() # son rakamı siler.
numbers.pop(0) # ilk rakamı siler.
numbers.pop(-1) # son rakamı siler() ile aynı çalışır
numbers.remove(49) # istediğiniz karakteri () içine yazdığınızda siler.

numbers.sort() # sayısal büyüklüğüne göre sıralanır.
letters.sort() # alfabbetik sıraya göre sıralanır.

numbers.reverse() # listeyi tersten yazar.
letters.reverse()

print(len(numbers)) # eleman sayısını verir.
print(len(letters))

print(numbers.count(10)) # 10 değerinden kaç tane olduğunu söyler.
print(letters.count('a')) # 'a' değerinden kaç tane olduğunu söyler.

numbers.clear() # bütün elemanları siler.
print(numbers)