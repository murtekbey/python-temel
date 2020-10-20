# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
# Kullanımı: open(dosya_adi, dosya_erişme_modu)
# dosya_erişme_modu => dosyayı hangi amaçla açtığınızı belirtir.

# "w": (Write) yazma modu. 
#   ** Dosyayı konumda oluşturur.
#   ** Dosya içeriğini siler ve yeniden ekleme yapar.

# file = open("newfile.txt","w") # Dosyayı oluşturduk.
# file = open("C:/users/murte/desktop/python_temelleri/newfile.txt", "w")
# file.close() # Dosyayı kapattık.

# file = open("newfile.txt","w", encoding='utf-8')
# file.write("Murat Altınpınar")
# file.close()


# "a": (Append) ekleme modu. Dosya konumda yoksa oluşturur.

# file = open("newfile.txt","a", encoding='utf-8')
# file.write("\nGurur Altınpınar")
# file.write("Gurur Altınpınar\n")
# file.close()

# "x": (Create) oluşturma modu. Dosya zaten varsa hata verir.

file = open("newfile2.txt","x", encoding='utf-8')

# "r": (Read) okuma modu. Varsayılan. Dosya konumda yoksa hata verir.