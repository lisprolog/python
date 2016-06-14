"""
count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3

count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2

count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",

            {"sum", "hamlet", "infinity", "anything"}) == 1
"""

def count_words(text, words):
    count = 0;
    
    if not words:
        return 0
    if not text:
        return 0
        
    for word in words:
        print(word);
        if word.lower() in text.lower():
            print(word);
            count += 1;
        
    return count


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
