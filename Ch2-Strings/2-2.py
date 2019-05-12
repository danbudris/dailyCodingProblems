from timeit import default_timer as timer

def reverse(string):
    string = string[::-1]
    return string

def main(arr):
    # Runs in O(n2 * c) time, where c is the length of the longest word
    # my solution, w/out viewing book solution
    result = []
    for word in range(len(arr)):
        for secondWord in range(len(arr)):
            if secondWord != word:
                palindrome = arr[word] + arr[secondWord]
                print(palindrome)
                if palindrome == reverse(palindrome):
                    result.append((word, secondWord))
    return(result)


def is_palindrome(word):
    return word == word[::-1]

def main2(words):
    #optimized book soltuion, runs in O(n*c) time
    d = {}
    for i, word in enumerate(words):
        d[word] = i

    result = []

    for i, word in enumerate(words):
        for char_i in range(len(word)):
            prefix, suffix = word[:char_i], word[char_i:]
            reversed_prefix = prefix[::-1]
            reversed_suffix = suffix[::-1]

            if (is_palindrome(suffix) and
                    reversed_prefix in d):
                if i != d[reversed_prefix]:
                    result.append((i, d[reversed_prefix]))
            
            if (is_palindrome(prefix) and
                    reversed_suffix in d):
                if i != d[reversed_suffix]:
                    result.append((i, d[reversed_suffix]))

    return(result)
                
if __name__ == "__main__":
    arr = ["code","edoc","da","d","racecar","asdfa","afdsafads","b","c","asdf","fdsa"]
    start = timer()
    print(main(arr))
    end = timer()
    print(end - start)

    # This one is significantly faster! Obviously...
    start = timer()
    print(main2(arr))
    end = timer()
    print(end - start)