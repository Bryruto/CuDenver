import sys
from PIL import Image, ImageOps

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
end1= sys.argv[1].split(".")
end2 = sys.argv[2].split(".")
if end1[1] != end2[1]:
    sys.exit("Input and output have different extensions")
try:
    with Image.open(sys.argv[1]) as pic:
        with Image.open("shirt.png") as shirt:
            pic = ImageOps.fit(pic, shirt.size)
            pic.paste(shirt, (0, 0), shirt)
            pic.save(sys.argv[2])
except FileNotFoundError:
    sys.exit("Invalid input ")
