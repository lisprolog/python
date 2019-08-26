'''
 You prefer a good old 12-hour time format. But the modern world we live in would rather use the 24-hour format and you see it everywhere. Your task is to convert the time from the 24-h format into 12-h format by following the next rules:
- the output format should be 'hh:mm a.m.' (for hours before midday) or 'hh:mm p.m.' (for hours after midday)
- if hours is less than 10 - don't write a '0' before it. For example: '9:05 a.m.'
Here you can find some useful information about the 12-hour format.

example

Input: Time in a 24-hour format (as a string).

Output: Time in a 12-hour format (as a string).

Precondition:
'00:00' <= time <= '23:59'
'''
def time_converter(time):
    result = ""
    hours = time[0:2]                           
    minutes = time[3:5]
    meridiem = "a.m."                           
    if (hours == "00" and minutes == "00"):     # converting "00" str() to 0 int() is a problem
        return "12:00 a.m."                     # therefore catch it right here.
    checkValue = int(hours) * 60 + int(minutes);# threshold for 12 hours subtraction
    hours2 = ""
    if int(hours) > 11:                         # change variable to p.m.
        meridiem = "p.m."
    if checkValue > 779:                        # subtract 12 hours
        hours = int(hours) - 12
    if int(hours) < 10:                         # delete leading 0 like (09:00) to (9:00) 
        hours3 = str(hours)
        hours2 = hours3.lstrip("0")
    else:
        hours2 = str(hours)
    result = str(hours2) + ":" + minutes + " " + meridiem # 
    return result

if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    assert time_converter('00:00') == '12:00 a.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
