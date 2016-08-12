def checkio(data):
    result = True;
    length = len(data);
    count_digit = False;
    count_upper = False;
    count_lower = False;
    if length < 10:
        result = False;
    for char in data:
        if char.isdigit() == True:
            count_digit = True;
    for char in data:
        if char.isupper() == True:
            count_upper = True;
    for char in data:
        if char.islower() == True:
            count_lower = True;
    if count_upper == False or count_lower == False or count_digit == False:
        result = False;
    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
