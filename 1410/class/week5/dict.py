def main():
    my_dict= {"a":1,"b":2}
    print("\nintial values in the dict", my_dict)

    my_dict["c"] = 3
    print("adding a 3 ",my_dict)

    my_dict["a"] =100
    print("changing the dict at key a to 100:",my_dict)

    x = my_dict.pop("b")
    print("\n after pop the dict is ",my_dict,"the pop i got is",x)

    del my_dict["a"]
    print("\nafter del my dict is",my_dict)
main()