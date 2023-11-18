score = float(input("Enter score: "))

if score < 0:
    print("Invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("pass")
else:
    print("Bad")