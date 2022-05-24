class Airplane:

    def __init__(self, make, model, year, max_speed):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometer = 0
        self.is_flying = False

    def get_fly(self, km):
        self.odometer += km
        print(f'Oдометр показывает {self.odometer} км')

    def take_off(self):
        self.is_flying = True
        print(f'Самолет взлетел')
        return self.is_flying

    def land(self):
        self.is_flying = False
        print(f'Самолет приземлился')

a1=Airplane("Airbus", 320,2022,1200)
print(a1.__dict__)
a1.take_off()
a1.land()
a1.get_fly(10000)
a1.take_off()
a1.land()
a1.get_fly(10000)
a1.take_off()
a1.land()
a1.get_fly(15000)