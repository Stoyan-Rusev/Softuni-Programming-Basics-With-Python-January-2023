degreece = int(input())
time_of_day = input()

clothes = None
shoes = None

if time_of_day == "Morning":
    if 10 <= degreece <= 18:
        clothes = "Sweatshirt"
        shoes = "Sneakers"
    elif 18 < degreece <= 24:
        clothes = "Shirt"
        shoes = "Moccasins"
    elif degreece >= 25:
        clothes = "T-Shirt"
        shoes = "Sandals"

elif time_of_day == "Afternoon":
    if 10 <= degreece <= 18:
        clothes = "Shirt"
        shoes = "Moccasins"
    elif 18 < degreece <= 24:
        clothes = "T-Shirt"
        shoes = "Sandals"
    elif degreece >= 25:
        clothes = "Swim Suit"
        shoes = "Barefoot"

elif time_of_day == "Evening":
    if 10 <= degreece <= 18:
        clothes = "Shirt"
        shoes = "Moccasins"
    elif 18 < degreece <= 24:
        clothes = "Shirt"
        shoes = "Moccasins"
    elif degreece >= 25:
        clothes = "Shirt"
        shoes = "Moccasins"

print(f"It's {degreece} degrees, get your {clothes} and {shoes}.")

