numbers = [1,2,3,4,5]
for num in numbers: # for yazıp kendimizin belirlediği bir değişken ismi(num) seçiyoruz. 
    # (listenin içerisinden tek tek elemanları al, num değişkeni içine at. her for döngüsü döndüğünde gelen num içeriğini yazdır.)
    print('num') # numbers'in içinde bulunan 5 elemanı teker teker yazdırır. 
###################################################################################################################################
names = ['Gurur', 'Murat', 'Efe']
for name in names:
    print(f'My name is {name}') # -> My name is Gurur, My name is Murat, My name is Efe
###################################################################################################################################
name = 'Murat Altınpınar'
for n in name:
    print(n) # Yukarıdaki string ifadenin her bir harfi tek tek yazdırılır. 
###################################################################################################################################
tuple = [(1,2),(1,3),(1,4),(1,5)] # Tuple listesi.
for t in tuple:
    print(t) # Her bir liste elemanı, bir tuple listesine karşılık gelir ve listeleri alt alta yazdırır. (1,2)-(1,3)-(1,4)-(1,5) gibi.
###################################################################################################################################
for a,b in tuple:
    print(a) # Tuple Listesinden sadece bir elemanı almış oluruz.
###################################################################################################################################
for a,b in tuple:
    print(a,b)
    # Tuple Listesinin her iki elemanını bu şekilde ayırarak alabiliriz. Liste içerisinde değil aynı dizede ayrı ayrı yazdırır.
###################################################################################################################################
d = {'k1':1,'k2':2,'k3':3} # Dictionary listesi.
for item in d:
    print(item) # Sadece key bilgileri gelir.
for item in d.items():
    print(item) # Bu şekilde key-value değerlerine ulaşabiliriz.
for key,value in d.items():
    print(key, value) # hem key, hem value değerine ulaşırız tuple'daki gibi.