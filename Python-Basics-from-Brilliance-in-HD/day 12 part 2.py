class Robot:
    def __init__(self, robot_name, robot_id, battery_level):
        self.robot_name = robot_name
        self.robot_id = robot_id
        self.battery_level = battery_level

    def display_robot(self):
        print("Robot Information")
        print("-----------------")
        print("Robot Name:", self.robot_name)
        print("Robot ID:", self.robot_id)
        print("Battery Level:", self.battery_level, "%")

    def charge_robot(self):
        self.battery_level = 100
        print("\nRobot fully charged!")


class DeliveryRobot(Robot):
    def __init__(self, robot_name, robot_id, battery_level, package_count):
        super().__init__(robot_name, robot_id, battery_level)
        self.package_count = package_count

    def display_delivery_robot(self):
        print("Delivery Robot Information")
        print("--------------------------")
        print("Robot Name:", self.robot_name)
        print("Robot ID:", self.robot_id)
        print("Battery Level:", self.battery_level, "%")
        print("Packages:", self.package_count)

    def deliver_package(self):
        if self.package_count > 0:
            self.package_count -= 1
            self.battery_level -= 10
            print("\nPackage delivered successfully!")
        else:
            print("\nNo packages left to deliver.")


# Create a Robot object
robot1 = Robot("Atlas", "R101", 80)

# Create a Delivery Robot object
robot2 = DeliveryRobot("CourierBot", "D201", 90, 5)

# Display robot information
robot1.display_robot()
print()

# Display delivery robot information
robot2.display_delivery_robot()
print()

# Deliver one package
robot2.deliver_package()
print()

# Display updated information
robot2.display_delivery_robot()
print()

# Charge the robot
robot2.charge_robot()
print()

# Display updated information
robot2.display_delivery_robot()
