"""
Hexadecimal Colour Code Lookup
Estimate: 15 minutes
Actual: 20 minutes
"""

# Constant dictionary containing color names and their hexadecimal codes
COLOUR_TO_HEX = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Aquamarine": "#7fffd4",
    "Azure": "#f0ffff",
    "Beige": "#f5f5dc",
    "Bisque": "#ffe4c4",
    "Black": "#000000",
    "BlanchedAlmond": "#ffebcd",
    "BlueViolet": "#8a2be2"
}

# Ask user for a color name, case-insensitive
colour_name = input("Enter colour name: ").capitalize()
while colour_name != "":
    if colour_name in COLOUR_TO_HEX:
        print(f"{colour_name} is {COLOUR_TO_HEX[colour_name]}")
    else:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").capitalize()
