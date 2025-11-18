import csv
def main():
    filename = "students.csv"

    # Explicit open
    f = open(filename, "r", newline="")

    reader = csv.reader(f)
    print (type(reader))

    # Read header
    header = next(reader)
    print("Header:", header)
    print (type(header))

    print("\nRows:")
    header = next(reader)
    # Loop just like "for line in file"
    try:
        while header:
            name = header[0]
            age = int(header[1])
            major = header[2]
            header = next(reader)

        # row is already split into fields by csv.reader
            print(f"Name: {name}, Age: {age}, Major: {major}")
    except Exception as e:
        print(e)
    # Explicit close

    f.close()
main()
"""for row in reader:
        
        # row is already split into fields by csv.reader
        name = row[0]
        age = int(row[1])
        major = row[2]

        print(f"Name: {name}, Age: {age}, Major: {major}")
"""