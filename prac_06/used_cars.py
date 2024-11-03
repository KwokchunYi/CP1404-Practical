"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from car import Car


def main():
    """Demo test code to show how to use the Car class."""

    # Create a Car object named "my_car" with 180 units of fuel
    my_car = Car(name="My Car", fuel=180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)  # This will use the __str__ method to display car details

    # Create another Car object named "limo" with 100 units of fuel
    limo = Car(name="Limo", fuel=100)
    limo.add_fuel(20)
    limo.drive(115)
    print(limo)  # Display the limo car details to test __str__ method


main()