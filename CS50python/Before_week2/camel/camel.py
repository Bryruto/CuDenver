while True:
    try:
        camel = input("camelCase: ")
    except ValueError:
        print("not a string")
    else:
        break
snake_case=""
for char in camel:
    if char.isupper():
        snake_case +="_"
    snake_case += char
print(f"snake_case:{snake_case.strip().lower()}")


