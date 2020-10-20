# Bankamatik Uygulaması

muratHesap = { # referans türde yapı
    'ad': 'Murat Altınpınar',
    'hesapNo': '23704683',
    'bakiye': 5000,
    'ekHesap': 12000
}

gururHesap = { # referans türde yapı
    'ad': 'Gurur Altınpınar',
    'hesapNo': '34692830',
    'bakiye': 22000,
    'ekHesap': 7000
}

def paraCek(hesap, miktar): # referans türde yapı olduğundan dolayı fonksiyon içerisinde yaptığım her işlem referans türünün içeriğini etkilicek. global olsa bile. ama referans tür de değilde tek tek atamış olsaydım fonksiyon içerisine kopyalama işlemi yapardı ve global olarak durumdan etkilenmezdi.
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print('Paranızı alabilirsiniz.')
        bakiyeSorgula(hesap)
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if (toplam >= miktar):
            ekHesapKullanimi = input('Yeterli bakiyeniz bulunmamaktadır. Ek hesabınızı kullanmak ister misiniz? (e/h)')
            
            if ekHesapKullanimi == 'e':
                ekHesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekHesapKullanilacakMiktar
                print('Paranızı alabilirsiniz.')
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadir.")
        else:
            print('Yeterli bakiyeniz bulunmadığından işleminizi gerçekleştiremiyoruz.')
            bakiyeSorgula(hesap)

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadir.\nEk hesabınızda {hesap['ekHesap']} TL bulunmaktadır.")

paraCek(muratHesap, 6000)

print('*'*50)

paraCek(muratHesap, 5000)