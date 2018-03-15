score = float(input("Enter your score: "))
if score < 0 or score > 100:
    print("Invalid score, try again")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")