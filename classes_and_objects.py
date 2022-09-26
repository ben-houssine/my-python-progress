

class car:
    def __init__(self, type, age, weight):
        self.type = type
        self.weight = weight
        self.age = age
        self.car_aviable = "yes"
        print("A new car has ben created")
    
    def addWeight(self, dW):
        self.weight += dW


car1 = car('BMW 520i Limousine', 2014, 1790)
car2 = car('RS 6 Avant', 2008, 2150)
print(" ")

print('Car1: {}, {} Kg' .format(car1.type, car1.weight))
print('Car2: {}, {} Kg' .format(car2.type, car2.weight))

car1.addWeight(15) #adds extra weight to the standard value contained in 'class car'
print("Car1: {}" .format(vars(car1)))

#Outputs:
#A new car has ben created
#A new car has ben created

#Car1: BMW 520i Limousine, 1790 Kg
#Car2: RS 6 Avant, 2150 Kg
#Car1: {'type': 'BMW 520i Limousine', 'weight': 1805, 'age': 2014, 'car_aviable': 'yes'}
