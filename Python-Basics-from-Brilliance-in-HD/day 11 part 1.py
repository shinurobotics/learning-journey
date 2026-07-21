class Laptop:
    def __init__(self, brand_name, processor, ram_size, storage_size):
        self.brand_name = brand_name
        self.processor = processor
        self.ram_size = ram_size
        self.storage_size = storage_size

    def display_info(self):
        print("Laptop Information")
        print("-------------------")
        print("Brand:", self.brand_name)
        print("Processor:", self.processor)
        print("RAM:", self.ram_size, "GB")
        print("Storage:", self.storage_size, "GB")

    def upgrade_ram(self, extra_ram):
        self.ram_size += extra_ram
        print("RAM upgraded successfully!")

    def show_ram(self):
        print("Current RAM:", self.ram_size, "GB")


# Create first object
laptop1 = Laptop("Lenovo", "Intel i7", 16, 512)

# Create second object
laptop2 = Laptop("ASUS", "AMD Ryzen 7", 8, 256)

# Display information
laptop1.display_info()
print()

laptop2.display_info()
print()

# Upgrade RAM
laptop2.upgrade_ram(8)

# Show updated RAM
laptop2.show_ram()
