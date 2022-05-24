value = int(input('Введите сумму :  '))

bank = {5000: 0, 2000: 0, 1000: 0, 500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 3: 0, 1: 0}


def get_money(s):
    for k, v in bank.items():
        if s == 0:
            break
        while s >= k:
            bank[k] += 1
            s -= k
    if s == 0:
        print('Ваши деньги : ', bank)
    else:
        raise ValueError


get_money(value)