import random
import time
from tabulate import tabulate
import matplotlib.pyplot as plt
from BST import BST
from prepare import prepare 
from SkipList import Brycen_SkipList
from BucketSort import bucketSort
from radixsort import RadixSort,is_it_sorted
from merges import fast_merge,merge
from TestFuction import timeEfficiency

#this is main
def main():
    #array of 100,10,000 elements per
    array = prepare("rand1000000.txt")
    original_input = [num for sublist in array for num in sublist]

    print("Limited to 5 for space\n")
    
    
    if input("would you like to see Question 1 output: 'y' or 'n' ").lower() == 'y':
        # first 50 for RadixSort so if you change dont do more then 50
        print(f"before RadixSort ->\n{'\n'.join(str(arr[:5]) for arr in array[:5])}")
        print()
        # last 50 for BucketSort if you change dont do less then 50 to start 
        print(f"before BucketSort ->\n{'\n'.join(str(arr[:5]) for arr in array[50:55])}")

        first,last = [],[]
        #take file first 50 elements
        for arr in array[:50]: 
            first.append(RadixSort(arr))
        
        #take file last 50 elements 
        for arr in array[50:]:
            last.append(bucketSort(arr))

        print("-" * 50)
        print(f"After RadixSort ->\n{'\n'.join(str(arr[:5]) for arr in first[:5])}")
        print()
        print(f"After BucketSort ->\n{'\n'.join(str(arr[:5]) for arr in last[:5])}")
        print("-" * 50)

        #new array of sorted arrays 
        array2 = first + last

        #do both merge fast and merge slow and check result is equal on both
        time_fast_merge = timeEfficiency(fast_merge,array2.copy())
        time_merge = timeEfficiency(merge,array2.copy())
        
        #check every value and duplicate count outside the timed section.
        expected = sorted(original_input)
        assert time_fast_merge[1] == expected, "Fast merge lost or changed elements"
        assert time_merge[1] == expected, "Slow merge lost or changed elements"
        print("Both merges preserve every original element, including duplicates.")
        print("-" * 50)

        # i passed back as array so i can index the print staments the way i want
        print()
        print(time_fast_merge[0])
        print("-" * 50)

        print()
        print(time_merge[0])
        print("-" * 50)

        print()
        print(f"DO THEY MATCH-> {time_fast_merge[1] == time_merge[1]}")
        print(f"is fast merge Sorted-> {is_it_sorted(time_fast_merge[1])}\nIs slow merge sorted-> {is_it_sorted(time_merge[1])}")
        print(f"size of Sorted fast merge-> {len(time_fast_merge[1])}\nSize of Sorted slow merge-> {len(time_merge[1])}")
        print(f"Fast Merge is {(time_merge[2] - time_fast_merge[2])/ 1_000_000_000:.2f} seconds Faster then Slow Merge")
        print(f"Speedup (slow / fast): {time_merge[2] / time_fast_merge[2]:.2f}x")
        
                

    # compare skip list and bst searches using the original input order
    if input("would you like to run skiplist vs bst 'y' or 'n' ").lower() == 'y':
        with open("rand1000000.txt","r") as file:
            nums = [int(value) for value in file.read().split()]
        run_search_simulation(nums)

    if input("would you like to run extra Credit 'y' or 'n' ").lower() == 'y':
        extra_credit(False)

        if input("run with 10mil 'y' or 'n' ")=='y':
            extra_credit(True)


def run_search_simulation(nums, query_count=1_000_000, trials=10,
                          seed: int | None = None):
    
    # generate queries once and reuse the same order for every structure and trial
    if not nums or query_count < 1 or trials < 1:
        raise ValueError("input data query count and trial count must be positive")
    
    # choose a fresh seed each run unless one is supplied for repeatable checks
    if seed is None:
        seed = random.SystemRandom().randrange(2**32)
    
    rng = random.Random(seed)
    queries = [rng.randint(0, 1_000_000) for _ in range(query_count)]

    # calculate the correct found count before timing any searches
    present = set(nums)
    expected_found = sum(key in present for key in queries)
    del present
    
    rows = []
    for trial in range(1, trials + 1):
        # build fresh structures outside the timed searches
        skiplist = Brycen_SkipList(len(nums), seed=seed + trial)
        bst = BST()
        print(f"Building trial {trial}/{trials}", flush=True)
        for value in nums:
            skiplist.insert(value)
            bst.insert(value)

        # alternate which structure is searched first to reduce order effects
        structures: list[tuple[str, Brycen_SkipList | BST]] = [
            ("skiplist", skiplist), ("bst", bst)]
        if trial % 2 == 0:
            structures.reverse()
        seconds: dict[str, float] = {}
        counts: dict[str, int] = {}
        for name, structure in structures:
            search = structure.search
            start = time.perf_counter_ns()
            found = sum(search(key) for key in queries)
            elapsed = time.perf_counter_ns() - start
            seconds[name] = elapsed / 1_000_000_000
            counts[name] = found
            assert found == expected_found, f"{name} found count is incorrect"
            del search, structure

        row = {
            "trial": trial, "query_seed": seed, "skiplist_seed": seed + trial,
            "input_count": len(nums), "query_count": query_count,
            "first_searched": structures[0][0], "expected_found": expected_found,
            "skiplist_seconds": seconds["skiplist"], "bst_seconds": seconds["bst"],
            "skiplist_found": counts["skiplist"], "bst_found": counts["bst"],
        }

        rows.append(row)
        # release both structures before building the next trial
        del structures, skiplist, bst

    print_search_results(rows)
    return rows


