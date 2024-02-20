class Car:
    def __init__(self, brand, speed = 0): #para moverse de class a object
        self.car_brand = brand  #self punto algo es un atributo, el otro brand es una variable
        #el atributo funciona en toda la clase
        # mientras que brand es una viriable local
        self.speed = speed
    def set_speed(self, speed ): #self es el objeto itself
        self.speed = speed



    def get_brand_nationality(self): #self es el objeto itself
        if self.car_brand == "Renault":
            return "France"
        elif self.car_brand == "Ferrari":
            return "Italy"

    def set_age(self, age):
        self.age = age
    def __set__(self, value):
        self.value = value

mycar = Car("Renault", 30)
mycar.set_speed(80)
print(mycar.speed)

print(mycar.get_brand_nationality())

yourcar = Car("Ferrari", 250)
print(yourcar.speed)
