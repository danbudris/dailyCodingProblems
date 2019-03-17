## Problem 1.1
## Pg. 20
## Problem: given an array, return a new array where each value is the product of all other elements in the array excluding the element at the current index in the array

def multiplyArray(input):
    x = 1
    for i in input:
        x = i*x
    return(x)

# Solution 1: with division
def main(input):
    x = multiplyArray(input)
    output = [x/i for i in input]
    return(output)

# Solution 2: without division
def main2(input):
    output = []
    for i in range(len(input)):
        output.append((multiplyArray(input[:i]) * multiplyArray(input[i+1:])))
    return(output)

if __name__ == "__main__":
    input = [1,2,3,4,5]
    print("Expected Output: " + str([120,60,40,30,24]))
    print("With Division: " + str(main(input)))
    print("Without Division: " + str(main2(input)))