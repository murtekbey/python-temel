
# # 1-100 e kadar.
# x = 1 # x'e 1 değerini verdik.
# while x <= 100: # x değeri 100 değerine eşit olana kadar döndür.
#     if x % 2==1: # eğer x değerinin 2 ye bölümünden kalan 1 ise;
#         print(f'sayı tek: {x}') # bu sayının tek olduğunu söyle.
#     else: # eğer x değerinin 2 ye bölümünden kalan 1 değil ise;
#         print(f'sayı çift: {x}') # bu sayının çift olduğunu söyle.
#     x += 1 # karşılığı x = x + 1 --> yani while döngüsü her çalıştığında x değeri 1 artacaktır. x değeri 100'e eşit olana kadar döngü devam eder.
# print('Bitti.') # 100'e kadar döngü bu şekilde devam eder. x değeri 100'e ulaştığında Bitti der.

name = '' # False --> name değerinin karşılığının boşluk olması False karşılık gelir.
while not name.strip(): # bizim için boşluk karakteri false olarak değerlendirildi. 
    # "while not" burada True'ya karşılık geliyor. 
    # .strip() komutu ile kişi inputa boşluk girse bile kabul etmez. .strip komutu boşlukları siler.
    name = input('isminizi giriniz: ') # name'in içine bir değer girmedikçe bize ismimizi sormaya devam eder. input ile bir değer girmemiz gerek.
print(f'Merhaba, {name}') # input değeri girildikten sonra bize ismimizi söyler.