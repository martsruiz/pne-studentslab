class Vehicle:
    def set_speed (self, speed):
        self.speed = speed
class Car(Vehicle):
    def __init__(self, brand, speed = 0):
        self.car_brand = brand
        self.speed = speed



class Ferrari(Car):


    def make_cabrio(self):
        self.speed = 20
        self.music = "loud"
        return "Wow"

mycar = Car("Renault")
yourcar = Ferrari("Ferrari")
print (yourcar.car_brand)
yourcar.set_speed(120)
print(yourcar.speed)

print(yourcar.make_cabrio (), "and music is", yourcar.music, "and speed is", yourcar.speed)
#print(mycar.make_cabrio (), "and music is", yourcar.music, "and speed is", yourcar.speed)
# #esto da error porque no entra en Ferarri ya que esta por debajo

