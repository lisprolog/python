# multiply digits of number

def checkio(number):
    if (number < 1 or number > 10**6 ): 
        return "Error"
        
    text = str(number);

    text = text.split('0');

    text = ''.join(text);

    result = 1;
    for ch in text:
        result *= int(ch);

    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
