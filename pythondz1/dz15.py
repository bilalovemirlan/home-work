raion = input("Какой район предпочитаете 'Ortosay', 'Baytik', 'Chonaryk' ")
mater = input("Материал дома желаете 'kirpich' or 'peskoblok' ")
sotka = int(input("Введите площадь участка : "))
summa = int(input("Введите сумму : "))

if raion == "Ortosay" or raion ==  "Baytik" or raion == "Chonaryk":
    print("Район по вашему запросу подходит")
if mater == "kirpich" and sotka <= 4 and summa <= 50000:
    print("Кирпичный дом")
elif mater == "peskoblok" and sotka <= 5 and summa <= 45000:
    print("Пескоблочный дом")
else:
    print("К сожелению дом не подходит")
