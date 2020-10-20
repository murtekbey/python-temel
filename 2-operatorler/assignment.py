x = 5
y = 10
z = 20

x, y, z = 5, 16, 20

x, y = y, x

# x = x + 5 TOPLAMA
x += 5 

# x = x - 5 ÇIKARMA
x -= 5 

# x = x * 5 ÇARPMA
x *= 5 

# x = x / 5 BÖLME
x /= 5 

# x = x % 5 BÖLME'DEN KALAN (MOD)
x %= 5 

# y = y // 5 BÖLME (KALANSIZ), (TAMSAYI)
y //= 5 

# y = y ** 5 ÜSSÜ ÇARPMA 
y **= 5

# y = y ** z 
y **= z 


values = 1, 2, 3, 4, 5,

print(values)
print(type(values)) # tuple

x, y, *z = values # '*z' ile values değerinde dışarda kalan elemanları z için yeni bir liste oluşturarak içine ekledik.

print(x, y, z)
print(x, y, z[0]) # *z ile values'in içinde dışarda kalan elemanlar için oluşturduğumuz listeden 0. indexdeki elemanı aldık.
