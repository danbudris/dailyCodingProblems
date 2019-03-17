# Problem 1.2
# Locate the smallest window to be sorted
## UNFINISHED

def main(inputArray):
    """ Done
        Takes an array of integers as input
    """
    start = 0
    end = 0
    sortedList = sorted(inputArray)

    for i in range(len(inputArray)):
        if inputArray[i] != sortedList[i]:
            if start == 0:
                start = i
            else:
                end = i

    return(start, end)


def main2(inputArray):
    """ Not complete
        Takes an array of integers as input
    """
    left = 0
    right = 0

    while left == 0:
        for i in range(len(inputArray)):
            if i+1 != len(inputArray):
                if (inputArray[i] > inputArray[i+1]):
                    left = i

    inputArray.reverse()
    while right == 0:
        for i in range(len(inputArray)):
            if i+1 != len(inputArray):
                if (inputArray[i] < inputArray[i+1]) or i != len(inputArray):
                    right = i

    return(left, right)

def main3(inputArray):
    maxSeen, minSeen = -float("inf"), float("inf")
    for i in range(len(inputArray)):
        if inputArray[i] > maxSeen:
            maxSeen = inputArray[i]
        if inputArray[i] < minSeen:
            minSeen = inputArray[i]

    return(maxSeen, minSeen)

if __name__ == "__main__":
    input = [1,2,3,4,3455,7,3,4,-11,2000,5,1]
    print(main(input))
    print(main2(input))
    print(main3(input))