'''
In the CheckiO mission Roman Numerals you have to convert a decimal number into its representation as a roman number.
Here you have to do the same but the other way around.

You are given a Roman number as a string and your job is to convert this number into its decimal representation.

A valid Roman number, in the context of this mission, will only contain Roman numerals as per the below table and follow the rules of the subtractive notation.
Check this Wikipedia article out for more details on how to form Roman numerals.
Numeral	Value
I	1 (unus)
V	5 (quinque)
X	10 (decem)
L	50 (quinquaginta)
C	100 (centum)
D	500 (quingenti)
M	1,000 (mille)

Input: A roman number as a string.

Output: The decimal representation of the roman number as an int.

Example:

reverse_roman('VI') == 6

reverse_roman('LXXVI') == 76

reverse_roman('CDXCIX') == 499

reverse_roman('MMMDCCCLXXXVIII') == 3888

1

2

3

4

Precondition:
len(roman_string) > 0
all(char in "MDCLXVI" for char in roman_string) == True
0 < reverse_roman(roman_string) < 4000
'''
def reverse_roman(roman_string):
    thisdict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    substraction = {
        "IV" : -2,   #   6-2   =   4
        "IX" : -2,   #  11-2   =   9
        "XL" : -20,  #  60-20  =  40
        "XC" : -20,  # 100-20  =  90
        "CD" : -200, # 600-200 = 400
        "CM" : -200  #1100-200 = 900
    }
    
    my_list = ["IV", "IX", "XL", "XC", "CD", "CM"]
    my_list2 = ["IV", "IX", "XL", "XC", "CD", "CM"]
    result = 0
    #big_buffer = []

    #print(roman_string)

    for elem in my_list:
        if elem in roman_string:
            if len(roman_string) > len(elem):
                result += substraction[elem]
                my_list2.remove(elem)
            
    for elem in roman_string:       #we add all elements in roman_string into result
        result += thisdict[elem]
        
    return result
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert reverse_roman('VI') == 6, '6'
    assert reverse_roman('LXXVI') == 76, '76'
    assert reverse_roman('CDXCIX') == 499, '499'
    assert reverse_roman('MMMDCCCLXXXVIII') == 3888, '3888'
    assert reverse_roman('MMMCMXCIX') == 3999, '3999'
    assert reverse_roman('MMMCDLXV') == 3465, '3465'
    print('Great! It is time to Check your code!');
