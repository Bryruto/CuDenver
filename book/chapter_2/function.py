family = ["brycen","kylie","caden","taylor","diana","billy","aaron","enis","natilie"]

print(f"{len(family)} people in my family")

print(f"if {family[0]} died i wood have {len(family) - 1}")

family.remove("brycen")# only deletes the frist occurence of the value but it is lost after you remove 
#also can use pop or del
#dead = family.pop(0) with the index with pop you make a variable with the person stored there if pop() its the last index 
#del family[0] with the index just removes and you cant get it back
