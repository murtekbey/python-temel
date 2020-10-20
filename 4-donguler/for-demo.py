sayilar = [1,3,5,7,9,12,19,21]
###################################################################################################################################
# 1. Sayılar listesindeki hangi sayılar 3'ün katıdır ?
for sayi in sayilar: # liste içerisindeki elemanları tek tek dolaşır.
    if sayi%3==0:
        print(sayi)
###################################################################################################################################
# 2. Sayılar listesinde sayıların toplamı kaçtır ?
toplam = 0 # 
for sayi in sayilar: # liste içerisindeki elemanları tek tek dolaşır.
    toplam += sayi # toplam = 0 'ı burda toplamın içerisine atıyoruz. bir sonraki dönüşünde toplamın aldığı yeni değerle birlikte bir sonraki sayıyı toplucak.
# 0+1=1, 1+3=4, 4+5=9, 9+7=16, 16+9=25, 25+12=37, 37+19=56, 56+21=77 <--- Sonucuna ulaşır.
print('Toplam: ',toplam)
###################################################################################################################################
# 3. Sayılar listesindeki tek sayıların karesini alınız.
# for sayi in sayilar: # liste içerisindeki elemanları tek tek dolaşır.
#     if (sayi%2==1):
#         print(sayi**2)
###################################################################################################################################
# # 4. Şehirlerden hangileri en fazla 5 karakterlidir ?
sehirler = ['Kocaeli','İstanbul','Ankara','İzmir','Rize']

for sehir in sehirler: # liste içerisindeki elemanları tek tek dolaşır.
    if (len(sehir) <= 5):
        print(sehir)
###################################################################################################################################
# 5. Ürünlerin fiyatları toplamı nedir?
urunler = [
    {'name':'samsung S6', 'price':'3000'},
    {'name':'samsung S7', 'price':'4000'},
    {'name':'samsung S8', 'price':'5000'},
    {'name':'samsung S9', 'price':'6000'},
    {'name':'samsung S10', 'price':'7000'}
]
toplam = 0
for urun in urunler: # liste içerisindeki elemanları tek tek dolaşır.
    fiyat = int(urun['price']) # price keyine karşılık gelen value bilgisini int'e çevirdik ki toplama işlemini yapabilelim.
    toplam += fiyat
print('Ürünlerin Toplam Fiyatı: ',toplam) # print komutunu en dışarıya almazsak her for döngüsü ile dolaştığında toplama işlemini tek tek yazdırır.
###################################################################################################################################
# 6. Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz ?
for urun in urunler: # liste içerisindeki elemanları tek tek dolaşır.
    if int(urun['price']) <= 5000:
        print(urun['name']) # print komutu içerde olmalı ki if koşulunu bize sağlasın.
