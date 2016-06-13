"""
 You are given an array of integers. You should find the sum of the elements with even indexes (0th, 2nd, 4th...) then multiply this summed number and the final element of the array together. Don't forget that the first element has an index of 0.

For an empty array, the result will always be 0 (zero).

Input: A list of integers.

Output: The number as an integer.

Example:

checkio([0, 1, 2, 3, 4, 5]) == 30

checkio([1, 3, 5]) == 30

checkio([6]) == 36

checkio([]) == 0
"""

def checkio(array):
    if len(array) == 0:
        return 0
    else:
        a = array[::2];
        print(a);
        b = sum(a);
        print(b);
        print(array[-1]);
        c = b * array[-1];
        return c
    """
        sums even-indexes elements and multiply at the last
    """
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
