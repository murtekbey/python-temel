import mod # Aynı klasördeki mod.py dosyasına tanımladığımız modülü başka bir dosyada bu şekilde kullanabiliriz.

# result = help(mod)
# result = help(mod.func)
# result = mod.number
# result = mod.numbers
# result = mod.person
# result = mod.person["name"]
result = mod.person["Age"]
# result = mod.func(10)

p = mod.Person()
p.speak()

print(result)