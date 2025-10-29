# Name:  Brycen Anderson

# Class: CSCI 1411-003

# Due Date: 10/29/2025

# Description: This is of lab 10
#ask for a list of numbers finds sum mean standard deviation then prints them 
def main():
    nums = read_data()
    #print(nums)
    total = compute_sum(nums)
    #print(total)
    mean = compute_mean(nums)
    #print(mean)
    sd = compute_sd(nums)
    #print(sd)
    display_result(total,mean,sd)

def read_data()-> list:
    """
    Function Name: read_data
    Description: Prompts user for and read in a set of
    numbers, one number at a time.
    Parameter: None
    Returns list of numbers
    """
    stop = " " 
    nums = []
    while stop:
        stop = input("Enter a number (press enter only when done):")
        if stop == "":
            return nums
        nums.append(int(stop))

def compute_sum(nums:list)->int:
    """
    Function Name: cumpute_sum
    Description: the sum of all ints in a list
    Parameter: nums list
    returns sum
    """
    total = 0
    for i in range(len(nums)):
        total += nums[i]
    return total

def compute_mean(nums:list)->float:
    """
    Function Name: compute_mean
    Description: find the mean of a list of ints
    Parameter: list 
    returns mean
    """
    return compute_sum(nums)/len(nums)


def compute_sd(nums:list)->float:
    """
    Function Name: compute_sd
    Description: find the standard deviation
    Parameter: list of numbers
    returns standard deviation
    """
    sums = 0
    mean = compute_mean(nums)
    for num in nums:
        sums = sums + (num - mean)**2
    return (sums / (len(nums)- 1))**0.5

def display_result(s:int,m:float,sd:float)->None:
    """
    Function Name: display_result
    Description: display results 
    Parameter: sum mean and standard deviation 
    returns nothing
    """
    print(f"Sum is: {s:.2f}\nMean is: {m:.2f}\nStandard Deviation is: {sd:.2f}")



if __name__ == "__main__":
    main()