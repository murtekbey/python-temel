####################################################################################################################################
def changeName(n):
    n = 'ada'
    name = 'yiğit'
    changeName(name) # fonksiyona gönderdiğimiz name değerini - n ile değiştirdi.
    print(name) # yazdırdığınızda 'yiğit' bilgisi yazılır.

####################################################################################################################################
def change(n):
    n[0] = 'istanbul' # listede güncelleme yapıyoruz 0. indeksi değiştiriyoruz
    sehirler = ['ankara','izmir']
    n = sehirler[:] # slicing işlemi yaptık. 
    # sehirler üzerindeki bilgileri 'n' içine alır. orjinal listede bir değişiklik yapmaz n dizesi içerisine kopyalama yapar.
    # sehirler dizisi üzerinde bir güncelleme yapmamış olduk 
    # # ancak n dizesi üzerinde bir güncelleme yapmış olduk.
    change(sehirler[:])

####################################################################################################################################
def add(*params): # burda tuple listesi olmasını sağlıyor. verdiğimiz isim önemli değil. args ya da params olabilir.
    print(type(params))
    sum = 0
    for n in params:
        sum = sum + n
    return sum # sum bir fonksiyon. python kütüphanesiyle geliyor. soldan sağa değerleri toplar.

print(add(10, 20))
print(add(10, 20, 30))
print(add(10,25,35,45,66,80,95)) # tüm sayıları soldan sağa 'sum' fonksiyonu kullandığımız için toplar.

####################################################################################################################################
def displayUser(**args): # 2 yıldız ekliyo olmamız önemli. '**' demek dictionary listesi geleceği anlamına gelir.
    print(type(args))
    for key, value in args.items():
        print('{} is {}'.format(key, value))
displayUser(name = 'Murat', age = 26, city = 'Antalya')
displayUser(name = 'Gurur', age = 19, city = 'İzmir', phone = '05551112233')
displayUser(name = 'Hazal', age = 12, city = 'Menemen', phone = '05551112234', email = 'ornek@gmail.com')

####################################################################################################################################
def myFunc(a, b, c, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myFunc(10,20,30,40,50, 60, 70, key1 = 'value1', key2 = 'value2')