def print_search_results(rows):
    # show the results and averages with a line between each row
    table = [
        [row["trial"], row["skiplist_seconds"], row["bst_seconds"],
         row["skiplist_found"], row["bst_found"]]
        for row in rows
    ]
    table.append([
        "Average",
        sum(row["skiplist_seconds"] for row in rows) / len(rows),
        sum(row["bst_seconds"] for row in rows) / len(rows),
        sum(row["skiplist_found"] for row in rows) / len(rows),
        sum(row["bst_found"] for row in rows) / len(rows),
    ])
    print(f"\nQueries per trial: {rows[0]['query_count']:,}")
    print(tabulate(
        table,
        headers=["Trial", "Skip list sec", "BST sec", "Skip found", "BST found"],
        tablefmt="rounded_grid",
        floatfmt=("", ".6f", ".6f", ",.0f", ",.0f"),
    ))

def avg(arr):
    return sum(arr) / len(arr)

def extra_credit(run = False):
    #make an array to hold the results
    avg_times = []

    for k in [2,5,10,20,50,100,200,500,750,1000]:
        #0 = sort_time , 1 = merge_time , 2 = total_time
        run_times = [[], [], []]
        
        arrays = []
        if run:
            nums = [random.randint(0,10_000_000) for _ in range(10_000_000)]
            size, extra = divmod(len(nums), k)
            start = 0
            for j in range(k):
                end = start + size + (j < extra)
                arrays.append(nums[start:end])
                start = end
        else:
            arrays = prepare("rand1000000.txt",k)
        
        print(".",end="")
        for i in range(3):

            #get the middle and split 
            mid = len(arrays)//2
            left = arrays[:mid]
            right = arrays[mid:]
            
            # sort the arrays of arrays
            new_left,new_right = [],[]
            sort_time = 0

            for arr in left:
                result= timeEfficiency(RadixSort,arr)
                new_left.append(result[1])
                sort_time += result[2]
                
            for arr in right: 
                result = timeEfficiency(bucketSort,arr)
                new_right.append(result[1])
                sort_time += result[2]
            
            run_times[0].append(sort_time)
            print(".",end="")
            #result of time function after combining the arrays
            result = timeEfficiency(fast_merge,new_left + new_right)
            run_times[1].append(result[2])
            
            run_times[2].append(sort_time + result[2])
            print(".",end="")
        avg_times.append([
            k,
            avg(run_times[0]) / 1_000_000_000,
            avg(run_times[1]) / 1_000_000_000,
            avg(run_times[2]) / 1_000_000_000,
        ])
    
    #print the table 
    print()
    print(tabulate(
        avg_times,
        headers=["k", "Sorting Time (sec)", "Merging Time (sec)",
                 "Total Time (sec)"],
        tablefmt="rounded_grid",
        floatfmt=(".0f", ".6f", ".6f", ".6f"),
    ))
    
    ks = [row[0] for row in avg_times]
    plt.figure(figsize=(10, 6))
    plt.plot(ks, [row[1] for row in avg_times], marker="o", label="Sorting Time")
    plt.plot(ks, [row[2] for row in avg_times], marker="o", label="Merging Time")
    plt.plot(ks, [row[3] for row in avg_times], marker="o", label="Total Time")
    best = min(avg_times, key=lambda row: row[3])
    plt.annotate(f"Minimum total: k = {best[0]}", (best[0], best[3]),
                 xytext=(10, 20), textcoords="offset points",
                 arrowprops={"arrowstyle": "->"})
    plt.xlabel("Number of sublists (k)")
    plt.ylabel("Average execution time (seconds)")
    plt.title("Sorting and merging times averaged over three runs")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()


#this is so main will only run if i run this file
if __name__ == "__main__":
    main()
