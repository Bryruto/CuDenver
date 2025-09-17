def main():
    my_set = {1,2,3}
    print("initial values in set ", my_set)
    my_set.sdd(4)
    print("\nafter a 4", my_set)

    my_set.remove(2)
    print("\naafter removing 2 form the ser", my_set)
    my_set.discard(1)
    print  ("\n my set after discard",my_set)
    x= my_set.pop()
    print("\n my set after pop", my_set)
    print("pop element is", x)
main()