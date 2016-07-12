def checkio(words_set):
    if len(words_set) < 2 or len(words_set) > 30:
        return False

    words_set2 = list(words_set);

    for word in words_set2:
        for word2 in words_set2:
            if word.endswith(word2) and word is not word2:
                return True
    
    return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio({"hello", "lo", "he"}) == True, "helLO"
    assert checkio({"hello", "la", "hellow", "cow"}) == False, "hellow la cow"
    assert checkio({"walk", "duckwalk"}) == True, "duck to walk"
    assert checkio({"one"}) == False, "Only One"
    assert checkio({"helicopter", "li", "he"}) == False, "Only end"

