items = {}

while True:
    try:
        item = input().upper()
        if item not in items:
            items[item] = 1
        else:
            items[item] += 1
    except EOFError:
        break

# Sort the dictionary by value (count) in descending order
sorted_items = dict(sorted(items.items(), key=lambda item: item[0]))

for key, value in sorted_items.items():
    print(f"{value} {key}")

