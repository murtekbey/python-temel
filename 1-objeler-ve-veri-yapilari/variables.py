maasAli = 5000
maasAhmet = 4000
vergi = 0.27

print(maasAli - (maasAli * vergi))
print(maasAhmet - (maasAhmet * 0.27))

# Değişken Tanımlama Kuralları
# * rakam ile başlayamaz.
number1 = 10
print(number1)

number1 = 20
print(number1)

number1 += 30
print(number1)

# büyük küçük harf duyarlılığı
age = 20
AGE = 30

print(age)
print(AGE)

# Türkçe karakter kullanmayalım
yas = 20
_age = 20

########################################################################################################################################################
x = 1               #int
y = 2.3             #float
name = "Murtek"     #string
isStudent = True    #bool
# YA DA
x, y, name, isStudent = (1, 2.3, "Murat", True) # Tek Satırda Anlatabilirsin.
########################################################################################################################################################
a = 10
b = 20
print(a+b) # 30

a = '10'
b = '20'
print(a+b) # 1020 (10 ile 20 yi yazı olarak tanıyıp birlestirir.)

firstName = "Murat"
lastName = " Altınpınar"
print(firstName + lastName) # Murat Altınpınar
