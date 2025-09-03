# Name:  Brycen Anderson

# Class: CSCI 1411-00X 

# Due Date: 9/3/2025

# Description: This is part 1 of lab 3. It reads in a temperature in  
# degree Fahrenheit and converts it to degree Celsius. 
# It also queries the user for their name and display a message. 

# Status: Runs as expected. 

 

def main(): 

    # first, ask the user for their first and last names 

    firstName = input ("Enter your first name ") 

    lastName = input ("Enter your last name ") 

 

    # now ask them for the temperature they wish to convert 

    fahren = (int)(input ("What is the temperature in Fahreneit? ")) 

 

    # next we convert using the standard F to C formula 

    celsius = (fahren-32)*(5/9) 

 

    # finally, print out the conversion 

    print ('Hello', firstName, lastName) 

    print (fahren, 'degree Fahrenheit is ', celsius, 'degrees Celsius')

main()