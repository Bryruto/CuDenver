import sys
import csv


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

try:
    with open(sys.argv[1], "r" )as bfor , open(sys.argv[2],"w") as afor:
        before = csv.DictReader(bfor)
        after = csv.DictWriter(afor,fieldnames=["first","last","house"])
        after.writeheader()
        for row in before:
            last,first = row["name"].split(",")
            after.writerow({
                "first": first.strip(),
                "last": last.strip(),
                "house": row["house"]
            })
except FileNotFoundError:
    sys.exit("File does not exist")

