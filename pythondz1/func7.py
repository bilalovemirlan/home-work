arr = [10, 20, 30, 40, 0, -10, -20, -30, -40]


def divide(array):
    pos = []
    neg = []
    for i in array:
        if i >= 0:
            pos.append(i)
        elif i < 0:
            neg.append(i)
    return pos, neg


print(divide(arr))