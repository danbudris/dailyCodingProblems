#Calculate maximum subarray sum
arr = [34, -50, 42, 14, -5, 86]
arr = [-5,-1,-8,-9]

def main1(arr):
    current_max = 0
    for i in range(len(arr) - 1):
        for j in range(i, len(arr)):
            current_max = max(current_max, sum(arr[i:j]))
    return current_max

def main2(arr):
    # solve using Kadane's algorithm
    # keeps a running tab of the largest contiguous sum of values seen so far
    max_ending_here = max_so_far = 0
    for x in arr:
        print("Current:\nMaxSofar: " + str(max_so_far) + "\nMaxEndingHere: " + str(max_ending_here) + "\n")
        print("x: " + str(x))
        max_ending_here = max(x, max_ending_here + x)
        print("max ending: " + str(max_ending_here))
        max_so_far = max(max_so_far, max_ending_here)
        print("max so far: " + str(max_so_far))
        print("\n")
    return max_so_far

def main3(arr):
    

if __name__ == "__main__":
    print(main2(arr))
    print(sum(arr))