my_favorites = {32, 33, 34}
vals_favorites = {int(input())}
jans_favorites = {int(input())}
abes_favorites = {int(input())}

likeable_numbers= set.union(vals_favorites,jans_favorites,abes_favorites,my_favorites)



print(f"My favorite numbers: {sorted(my_favorites)}")
print(f"Val's favorite numbers: {sorted(vals_favorites)}") 
print(f"Jan's favorite numbers: {sorted(jans_favorites)}") 
print(f"Abe's favorite numbers: {sorted(abes_favorites)}") 
print(f"Likeable numbers: {sorted(likeable_numbers)}")