name = 'Murat'
surname = 'Altınpınar'
age = 36

print('My name is {} {}'.format(name, surname)) # index sırasına göre
print('My name is {1} {0}'.format(name, surname)) # index numaraları vererek
print('My name is {s} {n}'.format(n=name, s=surname)) # değişken tanımlayarak
print('My name is {} {} and I am {} years old.'.format(name, surname, age)) 

result = 200 / 700 # 0.2857142857142857
print('the result is {r:1.5}'.format(r=result)) # {r:1.5} diyerek 1-5 arası indexe denk gelen numaraları alıp kısalttık.

print('My name is {} {} and I am {} years old.'.format(name, surname, age))
print(f'My name is {name} {surname} and I am {age} years old.') # yeni gelen sistem stringin basina "f" ekleyerek hepsi yazılabilir.
