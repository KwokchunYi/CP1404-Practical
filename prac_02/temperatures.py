def Celsius_to_Fahrenheit(celsius):
    """
    Convert celsius to Fahrenheit
    Formula:(celsius * 1.8) + 32
    """
    return(celsius * 1.8) + 32

def Fahrenheit_to_Celsius(Fahrenheit):
    """
    Convert Fahrenheit to Celsius
    Formula:(Fahrenheit - 32) / 1.8
    """
    return(Fahrenheit - 32) / 1.8

def main():
    option = input("A. Convert to celsius\nB. Convert to fahrenheit\nselect an option: ")
    value = float(input("Enter the value: "))
    if option == "A":
        print("converted celsius: " + str(Fahrenheit_to_Celsius(value)))
    elif option == "B":
        print("converted Fahrenheit: " + str(Celsius_to_Fahrenheit(value)))

    main()
