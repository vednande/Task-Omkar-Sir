class Brand_Series:
    def __init__(self, brand, series, price):
        self.brand = brand
        self.series = series
        self.price = float(price)

class Car(Brand_Series):
    def __init__(self, brand, series, price, car_name):
        super().__init__(brand, series, price)
        self.car_name = car_name
    
    def display(self):
        print(f"Brand == {self.brand}\nSeries == {self.series}\nCar Name == {self.car_name}\nPrice == {self.price}")

class Bike(Brand_Series):
    def __init__(self, brand, series, price, bike_name):
        super().__init__(brand, series, price)
        self.bike_name = bike_name

    def display(self):
        print(f"Brand == {self.brand}\nSeries == {self.series}\nBike Name == {self.bike_name}\nPrice == {self.price}")


print()
c1 = Car("Honda", "VX", 2000000, "City")
c1.display()
print()

c2 = Car("Toyota", "Legender", 4500000, "Fortuner")
c2.display()
print()

c3 = Car("BMW", "M series", 7230000.78, "m5 competition")
c3.display()
print()

b1 = Bike("BMW", "S series", 1250000.47, "1000 RR")
b1.display()
print()
