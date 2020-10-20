"""def square(num): return num ** 2 # square diye bir fonksiyon tanımladık ve içerisine num diye bir değişken atadık. return ile bu değişkene dön ve 2 ile çarp dedik.

result = square(5) # result değerine square fonksiyonumuzu verdik ve değişkenimizin içerisine "2" yazdık.

print(result) # yazdırma sonucu ile sonucumuzu aldık.

############################################## -  MAP METODU - #######################################################################
# map metodunun yaptığı işlem dizin elemanlarını fonksiyona tek tek göndermek.
def square(num): return num ** 2
numbers = [1,3,5,9]

result = list(map(square, numbers)) # numbers içerisindeki her bir değeri fonksiyon içerisine gönderir 
                                    # ve işlem gördükten sonra return edilir. her birisini liste şeklinde ekrana yazdırır.
print(result)
# for item in map(square, numbers): # ya da for döngüsüyle alt alta bu şekilde ekrana yazdırabiliriz.
#     print(item)

############################################## - LAMBDA METODU - ################################################################################

numbers = [1,3,5,9]

lambdas = list(map(lambda num: num ** 2, numbers)) 
# lambda komutu ile sadece tek bir yerde bu fonksiyonu yapmak için bu şekilde kullandım def yada for döngüsü kullanmadım. 
# isimsiz bir fonksiyonla kullandik.

print(lambdas)

####################################################################################################################################
square =  lambda num: num ** 2 # ya da lambda fonksiyonuna bir isim verebilirim bu şekilde.

numbers = [1,3,5,9]

result = list(map(square, numbers)) # numbers içerisindeki elemanları map ve square(lambda) metodunu kullanarak bu şekildede yapabiliriz.

result = square(5) # ya da sadece square(lambda) metodunu bu şekilde çalıştırarak istediğimiz sayının karesini alırız. 

print(result)"""

############################################## - FILTER METODU - ################################################################################
numbers = [1,3,5,9,10,4]

# def check_even(num): 
    # return num%2==0
check_even = lambda num: num%2==0 # bu şekilde direk de yazabiliriz.

result = list(filter(check_even, numbers)) # filtre kullanıp sadece çift sayıları yazdırdık.
# result = list(filter(lambda num: num%2==0, numbers)) # fonksiyon kullanmadan lambda'yı direk list-filter içerisinde kullanabiliriz.

# result = check_even(numbers[2]) # 2. indeksdeki eleman tek olduğu için bize false bilgisi gönderir.

print(result)