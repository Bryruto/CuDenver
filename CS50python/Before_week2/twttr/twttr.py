name = input("Input: ")
new = ""
for char in name:
    match char:
        case 'A' | 'E' | 'I' | 'O' | 'U' | 'a' | 'e' | 'i' | 'o' | 'u':
            char = ""
    new += char

print(f"Output:{new}")
