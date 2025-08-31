pizzas = ["cheese","pepperoni","meat lovers"]

for pie in pizzas:
    print(f" I love {pie} pizza : you can do it this way becuase python is cool -> for pie in pizzas\n")

for i in range(len(pizzas)):
    print(f" I like {pizzas[i]} pizza : i did this with index on the list -> for i in range(len(pizzas))\n")

print("these are my top 3 pizzas\n")

for i in range(1, 21):#count to 20
    print(i ,end = " ")

numbers = []

for i in range(1, 101):#it is 0 indexed so -1 at the end 
    numbers.append(i)

print(f"\n\n{sum(numbers)} getting the sum of the list\n")

print(f"{min(numbers)} getting the min of the list\n")

print(f"{max(numbers)} getting the max of the list\n")

sum(numbers)

#empty list for odd number
odd_num = []

for i in range(0,20,2):
    odd_num.append(i)

#empty list for number by 3 skipping 
threes = []

for i in range(0,30,3):
    threes.append(i)

print(f"list of 20 skip by 2 {odd_num} odd numbers \nlist of 30 skip by 3 {threes}\n")

cubes = []
for i in range(1,11):
    cubes.append(i**3)

print(cubes)
print()#did this for a new line

#comprehension
comp_cubes = [i**3 for i in range(1,11)]

print(f"{comp_cubes} this is short hand for the loop above comprehension")