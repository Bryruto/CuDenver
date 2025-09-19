import sys

fruit = input("Item: ").lower()
cal=0

match fruit:
    case "apple":
        cal += 130
    case "avocado" | "cantaloupe" | "honeydew melon" | "pineapple" | "strawberries" | "tangerine":
        cal += 50
    case "banana":
        cal += 110
    case "grapefruit":
        cal += 60
    case "grapes" | "kiwifruit":
        cal += 90
    case "lemon":
        cal += 15
    case "lime":
        cal += 20
    case "nectarine" | "peach":
        cal += 60
    case "orange":
        cal += 80
    case "pear" | "sweet cherries":
        cal += 100
    case "plums":
        cal += 70
    case "watermelon":
        cal += 80
if cal == 0:
    sys.exit()
else:
    print(f"Calories: {cal}")
