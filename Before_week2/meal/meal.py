def main():
    time = input("What time is it? ").strip()
    time = convert(time)
    if 18.0 <= time <= 19.0:
        print("dinner time")
    elif time >= 12.0:
        print("lunch time")
    elif 7.00<= time <= 8.0:
        print("breakfast time")

def convert(time):
    hours, minutes = time.split(":")
    hours =float(hours)
    minutes = float(minutes)
    minutes = round(minutes/ 60.0,2)
    return hours+minutes

if __name__ == "__main__":
    main()
