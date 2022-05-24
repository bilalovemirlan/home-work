
earn_money = int(input("Сколько хотите накопить ? :"))
bank = 0
while True:
    if bank < earn_money and bank != earn_money:
         money = int(input("Взнос  :"))
         bank = bank + money
    else:
         print(f'Поздравляю! Вы накопили {bank} сомов!')
         break