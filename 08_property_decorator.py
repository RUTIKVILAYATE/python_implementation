# Property Decorator 

# use the property decorator in the Car class to make the model attribute read-only

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.__model = model

    def display_name(self):
        return f"The Car is {self.brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod       # if want to access method after it --> the method should be called by class directly without parameter self
    def general_description():
        return "Cars are means of transport"
    
    @property              # by this you cannot overwrite the model name
    def model(self):
        return self.__model


my_car = Car("Tata", "Safari")
# my_car.model = "City"
print(my_car.model)