car_model = input('Какую машину желаете lexus или toyota? : ')
year = int(input('Какого года машину хотите выбрать? : ' ))
pzrobeg = int(input('C пробегом : '))
color = input('Цвет машины : ')
rul = input('Рульс лева или с права : ')
hoz = int(input('Хозяев до вас : '))
price = int(input('Цена : '))

if car_model in ['lexus', 'toyota'] and year >= 2004 and probeg == 150000 and color in ['grey', 'white'] and rul == 'lev' and hoz <= 2 and price <= 10000:
    print('Отлиный выбор')
elif car_model in ['lexus', 'toyota'] and year >= 2004 and probeg == 200000 and color in ['grey', 'white'] and rul == 'lev' and hoz <= 2 and price >= 8000:
    print('Отличный выбор')
else:
    print('К сожелению не смогли подобрать')
