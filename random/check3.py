def main():
    num_successes = 0

    while num_successes < 2:
        curr_height = int(input())
        if 17 <= curr_height <= 55:
            num_successes +=1
            print(curr_height)
main()