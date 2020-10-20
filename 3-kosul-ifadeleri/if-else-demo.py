###################################################################################################################################
# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme 
#    durumunu kontrol ediniz. Ehliyet alma koşulu en az 18 ve eğitim durumu 
#    lise ya da üniversite olmalıdır. 
name = input('Adınız: ')
age = int(input('Yaşınız: '))
education = input('Eğitim Düzeyi: ')

if (age >= 18):
    if (education.lower()=='lise') or (education.lower()=='üniversite'):
        print(f'Sayın {name}, ehliyet alabilirsiniz.')
    else:
        print(f'Sayın {name}, eğitim durumunuz yetersiz olduğundan dolayı ehliyet alamazsınız.')
else:
    print(f'Sayın {name}, 18 yaşından küçük olduğunuzdan dolayı ehliyet alamazsınız.')
###################################################################################################################################
# 2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre
#    not aralığına karşılık gelen not bilgisini yazdırınız.

yazili1 = float(input('1.Yazılı: '))
yazili2 = float(input('2. Yazılı: '))
sozlu = float(input('Sozlu: '))
ortalama = (yazili1+yazili2+sozlu)/3

if (ortalama>=0) and (ortalama<=24):
    print('Not Bilgisi: 0')
elif (ortalama>=25) and (ortalama<=44):
    print('Not Bilgisi: 1')
elif (ortalama>=45) and (ortalama<=54):
    print('Not Bilgisi: 2')
elif (ortalama>=55) and (ortalama<=69):
    print('Not Bilgisi: 3')
elif (ortalama>=70) and (ortalama<=84):
    print('Not Bilgisi: 4')
elif (ortalama>=85) and (ortalama<=100):
    print('Not Bilgisi: 5')
else:
    print('Yanlış bilgi girdiniz. Lütfen tekrar deneyin.')
###################################################################################################################################
# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere
#    göre hesaplayınız.
#    1. Bakım => 1. yıl     
#    2. Bakım => 2. yıl      
#    3. Bakım => 3. yıl     
#    ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız..
#    *** datetime modülünü kullanmanız gerekiyor.  
#    (simdi) - (2018/8/1) => gün

import datetime

tarih = (input('Aracınız hangi tarihte trafiğe çıktı (2000/1/30): '))
tarih = tarih.split('/')
trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi = datetime.datetime.now()
fark = simdi - trafigeCikis
days = int(fark.days)

if days<=365:
    print(f'{days} gün, 1. servis aralığı')
elif days>365 and days<=365*2:
    print(f'{days} gün, 2. Servis Aralığı')
elif days>365*2 and days<=365*3:
    print(f'{days} gün, 3. Servis Aralığı')
else:
    print('Hatalı süre bilgisi.')
