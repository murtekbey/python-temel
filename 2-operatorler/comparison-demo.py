###################################################################################################################################
# 1- Girilen 2 sayıdan hangisi büyüktür?
a = int(input('1.sayı: '))
b = int(input('2.sayı: '))

result = (a > b)
print(f'a:({a}) b:({b}) den büyüktür: {result}')
###################################################################################################################################
# 2- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
vize1 = float(input('1.Vize: '))
vize2 = float(input('2.Vize: '))
final = float(input("Final: "))
ortalama = (vize1/100)*30 + (vize2/100)*30 + (final/100)*40 # ya da bunun yerine,
ortalama = (((vize1 + vize2) / 2) * 0.6) + (final * 0.4) # vize1 ile vize2 yi topladıktan sonra 2'ye bölüp %60'nı alıyoruz.
print(f'Not Ortalamanız : {ortalama} ve dersten geçme durumunuz: {ortalama>=50}')
###################################################################################################################################
# 3- Eğer ortalama 50 ve üstündeyse geçti, değilse kaldı yazdırın.
if ortalama > 50:
    print('Geçti.')
else:
    print('Kaldı.')
###################################################################################################################################
# 4- Girilen bir sayının tek mi çift mi olduğunu yazdırın.
sayi = int(input('Sayı: '))
tekcift = (sayi % 2 == 0) # Sayı'nın 2 ye bölümünden kalan 0 oluyosa, Sayı çiftdir.
print(f'Girilen sayının çift olma durumu: {tekcift}')
###################################################################################################################################
# 5- Girilen bir sayının negatif pozitif durumunu yazdırın.
sayi = int(input('Sayı: '))
pozitifmi = (sayi > 0) # Sayı 0'dan büyükse pozitifdir.
print (f'Girilen sayının pozitif olma durumu: {pozitifmi}')
###################################################################################################################################
# 6- Parola ve E-Mail bilgisini isteyip doğruluğunu kontrol edin.
email = 'email@sadikturan.com'
password = 'abc123'
useremail = input('Mail: ') # Girilen bilgi zaten string olduğu için bir dönüşüm yapmaya gerek yok.
userpassword = input('Şifre: ') # Girilen bilgi zaten string olduğu için bir dönüşüm yapmaya gerek yok.

isEmail = (email == useremail.lower().strip()) # Burada .lower() komutu kullanırsak, e-mail büyük küçük farketmez. # .strip() komutu kullanırsak bırakılan boşlukları siler.
isPassword = (password == userpassword)
print(f'E-Mail bilgisi doğru mu: {isEmail}, Parola bilgisi doğru mu: {isPassword}')

verification = [email == useremail, password == userpassword] # BENİM YAZDIĞIM KOD
print (f'Girdiğiniz Kullanıcı Bilgileri: {verification}') # BENİM YAZDIĞIM KOD

# (email: , parola: abc123)
