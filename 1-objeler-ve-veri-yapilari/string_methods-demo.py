website = "http://www.murtekbey.com"
course = "Python Programlama"

# 1-  ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
result = ' Hello World '.strip()
# result = ' Hello World '.lstrip() # soldan boşluk karakterini siler.
# result = ' Hello World '.rstrip() # sağdan boşluk karakterini siler.

result = website.lstrip('/pth:') # sol taraftaki parantezin içinde yer alan tüm karakterleri siler.

# 2- 'www.murtekbey.com' içindeki murtekbey bilgisi haricindeki her karakteri silin.
result = 'www.murtekbey.com'.strip('w.moc') # parantezin içinde yer alan tüm karakterleri siler.

# 3-  'course' karakter dizisinin tüm karakterlerini küçük harf yapın.
result = course.lower()

# 4- 'website' içinde kaç tane a karakteri vardır ? (count('a'))
result = website.count('a')
result = website.count('www') # www harfler dizisini arar.
result = website.count('www',0,10) # 0 ila 10 index içerisinde www harfler dizisini arar.


# 5- 'website' "www" ile başlayıp com ile bitiyor mu?
result = website.startswith('www')
result = website.endswith('com')

# 6-  'website' içinde '.com' ifadesi var mı?
result = website.find('.com')
result = website.find('.com',0,10) # 0 ila 10. arasındaki index değerinde arar.
result = website.rfind('.com') # Sağ tarafdan başlayarak .com değerini arar.

result = website.index('com') # .find metoduna alternatif .index methodu (aynıdır.)
result = website.rindex('com') # sağdan
# result = website.lindex('comm') # comm kelimesi yoksa .find ' da -1 değerini verir, .index methodunda hata verir. # exception (hata objesine karşılık gelen bir ifade.)

# 7- 'course' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)
result = course.isalpha() # string'deki ifadeler alfabetik mi diye sorgular.
result = 'Hello'.isalpha()
result = course.isdigit() # string'deki ifadeler numerik mi diye sorgular.
result = '12345'.isdigit()

# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
result = 'Contents'.center(50,'*') # ortaya yerleştirir.
result = 'Contents'.ljust(50,'*')  # sola yerleştirir.
result = 'Contents'.rjust(50,'*')  # sağa yerleştirir.

# 9-  'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.
result = course.replace(' ', '-') # (' ', '-') ifadesinin sonuna ,5 eklersek sadece 5 karakteri değiştirir.

# 10- 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin
result = 'Hello World'.replace('World', 'There')

# 11-  'course' karakter dizisini boşluk karakterlerinden ayırın. (aynı zamanda parçalayarak listeleme yapar.)
result = course.split(' ')

print(result)
