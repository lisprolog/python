'''
This mission is the first one of the series. Here you should find the length of the longest substring that consists of the same letter. For example, line "aaabbcaaaa" contains four substrings with the same letters "aaa", "bb","c" and "aaaa". The last substring is the longest one, which makes it the answer.

Input: String.

Output: Int.

 Example:

long_repeat('sdsffffse') == 4

long_repeat('ddvvrwwwrggg') == 3

''' 

def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    if(len(line) < 1):
        return 0
    elif(len(line) == 1):
        return 1
        
    counter = 0
    index1 = 0
    index2 = 1

    max_temporary = 0
    max_finally = 0
    run = True
    while(run):
        mark1 = line[index1]
        mark2 = line[index2]
        #print(mark1)
        #print(mark2)
        if(mark1 == mark2):
            counter += 1
            index2 += 1
            if(counter > max_finally):
                max_finally = counter
                print(max_finally)
        else:
            index1 += 1
            index2 = index1 + 1
            counter = 0
        if(index1 == len(line)-1):
            run = False
        elif(index2 == len(line)):
            run = False
        #print("result")
        #print(max_finally)
    return max_finally + 1

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    print('"Run" is good. How is "Check"?')
