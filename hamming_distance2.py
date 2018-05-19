def checkio(n, m):
    #print (format(n, '022b'))
    #print (format(m, '022b'))
    #print (format(n^m, '022b'))
    result1 = list(format(n^m, '022b'))
    #print (result1)
    count = 0;
    for symbol in result1:
        if symbol == '1':
            count += 1;
    #print(count)
    return count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"
