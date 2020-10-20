website = "http://www.murtekbey.com"
course = "Python Programlama"

# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır?
result = len(course)

# 2- 'website' içinden www karakterlerini alın.
result = website[7:10]

# 3- 'website' içinden com karakterlerini alın.
result = website[-3:]

# 4- 'course' içinden ilk 15 ve son 15 karakterlerini alın.
result = course[:15]
result = course[-15:]

# 5- 'course' ifadesindeki karakterleri tersden yazdırın.
result = course[::-1]

s = '12345' * 5 # 5 kez yazılı string ifadesini yan yana getirir.
print(s[::5]) # 5 kez yazılacak olan string ifadesinde her seferinde 5. karakteri alacak

name, surname, age, job = 'Bora', 'Yılmaz', 32, 'mühendis'

# 6- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
# 'Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis.'
result = 'Benim adım '+ name + ' ' + surname + ', Yaşım ' + str(age) + ' ve mesleğim ' + job
result = 'Benim adım {} {}, Yaşım {} ve mesleğim {}'.format(name, surname, age, job)
result = f'Benim adım {name} {surname}, Yaşım {age} ve "mesleğim" {job}'

# 7- Hello world ifadesindeki w harfini 'W' ile değiştirin.
s = 'Hello world'
s = s[0:6] + 'W' + s[-4:] 
print(s)

# 8- 'abc' ifadesini yan yana 3 defa yazdırın.
result = 'abc ' * 3
print(result)
