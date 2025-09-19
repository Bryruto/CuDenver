import sys
dates = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
def main():
    while True:
        try:
            date =find_date()
        except Exception:
            pass
def find_date():
    months =""
    date = input("Date: ").title().strip()
    if ',' not in date:
        if '/' not in date:
            raise ValueError
    for char in date:
        if char.isalpha() == True:
            months += char
        else:
            break
    if months in dates:
        month = dates.index(months)+1
        month = str(month)
        date = date.replace(months,month)
        month,day,year = date.replace(',', '').split(" ")
    elif date[0].isnumeric()==True:#check if done the right way
        month,day,year = date.split('/')

    month= int(month)
    day = int(day)
    year= int(year)
    if month > 12:
        raise ValueError
    elif day >31:
         raise ValueError
    print(f"{year:04}-{month:02}-{day:02}")
    sys.exit()

main()




