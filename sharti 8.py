temp = float(input("Enter the water temperature: "))
if temp < 0:
    state = "frozen"
elif temp < 100:
    state = "liquid"
else:
    state = "vaporized"
print("The water is", state)
