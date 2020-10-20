# 1-  "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
arabalar = ['Bmw', 'Mercedes', 'Opel', 'Mazda']


# 2-  Liste Kaç elemanlıdır ?
result = len(arabalar)


# 3-  Listenin ilk ve son elemanı nedir ?
result = arabalar[0]
result = arabalar[-1]


# 4-  Mazda değerini Toyota ile değiştirin.
# result = arabalar.replace('Mazda', 'Toyota') String değerlerine güncelleme yapamadığımız için bu komut çalışmaz.
arabalar[-1] = 'Toyota' # Fakat bu şekilde arabalar komutundaki string değerini değiştirebiliriz.
result = arabalar


# 5-  Mercedes listenin bir elemanı mıdır ?
result = 'Mercedes' in arabalar # Sorduğumuz değeri arar ve sonucu True yada False olarak söyler.


# 6-  Listenin -2 indeksindeki değer nedir ?
result = arabalar[-2]


# 7-  Listenin ilk 3 elemanını alın.
result = arabalar[0:3]
result = arabalar[:3]
result = arabalar[-2:]


# 8-  Listenin son 2 elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin.
arabalar[-2:] = ['Toyota', 'Renault']
result = arabalar


# 9-  Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
result = arabalar + ['Audi', 'Nissan']


# 10- Listenin son elemanını silin.
del arabalar[-1]
result = arabalar


# 11- Liste elemanlarını tersten yazdırınız.
result = arabalar[::-1]


# 12- Aşağıdaki verileri bir liste içinde saklayınız. 
      # studentA: Yiğit Bilgi 2010, (70,60,70)
      # studentB: Sena Turan  1999, (80,80,70)
      # studentC: Ahmet Turan 1998, (80,70,90) 

studentA = ['Yiğit','Bilgi',2010,[70,60,70]] # [70,60,70] formatıyla '[]' kullanarak, listenin içerisinden başka bir liste oluşturduk.
studentB = ['Sena','Turan',1999,[80,80,70]]
studentC = ['Ahmet','Turan',1998,[80,70,90]]


# 13- Liste elemanlarını ekrana yazdırınız.
result = studentA[0]
result = studentB[1]
result = studentC[3] # listenin içerisindeki listenin index değeri.
result = studentC[3][1] # liste içerisindeki listeden 2. elemani getirdik.

result = f"Yiğit Bilgi 9 yaşında ve not ortalaması 66"
result = f"{studentA[0]} {studentA[1]} {2019-studentA[2]} yaşında ve not ortalaması {int((studentA[3][0] + studentA[3][1] + studentA[3][2])/3)}" # yuvarlamak için integer değerinde yazdık.
print(result)
