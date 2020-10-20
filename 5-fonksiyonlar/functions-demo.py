####################################################################################################################################
# 1. Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyon yazın.
def yazdir(kelime, adet): # yazdir diye bir fonksiyon oluşturduk ve dışardan kelime ve adet almasını istedik.
    print(kelime *  adet) # içerisine girilen parametrelere göre kelime sayısını adet ile çarpın ve bize kelimeyi o kadar yazdırın.

yazdir('Merhaba\n', 10) # burda kelime ve adet yerine ('Merhaba' , 10) kullandık ve sonucu aldık.

####################################################################################################################################
# 2. Kendine gönderilen sınırsız sayıda parametreyi bir listeye çeviren fonksiyon yazın.
def listeyeCevir(*params): # * kullandık çünkü sınırsız bir liste oluşturmak istiyoruz.
    liste = [] # boş bir liste oluşturduk.
    for param in params: # gönderilen bütün parametreleri dolaşmak için bir for döngüsü oluşturduk.
        liste.append(param) # her bir elemanı aldığımızda liste üzerine append() ile ekledik.
    return liste # işimiz bittikten sonrada return liste diyerek oluşturulan listeyi geri çevirelim.

result = listeyeCevir(10,20,30,40, 'Merhaba', 'Naber', 'Nasılsın') # listeyeCevir fonksiyonunu oluşturduk. şimdide sınırsız parametremizi bu fonksiyonun içerisine ekleyelim.

print(result) # ve listeyi ekranda yazdıralım.

####################################################################################################################################
# 3. Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.
def asalSayilariBul(sayi1, sayi2): 
    for sayi in range(sayi1, sayi2+1): # range komutunu kullanarak sayi1 ile sayi2 arasındaki bütün sayıları işin içine kattık ve for döngüsüyle tek tek dolaşıcaz. sayi2+1 dedik çünkü sayi2'yi de işin içine katmak istiyoruz.
        if sayi > 1: # sayının 1'den büyük olması koşulunu verdik çünkü 1 asal sayı değil. 
            for i in range(2, sayi): # döngüye 2 den başlayıp, o an da elde ettiğimiz sayıya kadar git. 
                if (sayi % i == 0): # Eğer sayı, kullanıcının girdiği sayıya varana kadar herhangi bir sayıya kalansız bir şekilde bölünürse
                    break # döngüyü durdur
            else:
                print(sayi)

sayi1 = int(input('1. Sayıyı giriniz: '))
sayi2 = int(input('2. Sayıyı giriniz: '))

asalSayilariBul(sayi1,sayi2)

####################################################################################################################################
# 4. Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde geriye gönderen bir fonksiyon yazın.

def tamBolenleribul(kullaniciSayi):
    tamBolenler = []
        
    for i in range(2, kullaniciSayi):
        if (kullaniciSayi % i == 0):
            tamBolenler.append(i)
    return tamBolenler


kullaniciSayi = int(input('Sayıyı giriniz: '))
result = tamBolenleribul(kullaniciSayi)

print(result)