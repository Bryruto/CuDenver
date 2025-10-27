# Name:  Brycen Anderson

# Class: CSCI 1411-003

# Due Date: 10/21/2025

# Description: This is of lab 9
#ask for date (mm/dd/yyyy) then give it back in long fomat

# Status: Runs as expected.
def month_to_name(number:str)->str:
   # month_names = {
    #"01": "January",
#    "02": "February",
 #   "03": "March",
  #  "04": "April",
   # "05": "May",
   # "06": "June",
 #   "07": "July",
  #  "08": "August",
   # "09": "September",
   # "10": "October",
   # "11": "November",
   # "12": "December",
#}
    months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    try:
        return months[int(number)-1]
    except:
        print(int(number))
        return "not here"
   # if number in month_names:
    #    return month_names[number]
    #return "not here"

    
def split_date(date:str)->list:
    return date.split("/") 

def date_convert(date:str)->str:
    month,day,year = split_date(date)
    month = month_to_name(month)

    return f"{date} in long fomat is {month} {day}, {year}"

def main():
    date = date_convert(input("Enter date:"))
    print(date)
main()