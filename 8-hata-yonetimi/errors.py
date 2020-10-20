# Error => Hata

# Error
# print(a) => NameError
# int('1a2') => ValueError
# print(10/0) => ZeroDivisionError
# print('denem'e) => SyntaxError 

# Error handling => Hata Yöntemi

# try: 
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)
# # except ZeroDivisionError:
# #     print('y için 0 girilemez.')
# # except ValueError:
# #     print('x ve y için sayısal değer girmelisiniz.')
# except (ZeroDivisionError, ValueError) as e: # Hataları e olarak atadık.
#     print('Yanlış bilgi girdiniz.')
#     print(e) # ZeroDivisionError mu yoksa ValueError mu bize söyler.

# try: 
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)

# except: # Hata türü ne olursa olsun bize Yanlış bilgi girdiniz ifadesini verir.
#     print('Yanlış bilgi girdiniz.')

while True:
    try: 
        x = int(input('x: '))
        y = int(input('y: '))
        print(x/y)

    except Exception as ex:
        print('Yanlış bilgi girdiniz.', ex)
    else:
        break
    finally:
        print('Try Except Sonlandı.')