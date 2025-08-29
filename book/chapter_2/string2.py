#make a list of places i want to go 
location = ["Dubai","Bail","Germany", "France", "Antarctica"]
print(f"{location} original list\n")

#print the sorted list but this does not change the list its temp just to print
print(f"{sorted(location)} sorted list \n")


#print to show you didnt change permanently 
print(f"{location} sorted did not change the list permanently\n")

#print the list in reverse order 
print(f"{sorted(location,reverse = True)} reverse on sorted \n")

#change the list to sorted and it is saved like that
location.sort()

print(f"{location} used sort on the list this does change the original list \n")

#change the sort list in reverse it saves like that
location.sort(reverse=True)

print(f"{location} used sort so changed the original list and add the reverse = True to to sort backwords \n")

#this also saves but just flips it
location.reverse()

print(f"{location} now this is just the reverse function\n")

#this used two times just puts the list back where it was same as not runing it at all 
location.reverse()

print(f"{location} used reverse again so just what it was before\n")


