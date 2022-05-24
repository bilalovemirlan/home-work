ram = int(input('оперативная память : '))
if ram >= 4 and ram <= 8:
    print("дальше")
elif ram >= 8:
    print("Будет Дорохо Бохато")
ssd = int(input('Введите желаемый размер SSD : '))
if ssd >= 256:
    print("дальше")
elif ssd <= 256:
    print("Ты во сне чувак")
hdd = int(input("Введите желаемый размер HDD : "))
if hdd >= 1000:
    print("дальше")
elif hdd <= 1000:
    print("мдааа")
price = int(input("Введите цену : "))
if price > 1000:
    print("Бохатый шоли")
sos = input(str("Какое состояние ноутбука желаете б/у или Новый ? : "))
a = "б/у"
b = "новый"
if sos != b:
    print("Чиркин Пиркин асмандын башындасынго")
elif sos == a:
    print("Келтиресинда")
