k = int(input('Укажите оюхват по бюсту : см'))
m = int(input('Укажите обхват бедер : см'))
n = int(input('Укажите обхват талии : см'))
t = int(input('Укажите рост : см'))
p = int(input('Укажите вес : кг'))
L = (k*m*t)//((n**2)*p)
print(L)