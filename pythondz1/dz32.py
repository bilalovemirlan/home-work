x1 = int(input("Введите координат коня: "))
y1 = int(input("Введите координат коня: "))
x2 = int(input("Введите координат другой фигуры: "))
y2 = int(input("Введите координат другой фигуры: "))
if (x2-x1)==2 and (y2-y1)==1 or (x2-x1)==1 and (y2-y1)==2:
    print("Конь бьет фигуру")
else:
    print("Конь не бьет фигуру")
