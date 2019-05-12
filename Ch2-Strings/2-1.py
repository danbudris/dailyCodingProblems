# Find anagram indicies
from collections import Counter
from collections import defaultdict
from timeit import default_timer as timer

def main1(inputstring, anagramstring):
    """
        Given an input string, return the indicies of any 
        potential starting points for an anagram of the anagram string
        Solved this one myself without having to look anything up!
        runs O(s*w) time, where S is the input string, and w is the anagram string
    """

    anagramIndicies = []
    anagramLen = len(anagramstring)
    anagramArray = (list(anagramstring))
    anagramArray.sort()

    for charIndex in range(len(inputstring)):
        substrArray = ((list(inputstring[charIndex:charIndex+anagramLen])))
        substrArray.sort()
        if substrArray == anagramArray:
            anagramIndicies.append(charIndex)

    return(anagramIndicies)

def main2(inputstring, anagramstring):
    def del_if_zero(dict, char):
        if dict[char] == 0:
            del dict[char]

    def anagram_indicies(word, s):
        result = []

        # set up the default dict with a key:pair of char:1 for each char in the word
        freq = defaultdict(int)
        for char in word:
            freq[char] += 1

        print(freq)

        for char in s[:len(word)]:
            freq[char] -= 1
            del_if_zero(freq, char)

        print(freq)

        if not freq:
            result.append(0)

        print(result)

        for i in range(len(word), len(s)):
            start_char, end_char = s[i - len(word)], s[i]
            print(start_char, end_char)
            freq[start_char] += 1
            print(freq)
            del_if_zero(freq, start_char)
            print(freq)

            freq[end_char] -= 1
            del_if_zero(freq, end_char)
            print(freq)

            if not freq:
                beg_index = i - len(word) + 1
                result.append(beg_index)
                print(result)

        return result

    return(anagram_indicies(anagramstring, inputstring))

if __name__ == "__main__":
    inputstring = "abxaba"
    inputstringarry = list(inputstring)
    anagramstring = "ab"

    # as you adjust the size of the input string and anagram string, you can see the time of main1 grow at O(s*x), while main2 grows a O(s)
    start = timer()
    print(main1(inputstring, anagramstring))
    end = timer()
    print(end - start)

    start = timer()
    print(main2(inputstring, anagramstring))
    end = timer()
    print(end - start)
