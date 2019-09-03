'''
 Positive integers can be expressed as sums of consecutive positive integers in various ways. For example, 42 can be expressed as such a sum in four different ways:(a) 3+4+5+6+7+8+9, (b) 9+10+11+12, (c) 13+14+15 and (d) 42. As the last solution (d) shows, any positive integer can always be trivially expressed as a singleton sum that consists of that integer alone.

Compute how many different ways it can be expressed as a sum of consecutive positive integers.

Input: Int.

Output: Int.

Precondition: Input is always a positive integer.

The mission was taken from Python CCPS 109 Fall 2018. It’s being taught for Ryerson Chang School of Continuing Education by Ilkka Kokkarinen
'''
def count_consecutive_summers(num):
    count = 0
    for x in range (1, num):                # loop the numbers
        if(induction(x, num, 0)) == 1:      # if induction successfull
            count += 1                      # increase counter
    return count + 1    # adding trivial solution 

def induction(x, num, result):
    result += x

    if(x < 1):
        return 0;       # case: counter wrong and negative  fail
    elif(x > num):
        return 0;       # case: counter overflow            fail
    elif(result > num):
        return 0;       # case: result done                 fail
    elif(result == num):
        return 1;       # case: result successfull          success
    return induction(x + 1, num, result);       # end recursion, 1 or 0. success or fail
    
if __name__ == '__main__':
    print("Example:")
    print(count_consecutive_summers(42))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_consecutive_summers(42) == 4
    assert count_consecutive_summers(99) == 6
    assert count_consecutive_summers(1) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")
