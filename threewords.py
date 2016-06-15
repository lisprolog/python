# checking if text includes 3 words in a row

def checkio(words):
    count = 0;
    result = False;
    lines = words.split(' ')
    for w in lines:
        print(count);
        if (count == 3):
            result = True;
        elif (w.isdecimal()):
            count = 0;
        else:
            count += 1;
      
    if(count >= 3):  
        return True;
    else:
        return False;

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"

