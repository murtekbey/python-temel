###################################################################################################################################
numbers = []
for x in range(10):
    numbers.append(x)
print(numbers)

numbers = [x for x in range(10)] # x'in çerisine gelen değer x'in içerisindeki elemanları temsil ediyor.
print(numbers) # yukarıdaki işlemin aynısını tek satırda bu şekilde yapabiliriz.
################################################################################################################
for x in range(10):
    print(x**2)
numbers = [x**2 for x in range(10)]
print(numbers)

numbers = [x*x for x in range(10) if x%3==0] # yukarıdaki işlemin aynısını tek satırda bu şekilde yapabiliriz.
print(numbers)
################################################################################################################
myString = 'Hello'
myList = []

for letter in myString:
    myList.append(letter)
print(myList)

myList = [letter for letter in myString] # yukarıdaki işlemin aynısını tek satırda bu şekilde yapabiliriz.
print(myList)
################################################################################################################
years = [1994, 1999, 2008, 1956, 1986] 
ages = [2020-year for year in years] # 2020 sayısından years içerisinde olan değerlerin her birini for döngüsüyle çıkarttık ve yaşlarını bulduk.
print(ages) 
################################################################################################################
results = [x if x%2==0 else 'TEK' for x in range (1, 10)] # x'in liste içerisine dahil olmasını istiyorsak if koşulunu hemen sağına yazarız ve koşulu gerçekleştiriyorsa dahil olmasını bekleriz.
# Bu şekilde x değişkeni üzerinde istediğimiz değişikliği yaptırabiliriz.
print(results) # Çift olmayan sayılar yerine 'TEK' yazar.
################################################################################################################
result = []
for x in range(3): # 3'e kadar olan sayıları teker teker x içerisine aldık. 
    for y in range(3): # iç döngü'de oluşturup tekrar 3'e kadar olan sayıları teker teker y içerisine aldık.
        result.append((x,y)) # x ve y değerlerini result içerisine aktaralım.
print(result) # döngümüz x için 3 kere dönücek bitince aynı işlemi y içinde tekrar yapıcak. ve tüm kombinasyonları liste içerisine ekleyip yazdırıcak.
# [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
numbers = [(x,y) for x in range(3) for y in range(3)] # yukarıdaki işlemin aynısını tek satırda bu şekilde yapabiliriz.
print(numbers)
