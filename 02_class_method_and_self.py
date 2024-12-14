# Class Method and Self

# Add a method to the Car class that displays the full name of the car (brand and model)

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def display_name(self):
        return f"The Car is {self.brand} {self.model}"

car_ka_object = Car("Toyota","Corolla")
display_ki_value = car_ka_object.display_name()

print(display_ki_value)