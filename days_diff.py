from datetime import date

def days_diff(date1, date2):

    days = 0;

    if date2 >= date1:
        d0 = date(date1[0], date1[1], date1[2]);
        d1 = date(date2[0], date2[1], date2[2]);
        delta = d0 - d1;
    if date1 > date2:
        d0 = date(date1[0], date1[1], date1[2]);
        d1 = date(date2[0], date2[1], date2[2]);
        delta = d1 - d0;        
    
    if delta.days < 0:
        days = delta.days * -1;

    return days;

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238

