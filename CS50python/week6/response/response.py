import sys
from validator_collection import validators, errors

try:
    email_address = validators.email(input("email: "))
    print("Valid")
except errors.InvalidEmailError:
    print("Invalid")

