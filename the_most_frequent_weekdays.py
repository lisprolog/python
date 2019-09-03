'''

 What’s your favourite day of the week? Check if it's the most common day of the week in a year.


You are given a year as an integer (e. g. 2001). You should return the most frequent day(s) of the week in that particular year. The result has to be a list of days sorted by the order of days in a week (e. g. ['Monday', 'Tuesday']). Week starts with Monday.


Input: Year as an int.


Output: The list of most common days sorted by the order of days in a week (from Monday to Sunday).


Preconditions: Year is between 1 and 9999. Week starts with Monday. 

'''

#calendar.weekday(year,month,day) 

#Returns the day of the week (0 is Monday) for year (1970–…), month (1–12), day (1–31).

    

import calendar

def most_frequent_days(year):

    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    daysList = []

    first = calendar.weekday(year, 1, 1);       # get first day of year

    last = calendar.weekday(year, 12, 31);      # get last day of year

    for x in range(first, 7):                   # add days of first week

        daysList.append(x);             

    for y in range(last, -1, -1):               # add days of last week

        daysList.append(y);

    weekdays = []

    for z in range (0,7):                       # count most frequent day of week

        if (daysList.count(z) == 2):            # if both beginning of year and end of year:

            weekdays.append(week[z]);           # 

    if len(weekdays) == 0:                      # if edgecase: first:Sunday, last:Monday

        for z in range (0,7):

            if (daysList.count(z) == 1):        # check only for one appearence

                weekdays.append(week[z]);

    print(weekdays)

    return weekdays


if __name__ == '__main__':

    # These "asserts" using only for self-checking and not necessary for auto-testing

    assert most_frequent_days(2399) ==  ['Friday'], "1st example"

    assert most_frequent_days(1152) == ['Tuesday', 'Wednesday'], "2nd example"

    assert most_frequent_days(56) == ['Saturday', 'Sunday'], "3rd example"

    assert most_frequent_days(2909) == ['Tuesday'], "4th example"

    assert most_frequent_days(328) == ['Monday', 'Sunday'], "Test 14"

