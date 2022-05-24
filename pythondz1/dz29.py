x = int(input("Введите координат : "))
y = int(input("Введите координат : "))
if x > 0 and y > 0:
    print("Вы в первой четверти!")
elif y > 0 and x < 0:
    print("Вы во второй четверти!")
elif x < 0 and y < 0:
    print("Вы в третей четверти!")
elif y < 0 and x > 0:
    print("Вы в четвертой четверти!")
else:
    print("Ошибка")
