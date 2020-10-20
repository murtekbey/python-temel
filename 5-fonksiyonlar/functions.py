####################################################################################################################################
def sayHello(name = 'user'): 
    return 'Hello '+ name

msg = sayHello('Murat')

print(msg)

####################################################################################################################################
def total(num1, num2):
    return num1 + num2

result = total(10,20)

print(result)

####################################################################################################################################
def yasHesapla(dogumYili):
    return 2020 - dogumYili

ageMurat = yasHesapla(1994)

print(ageMurat)

####################################################################################################################################
def emekliligeKacYilKaldi(dogumYili, isim):
    '''
    DOCSTRING: Dogum yiliniza gore emekliliginize kac yil kaldigini hesaplar.
    INPUT: Dogum yili
    OUTPUT: Hesaplanan yil bilgisi
    '''
    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas

    if emeklilik > 0:
        print(f'Emekliliğinize {emeklilik} yıl kaldı.')
    else:
        print('Zaten emekli oldunuz.')

emekliligeKacYilKaldi(1994, 'Murat')
emekliligeKacYilKaldi(1950, 'Cennet')

print(help(emekliligeKacYilKaldi))

list = [1,2,3]

print(help(list.append))