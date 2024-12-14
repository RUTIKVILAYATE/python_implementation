class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + " !"

    def display_name(self):
        return f"The Car is {self.__brand} {self.model}"

car_ka_object = Car("Toyota","Corolla")
# display_ki_value = car_ka_object.__brand

print(car_ka_object.__brand)
print(car_ka_object.get_brand)



# Encapsulation
# Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

