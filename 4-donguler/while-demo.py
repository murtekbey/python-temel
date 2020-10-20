sayilar = [1,3,5,7,9,12,19,21]

#####################################################################################################################################
# # 1. sayilar listesini while ile ekrana yazdirin.
i = 0 
while (i < len(sayilar)): 
    print(sayilar[i])
    i += 1 

#####################################################################################################################################
# 2. Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın.
baslangic = int(input('Başlangıç değeri: ')) 
bitis = int(input('Bitiş değeri: ')) 
i = baslangic 
while i < bitis: 
    i += 1 
    print(i) 
print('Bitti.')

#####################################################################################################################################
# 3. 1-100 arasındaki sayıları azalan şekilde yazdırın.
i = 100 
while i > 0:
    print(i)
    i -= 1 

#####################################################################################################################################
# 4. Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın.
numbers = [] 
i = 0 

while i < 5:
    sayi = int(input('Sayı giriniz: ')) 
    numbers.append(sayi) 
    i +=1 
numbers.sort() 
print(numbers) 

#####################################################################################################################################
# 5. Kullanıcıdan alacağınız sınırsız ürün bilgisini ürünler listesi içerisinde saklayınız.
# ** ürün sayısını kullanıcıya sorun.
# ** dictionary listesi yapısı (name, price) şeklinde olsun.
# ** ürün ekleme işlemi bittiğinde ekranda while ile listeleyin.

urunler = [] 

adet = int(input('Kaç adet ürün eklemek istiyorsunuz: '))
i = 0

while i < adet:
    name = input('Eklemek istediğiniz ürünün isim bilgisini girin: ')
    price = int(input('Eklemek istediğiniz ürünün fiyat bilgisini girin: '))
    urunler.append({ 
        'name': name, 
        'price': price
    })
    i += 1

for urun in urunler:
    print(f'Ürünün Adı: {urun["name"]}\t Ürünün Fiyatı: {urun["price"]}')
print(urunler)