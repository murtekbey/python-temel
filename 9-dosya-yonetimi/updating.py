# with open("newfile.txt","r+",encoding="utf-8") as file: # güncelleme işlemi.
#     file.seek(10)
#     file.write("deneme") 

# with open("newfile.txt","r+",encoding="utf-8") as file: # r+ komutu, hem okuma hem yazma modunu temsil eder.
#     print(file.read()) # dosyayı baştan sona okur.

############## - Sayfa Sonunda Güncelleme - ##############

# with open("newfile.txt","a",encoding="utf-8") as file: # append bi ekleme işlemi olduğu için cursor sayfanın en sonuna gider.
#     file.write("\nMurat Altınpınar")

############## - Sayfa Başında Güncelleme - ##############

# with open("newfile.txt","r+",encoding="utf-8") as file: 
#     content = file.read()
#     content = "Kadir Altınpınar\n" + content # Sayfanın en başına yazdırabiliriz bu şekilde.
#     file.seek(0)
#     file.write(content)

# with open("newfile.txt","r",encoding="utf-8") as file: 
#     print(file.read())

############## - Sayfa Ortasında Güncelleme - ##############

with open("newfile.txt","r+",encoding="utf-8") as file: 
    list = file.readlines() # Tüm içerik bir liste şeklinde gelir.
    list.insert(1,"Efe Özcan\n")
    file.seek(0) # Cursor'un konumu nereye aldığımız önemli.
    file.writelines(list) # Dosyayı satır olarak yazdırır.

with open("newfile.txt","r",encoding="utf-8") as file: 
    print(file.read())
