###################################################################################################################################
# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
sayi = int(input('Sayı: '))
if (sayi > 0) and (sayi<=100):
    print('Sayı 0 ile 100 arasında.')
else:
    print('Sayı 0 il 100 arasında bir sayı değil.') 
###################################################################################################################################
# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
sayi = int(input('Sayı: '))
if (sayi > 0):
    if (sayi % 2 == 0):
        print('Girilen sayı pozitif ve çift bir sayıdır.')
    else:
        print('Girilen sayı pozitif ancak tek bir sayıdır.')
else:
    print('Girilen sayı negatif bir sayıdır.')
###################################################################################################################################
# 3- Email ve parola bilgileri ile giriş kontrolü yapınız.
email = 'murtekbey@gmail.com'
password = 'murtek2q'
girilenEmail = input('E-Mail: ')
girilenPassword = input('Parola: ')

if (girilenEmail.lower() == email):
    if (girilenPassword.lower() == password):
        print('Bilgileriniz doğru.')
    else:
        print('Parolanız hatalı.')
else:
    print('E-Mail adresiniz hatalı.')
###################################################################################################################################
# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
a = int(input('1.Sayı: '))
b = int(input('2.Sayı: '))
c = int(input('3.Sayı: '))

if (a > b) and (a > c):
    print(f'1. sayı en büyük sayıdır.')
elif (b > a) and (b > c):
    print(f'2. sayı en büyük sayıdır.')
elif (c > a) and (c > b):
    print(f'3. sayı en büyük sayıdır.')
else:
    print('Girdiğiniz bilgiler hatalı.')
###################################################################################################################################
# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti, değilse kaldı yazdırın.
#    a-) Ortalama 50 olsa bile final notu en az 50 olmalıdır.
#    b-) Finalden 70 alındığında ortalamanın önemi olmasın.
vize1 = float(input('1. Vize: '))
vize2 = float(input('2. Vize: '))
final = float(input('Final: '))
ortalama = (((vize1 + vize2)/2 )* 0.6) + (final * 0.4)

# Benim Yazdığım KOD!
if (final < 50):
    print(f'Sınıfı geçemediniz. Final notunuz en az 50 olmalıdır. Ortalama: {ortalama}')
elif (final >= 70):
    print(f'Sınıfı final notunuz 70 üzeri olduğu için geçtiniz. Ortalama: {ortalama}')
elif (ortalama >= 50):
    print(f'Sınıfı geçtiniz. Ortalama: {ortalama}')
else:
    print(f'Sınıfı geçemediniz. Ortalama: {ortalama}')

"""
# Sadik Turan'ın Yaptığı 1. **
if (ortalama>=50):
    if (final>=50):
        print(f'Öğrencinin Ortalaması: {ortalama}, Geçme Durumu: Başarılı')
    else:
        print(f'Öğrencinin Ortalaması: {ortalama}, Geçme Durumu: Başarısız (Finalden en az 50 almanız gerekiyor.)')
else:
    print(f'Öğrencinin Ortalaması: {ortalama}, Geçme Durumu: Başarısız')


# Sadık Turan'ın Yaptığı 2. **
if (ortalama >=50):
    print(f'Öğrencinin Ortalaması: {ortalama}, Geçme Durumu: Başarılı')
else:
    if (final>=70):
        print(f'Öğrencinin Ortalaması: {ortalama}, Geçme Durumu: Başarılı (Finalden 70 ve üzeri aldığınız için geçtiniz.')
    else:
        print(f'Öğrencinin Ortalaması: {ortalama}, Geçme Durumu: Başarısız')
"""
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

#zayif = (formul >= 0) and (formul <= 18.4)
#normal = (formul >= 18.5) and (formul <= 24.9)
#kilolu = (formul >= 25.0) and (formul <= 29.9)
#obez = (formul >= 30.0) and (formul <= 34.9)

print(f'{ad} isimli kişinin, Vücut Kitle Indeksi; {formul}')

if (formul >= 0) and (formul <= 18.4):
    print('Durum : Zayıf')
elif (formul >= 18.5) and (formul <= 24.9):
    print('Durum : Normal')
elif (formul >= 25.0) and (formul <= 29.9):
    print('Durum : Kilolu')
elif (formul >= 30.0) and (formul <= 34.9):
    print('Durum : Obez')
else:
    print('Hatalı bilgi girdiniz.')
