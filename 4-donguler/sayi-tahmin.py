'''
    1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalışın. (hak = 5)
    ** "random modülü" için "python random" şeklinde arama yapın.
    ** 100 üzerinden puanlama yapın. Her soru 20 puan.
    ** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın.
'''
import random  # python'un random modülünü ekledik.
randomSayi = random.randint(1,100)  # random modülünü random.randint() modülü ile kullandık ve 1 ila 100 arasında bir random sayi vermesini istedik.
can = int(input('Kaç hak kullanmak istersiniz: ')) # Kullanıcıya kaç hakkı olmasını istiyorsa int değerinde yazmasını istedik.
hak = can # hak = can dedik bu sayede kullanıcının hakkını kendi belirleyebilmesini sağladık.
sayac = 0 # kullanıcı için sayaç koyduk ve bu değerle kaç seferde bildiğini ve puanını hesaplamak için kullanabiliriz.

while hak > 0: # while döngüsü kullanarak kullanıcının yazdığı hak kadar tahmin yapabilmesini sağlıcaz.
    hak -= 1 # her döngü döndüğünde hak değerinden 1 çıkmasını istiyoruz.
    sayac += 1 # her döngü döndüğünde sayacın 1 artmasını istiyoruz.
    kullaniciSayi = int(input('Bir sayı giriniz: ')) # kullanıcının talep ettiği hak kadar bir sayı girme şansı verdik.
    if kullaniciSayi == randomSayi: # random sayi ile kullanicinin girdiği sayi aynı gelme koşulunda
        print(f'Tebrikler {sayac}. seferde bildiniz. Toplam puanınız: {100 - (100/can) * (sayac-1)}') # oyunu kazanıyor.
        break # koşulu sağladığı için oyunu kazanıyor ve döngü duruyor.
    elif kullaniciSayi < randomSayi: # kullanıcın girdiği sayı, random gelen sayıdan küçükse..
        print('Yukarı!') # Yukarı ifadesi yazdırılıyor.
    else: # Aksi takdirde
        print('Aşağı') # Aşağı ifadesi yazdırılıyor.

    if hak == 0: # Eğer yukarıdaki koşullar kullanıcının girdiği hak sayısı kadar tahmin de bulunup, random atanan sayıyı bulamadıysa ve hakkı 0 kaldıysa
        print(f'Hakkınız Kalmadı. Tutulan Sayı: {randomSayi}') # bu ifade yazdırılıyor.