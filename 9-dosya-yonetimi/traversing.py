with open("newfile.txt","r",encoding="utf-8") as file:
    content = file.read()
    print(content)
    file.seek(0)
    print(file.tell())
    content2 = file.read()
    print(content2)
