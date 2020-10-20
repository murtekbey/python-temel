# username, password => database

# 'murataltinpinar', '123456'

a, b, c, d = 5, 5, 10, 4
password = '1234'
username = 'murtekbey'

result = (a == b) # True --> == ifadesi a, b'ye eşit mi diye sorar.
result = (a == c) # False
result = ('murtekbey' == username) # True
result = ('mrtkby' == username) # False
result = (a != b) # False != ifadesi a, b'ye eşit değil mi sorusu sorar. Soruyu tersten sormamızı sağlar.
result = (a != c) # True
result = (a > c) # False > ifadesi a, c'den büyük mü diye sorar.
result = (a < c) # True < ifadesi a, c'den küçük mü diye sorar.
result = (a >= b) # True >= ifadesi a, b'den büyük mü ya da eşit mi diye sorar. İki bilgiden biri doğruysa True cevabını alırız.
result = (a <= b) # True <= ifadesi a, b'den küçük mü ya da eşit mi diye sorar. İki bilgiden biri doğruysa True cevabını alırız.
result = (True == 1) # True --> True ifadesi 1'e karşılık geldiği için True cevabını alırız.
result = (False == 1) # False --> False ifadesi 1'e karşılık gelmediği için False cevabını alırız.
result = (False == 0) # True --> false ifadesi 0'a karşılık geldiği için True cevabını alırız.
result = False + True + 40

print(result)