###################################################################################################################################
# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
sayi = float(input('Sayı: '))
result = (sayi > 0) and (sayi<=100)
print(f'Sayı 0 ile 100 arasında mı: {result}')
###################################################################################################################################
# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
sayi = int(input('Sayı: '))
result = (sayi > 0) and (sayi % 2 == 0)
print(f'Girilen sayı pozitif ve çift sayı mı: {result}')
###################################################################################################################################
# 3- Email ve parola bilgileri ile giriş kontrolü yapınız.
email = 'admin'
password = '1234'

girilenEmail = input('E-Mail: ')
girilenPassword = input('Parola: ')

result = (girilenEmail == email) and (girilenPassword == password)
print(f'Girilen E-mail ve Parola: {result}')
###################################################################################################################################
# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
a = int(input('1.Sayı: '))
b = int(input('2.Sayı: '))
c = int(input('3.Sayı: '))

result = (a > b) and (a > c)
print(f'1. sayı en büyük sayıdır: {result}')

result = (b > a) and (b > c)
print(f'2. sayı en büyük sayıdır: {result}')

result = (c > a) and (c > b)
print(f'3. sayı en büyük sayıdır: {result}')
###################################################################################################################################
# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti, değilse kaldı yazdırın.
#    a-) Ortalama 50 olsa bile final notu en az 50 olmalıdır.
#    b-) Finalden 70 alındığında ortalamanın önemi olmasın.
vize1 = float(input('1. Vize: '))
vize2 = float(input('2. Vize: '))
final = float(input('Final: '))

ortalama = (((vize1 + vize2)/2 )* 0.6) + (final * 0.4)

result = ((ortalama >= 50) and (final >= 50)) or (final >= 70)

print(f'Ortalama: {ortalama}, Geçme Durumu: {result}')
###################################################################################################################################
# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#    Formül: (Kilo / boy uzunluğunun karesi)
#    Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#    0-18.4     => Zayıf
#    18.5-24.9  => Normal
#    25.0-29.9  => Fazla Kilolu
#    30.0-34.9  => Şişman (Obez)

ad = input('Ad: ')
kilo = float(input('Kilo: '))
boy = float(input('Boy: '))

formul =  kilo / (boy ** 2)
zayif = (formul >= 0) and (formul <= 18.4)
normal = (formul >= 18.5) and (formul <= 24.9)
kilolu = (formul >= 25.0) and (formul <= 29.9)
obez = (formul >= 30.0) and (formul <= 34.9)

print(f'{ad} isimli kişinin, Vücut Kitle Indeksi; {formul}')
print(f'Zayıf: {zayif}')
print(f'Normal: {normal}')
print(f'Fazla Kilolu: {kilolu}')
print(f'Şişman(Obez): {obez}')
