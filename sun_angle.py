'''
 Your task is to find the angle of the sun above the horizon knowing the time of the day. Input data: the sun rises in the East at 6:00 AM, which corresponds to the angle of 0 degrees. At 12:00 PM the sun reaches its zenith, which means that the angle equals 90 degrees. 6:00 PM is the time of the sunset so the angle is 180 degrees. If the input will be the time of the night (before 6:00 AM or after 6:00 PM), your function should return - "I don't see the sun!".

example

Input: The time of the day.
Output: The angle of the sun, rounded to 2 decimal places.

Example:

sun_angle("07:00") == 15
sun_angle("12:15"] == 93.75
sun_angle("01:23") == "I don't see the sun!"
How it is used: One day it can save your life, if you'll be lost far away from civilization.
Precondition:
00:00 <= time <= 23:59 
'''

def sun_angle(time):
    # 4 minutes = 1 degree    
    no_sun = "I don't see the sun!"
    hour = int(time[0:2])
    minutes = int (time[3:5])
    if hour < 6 or hour > 18:
        return no_sun
    if hour == 18 and minutes > 0:
        return no_sun
    #print(hour)
    #print(minutes)
    # start at 6:00: subtract 6
    # convert the hours into minutes : multiply with 60
    # add the minutes
    # to convert into degrees: 1 degree are 4 minutes: divide by 4
    result = ((hour - 6)* 60 + minutes) / 4
    result2 = round(result,2)
    #print(result2)
    return result2

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing

    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    assert sun_angle("12:15") == 93.75
    print("Coding complete? Click 'Check' to earn cool rewards!")

