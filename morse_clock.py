'''
Morse clock
You will create a module for converting a normal time string to a morse time string. As you can see in the illustration, a gray circle means on, while a white circle means off. Every digit in the time string contains a different number of slots. The first digit for the hours has a length of 2 while the second digit for the hour has a length of 4. The first digits for the minutes and seconds have a length of 3 while the second digits for the minutes and seconds have a length of 4. Every digit in the time is converted to binary representation. You will convert every "on" (or 1) signal to dash ("-") and every "off" (or 0) signal to dot (".").

A time string can be in any of the following formats: "hh:mm:ss", "h:m:s" or "hh:m:ss". The "missing" digits are zeroes. For example, "1:2:3" is the same as "01:02:03".

The result will be a morse time string with specific format:

h h : m m : s s

where each digits is represented as sequence of "." and "-" (dots and dashes). Morse clock

Input: A normal time string as a string.

Output: The morse time string as a string.

Example:

morse_time("10:37:49") == ".- .... : .-- .--- : -.. -..-"
morse_time("21:34:56") == "-. ...- : .-- .-.. : -.- .--."
morse_time("00:1:02") == ".. .... : ... ...- : ... ..-."
morse_time("23:59:59") == "-. ..-- : -.- -..- : -.- -..-"

Precondition:

time string contains correct time.

'''
def morse_time(time_string):
    next_list = [];
    next_list = time_string.split(":");
    # get the numbers
    next_list_digit_complete = [];
    print("next_list:" + str(next_list));
    # make 01 out of 1
    for x in next_list:
        if len(str(x)) < 2:
            next_list_digit_complete.append("0" + str(x));
        else:
            next_list_digit_complete.append(str(x));
    first = next_list_digit_complete[0];
    firsta = first[0];
    if int(firsta) == 0:
        firsta_converted = "00";
    elif int(firsta) == 1:
        firsta_converted = "01";
    elif int(firsta) == 2:
        firsta_converted = "10";
    
    firstb = first[1];
    firstb_4 = str(binary(int(firstb)));
    if(len(str(binary(int(firstb))))) < 4:
        firstb_4s = firstb_4.rjust(4, '0');
        firstb_4 = firstb_4s;
    second = next_list_digit_complete[1];
    seconda = second[0];
    seconda_3 = str(binary(int(seconda)));
    if(len(str(binary(int(seconda))))) < 3:
        seconda_3s = seconda_3.rjust(3, '0');
        seconda_3 = seconda_3s;
    secondb = second[1];
    secondb_4 = str(binary(int(secondb)));
    if(len(str(binary(int(secondb))))) < 4:
        secondb_4s = secondb_4.rjust(4, '0');
        secondb_4 = secondb_4s;
    third = next_list_digit_complete[2];
    thirda = third[0];
    thirda_3 = str(binary(int(thirda)));
    if(len(str(binary(int(thirda))))) < 3:
        thirda_3s = thirda_3.rjust(3, '0');
        thirda_3 = thirda_3s;
    thirdb = third[1];
    thirdb_4 = str(binary(int(thirdb)));
    if(len(str(binary(int(thirdb))))) < 4:
        thirdb_4s = thirdb_4.rjust(4, '0');
        thirdb_4 = thirdb_4s;
    new_string = firsta_converted + " " + firstb_4 + " : " + seconda_3 + " " + secondb_4 + " : " + thirda_3 + " " + thirdb_4;
    new_string2 = new_string.replace("0", ".");
    new_string3 = new_string2.replace("1", "-");
        
    return new_string3;

def binary(n):
    newInt2 = int(n)
    binStr = ""
    while newInt2 > 0:
	    binStr = str(newInt2 %2) + binStr
	    newInt2 = newInt2 // 2
    return binStr

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert morse_time("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert morse_time("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert morse_time("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert morse_time("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

