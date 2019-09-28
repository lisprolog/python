'''
 You are given a string and two markers (the initial and final). You have to find a substring enclosed between these two markers. But there are a few important conditions:

    The initial and final markers are always different.
    If there is no initial marker, then the first character should be considered the beginning of a string.
    If there is no final marker, then the last character should be considered the ending of a string.
    If the initial and final markers are missing then simply return the whole string.
    If the final marker comes before the initial marker, then return an empty string.

Input: Three arguments. All of them are strings. The second and third arguments are the initial and final markers.

Output: A string. 
'''

import re

def between_markers(text: str, begin: str, end: str) -> str:

    # one symbol

    if len(begin) == 1 and len(end) == 1:

        first = text.find(begin)

        last = text.find(end)

        return text[first+1:last]

  

    if text.find(begin) > -1 and text.find(end) > -1:

        x = re.split(begin, text)

        y = re.split(end, x[1])

        result = y[0]

    elif text.find(begin) < 0 and text.find(end) > -1:

        x = re.split(end, text)

        my_buffer = x[0]

        result = my_buffer[:-1]

    elif text.find(end) < 0 and text.find(begin) > -1:

        x = re.split(begin, text)

        my_buffer = x[1]

        result = my_buffer[1:]

    elif text.find(begin) < 0 and text.find(end) < 0:

        result = text

    else:

        print("ERROR")

    return result


if __name__ == '__main__':

    print('Example:')

    print(between_markers('What is >apple<', '>', '<'))


    # These "asserts" are used for self-checking and not for testing

    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"

    assert between_markers("<head><title>My new site</title></head>",

                           "<title>", "</title>") == "My new site", "HTML"

    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'

    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'

    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'

    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'

    print('Wow, you are doing pretty good. Time to check it!')

