# Problem 1.2
# Locate the smallest window to be sorted
## UNFINISHED

def main(input):
    start = 0
    end = 0
    sortedList = sorted(input)
    for i in range(len(input)):
        if input[i] != sortedList[i]:
            if start == 0:
                start = i
            else:
                end = i
    return(start, end)

def main2(input):
    maxValue = 0
    end = 0
    for i in input:
        if i > maxValue:
            maxValue = i
        if i < maxValue:
            end = 

if __name__ == "__main__":
    #input = [3,7,5,6,9]
    input = [1,2,3,4,100,7,8,9,11,10]
    print(main(input))