#make a list of places i want to go 
location = ["Dubai","Bail","Germany", "France", "Antarctica"]
print(f"{location} original list\n")

#print the sorted list
print(f"{sorted(location)} sorted list \n")


#print to show you didnt change permanently 
print(f"{location} sorted did not change the list permanently\n")

#print the list in reverse order 
print(f"{sorted(location,reverse = True)} reverse on sorted \n")

location.sort()

print(f"{location} used sort on the list this does change the original list \n")

location.sort(reverse=True)

print(f"{location} used sort so changed the original list and add the reverse = True to to sort backwords \n")

location.reverse()

print(f"{location} now this is just the reverse function\n")

location.reverse()

print(f"{location} used reverse again so just what it was before\n")


