MORSE = {'.-':    'a', '-...':  'b', '-.-.':  'c',
         '-..':   'd', '.':     'e', '..-.':  'f',
         '--.':   'g', '....':  'h', '..':    'i',
         '.---':  'j', '-.-':   'k', '.-..':  'l',
         '--':    'm', '-.':    'n', '---':   'o',
         '.--.':  'p', '--.-':  'q', '.-.':   'r',
         '...':   's', '-':     't', '..-':   'u',
         '...-':  'v', '.--':   'w', '-..-':  'x',
         '-.--':  'y', '--..':  'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9'
        }

def morse_decoder(code):
    result = ""
    words = code.split(" ")
    for elem in words:
        if len(elem) > 0:
            result += MORSE[elem]
        elif len(elem) == 0:
            result += " "
    if result.isdigit():
        result2 = result
    else:
        result2 = upperCapital(result)
    result3 = rearrange(result2)
    return result3
    
def upperCapital(result):
    result2 = ""
    result2 += result[0].upper()
    result2 += result[1:]
    return result2
    
def rearrange(tooManyWhiteSpaces):
    first = tooManyWhiteSpaces.split(' ')
    second = []
    for elem in first:
        if len(elem) > 0:
            second.append(elem)
    third = ' '.join(second)
    return third

if __name__ == '__main__':
    print("Example:")
    print(morse_decoder('... --- ...'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert morse_decoder("... --- -- .   - . -..- -") == "Some text"
    assert morse_decoder("..--- ----- .---- ---..") == "2018"
    assert morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--") == "It was a good day"
    print("Coding complete? Click 'Check' to earn cool rewards!")
