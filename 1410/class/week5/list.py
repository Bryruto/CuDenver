def main():
    my_list= [1,2,3]
    print("\nbefore adding new values ", my_list)#[1,2,3]
    my_list.append(4)
    print("\nafter appending 4 ",my_list)#[1,2,3,4]
    my_list.insert(1,10)
    print("\nafter inserting '10' into position 1", my_list)

    my_list.remove(2)
    print("\nafter removing the value 2", my_list)
    x = my_list.pop(2)
    print("\nafter poppong the valur at location 2",my_list)
    print("\nitem is popped", x)

    del my_list[1]
    print("\nafter deleting the value at location 1", my_list)#[1,4]
main()