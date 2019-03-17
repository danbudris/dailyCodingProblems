import bisect

arr = [3, 4, 9, 6, 1]

def main(arr):
    newArr = []
    for i in range(len(arr)):
        x = 0
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                x += 1
        newArr.append(x)
    return(newArr)

def main1(arr):
    # using Bisect
    """
    reverses the list, so we start witht he right most number and go backwards from there
    we start with an empty 'result' and 'seen' list
    starting with the rightmost value, we check where we would insert it into the 'seen' list; this is the fist value, so it's empty, so it goes in at 0
    then we go to the next value -- we use bisect.bisect_left to check where we would insert it, and that index tells us how many 'seen' values are less than it.  We add that index to the result, and so on
    at the end, after we've iterated through all of the values, and inserted them into seen and result, we re-reverse the result list, so that it shows up in the original order
    https://docs.python.org/2/library/bisect.html
    """
    result = []
    seen = []
    for num in reversed(arr):
        i = bisect.bisect_left(seen, num)
        result.append(i)
        bisect.insort(seen, num)
    return list(reversed(result))

if __name__ == "__main__":
    print(main(arr))
    print(main1(arr))