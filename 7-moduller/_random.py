import random

# result = dir(random)
# result = help(random)

result = random.random() # 0.0 - 1.0 arasında bir random sayı üretir.
result = random.random() * 100 # 0.0 - 1.0 arasında bir random sayı üretir ve üretilen sayılar 100 ile çarpılır.

result = random.uniform(1,10) # 1 ile 10 arasnda bir sayı üretir (ondalıklı sayılar.)
result = int(random.uniform(1,100)) # integere çevirerek sayının ondalık kısmını atabiliyoruz.

result = random.randint(1,100) # 1 ile 100 arasında tam sayı üretir.

greeting = 'Hello There.'
names = ['Murat', 'Gurur', 'Pınar', 'Işıl', 'Hazal', 'Anıl', 'Süleyman', 'Efe']
result = names[random.randint(0,len(names)-1)] # random.choice yerine böyle yazabiliriz fakat hazır bir fonksiyonumuz var.
result = random.choice(names) # Bizim için listenin içerisinden rasgele bir elemanı seçer getirir.
result = random.choice(greeting) # liste olmadığı için her harfi ayrı ayrı random şekilde getirir.

liste = list(range(10)) # [0,1,2,3,4,5,6,7,8,9]
random.shuffle(liste) # listedeki elemanların yerini karıştırır.
result = liste

liste = range(100) # 100 elemanlı bir liste
result = random.sample(liste, 3) # listenin içerisinden rasgele 3 tane elemanı almak.
result = random.sample(names, 2) # names listesinin içerisinden rasgele 2 tane getir.

print(result)