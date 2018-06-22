'''
Vowels -- A E I O U Y
Consonants -- B C D F G H J K L M N P Q R S T V W X Z

You are given a block of text with different words. These words are separated by white-spaces and punctuation marks. Numbers are not considered words in this mission (a mix of letters and digits is not a word either). You should count the number of words (striped words) where the vowels with consonants are alternating, that is; words that you count cannot have two consecutive vowels or consonants. The words consisting of a single letter are not striped -- do not count those. Casing is not significant for this mission.

Input: A text as a string (unicode)

Output: A quantity of striped words as an integer.

Precondition:The text contains only ASCII symbols.
0 < len(text) < 105 
'''
VOWELS = "AEIOUY0123456789"

CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):

    text = text.upper()

    newWord = []

    for letter in text:

        #print(letter)

        if letter in VOWELS:

            newWord.append(0)

        elif letter in CONSONANTS:

            newWord.append(1)

        else:

            newWord.append(' ')

    #print(newWord)

    newWord2 = ''

    for elem in newWord:

        #print(elem)

        newWord2 += str(elem)

    #print(newWord2)

    word_list1 = newWord2.split(' ')

    #print(word_list1)

    word_list2 = []

    for elem in word_list1:

        if len(elem) > 1:

            word_list2.append(elem)

    #print(word_list2)

    result = 0

    for word in word_list2:

        if count(word):

            result += 1

            #print(result)

    #result = count(newWord)

    return result 

def count(binaryStream):

    previous = None

    for elem in binaryStream:

        #initialisation of previous

        if previous is None:

            previous = elem

            #print('Start:INIT of Previous')

            #print(previous)

        else:

            #check valid

            if previous == '1' and elem == '0':

                previous = elem

                #print('10')

            elif previous == '0' and elem == '1':

                previous = elem

                #print('01')

            #check invalid

            elif previous == '1' and elem == '1':

                previous = elem

                #print('11False')                

                return False

            elif previous == '0' and elem == '0':

                previous = elem

                #print('00False')

                return False

            #print('Good')

    return True

        


#These "asserts" using only for self-checking and not necessary for auto-testing

if __name__ == '__main__':

    assert checkio("My name is ...") == 3, "All words are striped"

    assert checkio("Hello world") == 0, "No one"

    assert checkio("A quantity of striped words.") == 1, "Only of"

    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"


