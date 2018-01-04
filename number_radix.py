'''
this program translates any integer base to decimal.
examples for testing:
    assert checkio("101", 2) == 5, "Binary"
    assert checkio("111112", 3) == 365, "Ternary"
    assert checkio("200", 4) == 32, "Quaternary"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("25", 6) == 17, "Heximal/Senary"  
    assert checkio("112", 8) == 74, "Octal
    assert checkio("AB", 10) == -1, "B > A > 10"
    assert checkio("10000", 12) == 20736, "duodecimal"
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("20", 20) == 40, "Vigesimal"
    assert checkio("D0", 20) == 260, "Vigesimal"
    assert checkio("100", 20) == 400, "Vigesimal"    
    assert checkio("Z", 36) == 35, "Hexatrigesimal"
'''
def checkio(str_number, radix):
    
    myList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"];

    # initialise first digit
    letter = str_number[0].lower();
    faktor = myList.index(letter);
    
    # digit cannot be greater than base
    if faktor >= radix:
        return -1
        
    # only one digit
    if len(str_number) == 1:
        return faktor;

    # only two digits 
    if len(str_number) == 2:
        letter = str_number[0].lower();
        faktor = myList.index(letter);
        if faktor > radix:
            return -1
        result =  faktor * radix;
        letter = str_number[1].lower();
        faktor = myList.index(letter);
        if faktor > radix:
            return -1
        result += faktor;
        return result

    # all other cases
    result = faktor;
    for elem in range(1, len(str_number)):
            letter = str_number[elem].lower();
            faktor = myList.index(letter);
            # check that digit is not greater than base
            if faktor > radix:
                return -1
            result *= radix;
            result += faktor;

    return result;

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A > 10"

