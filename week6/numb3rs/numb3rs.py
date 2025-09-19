import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if result := re.search(r"^([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$)",ip):
        part = []
        part = result.group(1).split(".")
        if len(part) >4:
            return False
        for p in part:
            if len(p) >=2:
                if p[0] == "0":
                    return False
        if 0 <= int(part[0]) <= 255 and 0 <= int(part[1]) <= 255 and 0 <= int(part[2]) <= 255 and 0 <= int(part[3]) <= 255:
            return True
    return False
if __name__ == "__main__":
    main()
