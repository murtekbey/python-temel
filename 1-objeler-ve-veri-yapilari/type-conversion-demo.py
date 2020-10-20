'''
    Daire Alanı   : πr²
    Daire Çevresi : 2πr    

    * Yarı çapı verilen bir dairenin alan ve çevresini 
    hesaplayınız. (r: 3.14)
'''

pi = 3.14 # pi sayısına değer verdik.
r = float(input("Yarı Çap: ")) # kullanıcıdan dairenin yari cap degerini aldik

alan = pi * (r ** 2) # alan hesaplama formülü
print(type(alan)) # komutun türünü yazdırmak

cevre = 2 * pi * r # cevre hesaplama formülü
print(type(cevre)) # komutun türünü yazdırmak

print("Alan: "+ str(alan) +" Çevre: "+ str(cevre)) # alan ve cevre bilgisi float bir bilgi olduğu için 'str()' komutu ile string'e donusturduk.