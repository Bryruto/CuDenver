family = ["brycen","kylie","caden","taylor","diana","billy","aaron","enis","natilie"]

print(f"{family} original family")
print(f"{len(family)} people in my family")

print(f"if {family[0]} died i would have {len(family) - 1}")

family.remove("brycen")# only deletes the frist occurence of the value but it is lost after you remove 
#also can use pop or del
#dead = family.pop(0) with the index with pop you make a variable with the person stored there if pop() its the last index 
#del family[0] with the index just removes and you cant get it back
print(f"{family} removed brycen")
print(F"{sorted(family)} temp sorting the list with sorted")

family.reverse()
print(f"{family} now lets flip it with the reverse this is the original list being fliped ")

print(f"{family[-1]} <- so if you say [-1] this is the last element in the list/array [start : end] is how you can think about it [3:5] so this starts at index 1 then goes to index 5")
print("works alot like a loop just syntax different  ")