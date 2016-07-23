def checkio(first, second):
    first_words = first.split(",");
    second_words = second.split(",");
    first_set = set(first_words);
    second_set = set(second_words);
    intersec = ",".join(sorted(second_set.intersection(first_set)));
    return intersec

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"

