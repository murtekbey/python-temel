
#key - value

# 41 => kocaeli, 34 => istanbul

sehirler = ['Kocaeli', 'İstanbul']
plakalar = [41, 34]

print(plakalar[sehirler.index('Kocaeli')]) # Kocaeli'nin olduğu indexi 'sehirler' üzerinden alır ve 'plakalar' da aynı indexdeki değeri getirir.
print(plakalar[sehirler.index('İstanbul')]) # index Sıralarının birbirine uyuyo olmasi gerekir.

print(plakalar[sehirler.index('Kocaeli')]) 
print(plakalar[sehirler.index('İstanbul')]) 
plakalar = { 'Kocaeli' : 41, 'İstanbul' : 34 }

print(plakalar['Kocaeli'])
print(plakalar['İstanbul'])

plakalar['Ankara'] = 6 # listeye yeni bir key - value değeri atadık.
plakalar['Kocaeli'] = 'New Value' # Kocaeli'nin 41 olan Value değerini 'New Value' olarak değiştirdik.

print(plakalar)

users = {
    'murataltinpinar' : {
        'age' : 26,
        'roles' : ['admin', 'user'],
        'email' : 'ornek@gmail.com',
        'adress' : 'Antalya',
        'phone' : '05451213693'
    },
    'gururaltinpinar' : {
        'age' : 18,
        'roles' : ['admin', 'user'],
        'email' : 'ornek2@gmail.com',
        'adress' : 'Dokuma',
        'phone' : '05552521424'
    }
}

# print(users['murataltinpinar']['age'])
# print(users['murataltinpinar']['email'])
# print(users['murataltinpinar']['adress'])
print(users['murataltinpinar']['roles'][0])