import csv
import sys


def main():

    if len(sys.argv) != 3:
        print("missing")
        sys.exit()

    # Read database file into a variable
    row_str = []
    with open(sys.argv[1])as file:  # open a file and name it file
        Str = csv.DictReader(file)  # make the csv file into a dict list
        for row in Str:
            row_str.append(row)

    # Read DNA sequence file into a variable
    # this means open the csv and read the line i did read only becuase it only 1 line
    with open(sys.argv[2], "r")as sequence:
        dna = sequence.read().strip()  # strip removes white space

    # Find longest match of each STR in DNA sequence
    my_dict = {}
    for key in row_str[0]:
        if key != "name":
            my_dict[key] = longest_match(dna, key)

    # Check database for matching profiles
    strs = [key for key in row_str[0] if key != "name"]
    my_counts = [my_dict[str_] for str_ in strs]
    for row in row_str:
        row_counts = [int(row[str_])for str_ in strs]
        if row_counts == my_counts:
            print(row["name"])
            sys.exit()
    print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
