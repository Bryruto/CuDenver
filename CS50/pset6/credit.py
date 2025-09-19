import sys
while True:
    try:
        number = input("number: ")  # get card number #input is a string unless told otherwise
    except ValueError:  # if not a number
        print("not a number")
    else:
        break  # leave the loop
digits = []  # making a list just a way better array
for char in number:  # loops through each char in number
    digits.append(int(char))  # setting char in the number to an int in the list
digits.reverse()
total = 0
number = 0
new = 0
# start with index 1 then length of digits and then each time add 2 to skip
for i in range(1, len(digits), 2):
    number = digits[i]*2
    if number > 9:
        new = number % 10  # take the right digits or last
        new += (number // 10)  # grab the first digit and add to what the last was
        number = new  # set the new to number
    total += number  # add the total to number and put into total
for s in range(0, len(digits), 2):  # loop through the 0 index in digit and add to each time till lenght of digits is met
   total += digits[s]  # add all the digits to the total
if total % 10 == 0:  # if not 0 at the end then it is not valid
    digits.reverse()#reverse it back to the state it was was before
    if digits[0] == 3 and digits[1] == 4 or digits[1] == 7 and len(digits) == 15:#check to see the size and first 2 numbers is right
        print("AMEX")
    elif (digits[0] == 5 and (digits[1] >= 1 and digits[1] <= 5) )and len(digits) ==16:
        print("MASTERCARD")
    elif digits[0] == 4 and len(digits) == 16 or len(digits) == 13:
        print("VISA")
    else:
        print("INVALID")
else:
     print("INVALID")
