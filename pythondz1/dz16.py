a = input("Напишите имя файла : ")
print(a[a.rfind('.') + 1:] if '.' in a else "с файлом что то не так")


