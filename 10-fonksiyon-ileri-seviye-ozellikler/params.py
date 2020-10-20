def toplama(a,b):
    return a+b
def cikarma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bolme(a,b):
    return a/b

def islem(f1,f2,f3,f4, islem_adi): # yukarıda hazırlamış olduğumuz fonksiyonları başka bir fonksiyona parametre olarak gönderiyoruz.
    if islem_adi == 'toplama': # örneğin islem fonksiyonunda f1 parametresi için toplama fonksiyonunu kullanıcaz.
        print(f1(2,8))
    elif islem_adi == 'cikarma':
        print(f2(5,3))
    elif islem_adi == 'carpma':
        print(f3(3,4))
    elif islem_adi == 'bolme':
        print(f4(10,2))
    else:
        print('Geçersiz işlem.')

islem(toplama, cikarma, carpma, bolme, 'toplama') # burada gördüğünüz gibi f1, f2, f3, f4 parametreleri için toplama, cikarma, carpma, bolme fonksiyonlarını kullandık.
islem(toplama, cikarma, carpma, bolme, 'cikarma')
islem(toplama, cikarma, carpma, bolme, 'carpma')
islem(toplama, cikarma, carpma, bolme, 'bolme')
islem(toplama, cikarma, carpma, bolme, 'asdasd')