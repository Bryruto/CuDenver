import sys
import pyfiglet
import random

figlet = pyfiglet.Figlet()
font_list = figlet.getFonts()

# Check if user passed the correct number of arguments
if len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        font_ = sys.argv[2]
        if font_ not in font_list:
            sys.exit("Font not found.")
    else:
        sys.exit("no font select")
elif len(sys.argv) == 1:
    font_ = random.choice(font_list)
else:
    sys.exit("you shall not pass")

say = input("Input: ")

figlet.setFont(font=font_)
print(figlet.renderText(say))


