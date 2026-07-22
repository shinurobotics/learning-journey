class Vehicle:
    def __init__(self, brand, model, fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type

    def display_vehicle(self):
        print("Vehicle Information")
        print("-------------------")
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Fuel Type:", self.fuel_type)

class Motorcycle(Vehicle):
    def __init__(self, brand, model, fuel_type, engine_capacity):
        #copies the parent variable to the child
        super().__init__(brand, model, fuel_type)
        
        self.engine_capacity = engine_capacity

    def display_motorcycle(self):
        print("Motorcycle Information")
        print("----------------------")
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Fuel Type:", self.fuel_type)
        print("Engine Capacity:", self.engine_capacity, "cc")

    def start_engine(self):
        print(self.brand, self.model, "engine started!")


# Create a Vehicle object
vehicle1 = Vehicle("Toyota", "Corolla", "Petrol")

# Create a Motorcycle object
motorcycle1 = Motorcycle("Yamaha", "R15", "Petrol", 155)

# Display vehicle information
vehicle1.display_vehicle()
print()

# Display motorcycle information
motorcycle1.display_motorcycle()
print()

# Start the motorcycle engine
