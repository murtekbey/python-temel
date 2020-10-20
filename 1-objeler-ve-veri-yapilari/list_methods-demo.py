names = ['Ali', 'Yağmur', 'Hakan', 'Deniz']
years = [1998, 2000, 1998, 1987]

# 1-  "Cenk" ismini listenin sonuna ekleyiniz.
names.append('Cenk')

# 2-  "Sena" değerini listenin başına ekleyiniz.
names.insert(0, 'Sena') # listenin başına ekler.
names.insert(-1, 'Mehmet') # listenin sonundaki karakterin bir öncesine ekler.
names.insert(len(names), 'Mehmet') # listenin sonuna ekler.

# 3-  "Deniz" ismini listeden siliniz.
names.remove('Deniz')
names.pop() # listenin en sonundakini siler. () arasına bir index numarası verirseniz o index numarasındaki elemanı siler.

# 4-  "Deniz" isminin indeksi nedir ?
print(names.index('Deniz')) # ya da aşağıda ki yolu tercih edebilirsin.
index = names.index('Deniz')
print(index)

# 5-  "Ali" listenin bir elemanı mıdır ?
result = 'Ali' in names # True ya da False değerini alırsın.
print(result) 

# 6-  Liste elemanlarını ters çevirin.
names.reverse()

# 7-  Liste elemanlarını alfabetik olarak sıralayınız.
names.sort()

# 8-  years listesini rakamsal büyüklüğe göre sıralayınız.
years.sort()

# 9-  str = "Chevrolet,Dacia" karakter dizisini listeye çeviriniz.
str = "Chevrolet,Dacia"
result = str.split(',')
print(result)

# 10- years dizisinin en büyük ve en küçük elemanı nedir ?
min = min(years)
max = max(years)
print(min, max)
# YA DA
val = [max(years), min(years)]
print(val)

# 11- years dizisinde kaç tane 1998 değeri vardır ?
result = years.count(1998)
print(result)
# YA DA
print(years.count(1998))

# 12- years dizisinin tüm elemanlarını siliniz.
years.clear()
print(years)

# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.
markalar = []

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

print(markalar)
