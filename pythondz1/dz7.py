q = int(input( "Введите ваш оклад : "))
w = int(input( "Кол-во календарных дней по производственному календарю : "))
e = int(input( "Введите фактических отработанных дней : "))
r = int(input( "Кол-во премии : "))
t = 13
y = int(input( "Различные удержания : "))
u = (q/w * e + r) * ((y - t) / 100) - y
print(u)
