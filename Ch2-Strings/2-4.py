# Daily Coding Problems 2.4
# Smallest rotated string

def main(string, rotation):
    candidateStrings = (
        [string[:position] + string[position+1:] + string[position] for position in range(rotation)]
    )

    lexiLeast = None

    for candidateString in candidateStrings:
        if not lexiLeast:
            lexiLeast = candidateString 
        for position in range(len(string)):
            if candidateString[position] < lexiLeast[position]:
                print("{} at position {} is less than {}.  {} will now overtake {} as lexiLeast.\n".format(candidateString[position], position, lexiLeast[position], candidateString, lexiLeast))
                lexiLeast = candidateString
            elif candidateString[position] == lexiLeast[position]:
                print("{} vs {}:\n{} at position {} is equal to {}.  Next char!\n".format(candidateString, lexiLeast, candidateString[position], position, lexiLeast[position]))
                continue
            else:
                print("{} vs {}:\n{} at position {} is greater than {}.  Moving on.\n".format(candidateString, lexiLeast, candidateString[position], position, lexiLeast[position]))
                break

    print(candidateStrings)
    return(lexiLeast)

if __name__ == "__main__":
    string = "aaaaabbbbb"
    rotation = 6
    print(main(string, rotation))