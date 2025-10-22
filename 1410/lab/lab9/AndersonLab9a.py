# Name:  Brycen Anderson

# Class: CSCI 1411-003

# Due Date: 10/21/2025

# Description: This program how to use functions in a Python
# program. It also shows how to use parameters to pass data
# to a function and return data from a function using a return
# statement.

# Status: Runs as expected.

# f_to_c function
# parameter: Temperature in degree Fahrenheit (fahrenheit)
# returns equivalent temperature in degree Celsius
def f_to_c(fahrenheit):
    result = (fahrenheit - 32) * (5.0 / 9.0)
    return result

# f_to_c_list function
# parameter: a list of temperature in degree Fahrenheit(temp_list)
# It coverts the temperatures in list to equivalent temperatures in
# Celsius. There is no return statement as data is returned using
# the list that is passed as an argument.
def f_to_c_list(temp_list):
    for i in range(len(temp_list)):
        fahrenheit = temp_list[i]
        celsius = f_to_c (fahrenheit)
        temp_list[i] = round(celsius,2)

# main function
def main():  
    temp_list = []
    # Ask user for a set of 5 temperature in degree Fahrenheit
    for i in range(5):
        fahrenheit = float(input("Enter temperature in degree Fahrenheit: "))
        temp_list.append(fahrenheit)

    # call the function f_to_c_list
    f_to_c_list(temp_list)
    print("The converted temperature list")
    print(temp_list)

main()