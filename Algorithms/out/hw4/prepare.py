
# n is the number of elements per array
# k is the number of arrays
def perpare(file_Name:str): # returns array
    with open(file_Name,"r") as file:
        # make array with all elements
        nums = file.read().split()
    
    # number of elements for n
    total_n = len(nums)

#all of my files will have a main for testing that file 
def main():
    pass

if __name__ == "__main__":
    main()
