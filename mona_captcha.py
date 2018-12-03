'''
Your program should read the number shown in an image encoded as a binary matrix. 
Each digit can contain a wrong pixel, but no more than one for each digit. 
The space between digits is equal to one pixel 
(just think about "1" which is narrower than other letters, but has a width of 3 pixels).

Captcha

Input: An image as a list of lists with 1 or 0.

Output: The number as an integer.

Example:

recognize([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
     [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
     [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
     [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
     [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]) == 394
recognize([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0],
     [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
     [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
     [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
     [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]) == 394

Precondition:

matrix_rows = 5

5 ≤ matrix_columns < 30

digit_width = 3

digits_space = 1

Each digit contains no more than one wrong pixel.

'''

FONT = ("--X--XXX-XXX-X-X-XXX--XX-XXX-XXX--XX-XX--"
        "-XX----X---X-X-X-X---X-----X-X-X-X-X-X-X-"
        "--X---XX--X--XXX-XX--XXX--X--XXX-XXX-X-X-"
        "--X--X-----X---X---X-X-X-X---X-X---X-X-X-"
        "--X--XXX-XXX---X-XX---XX-X---XXX-XX---XX-")

def recognize(image):
    one =   [0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0];
    two =   [0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1];
    three = [0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1];
    four =  [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1];
    five =  [0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0];
    six =   [0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1];
    seven = [0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0];
    eight = [0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1];
    nine =  [0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0];
    zero =  [0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1];
    digits = [zero, one, two, three, four, five, six, seven, eight, nine];
    lists = [];
    listb = [];
    x = 0;
    # digits are coded in one image
    # first we extract the first 4 pixels per line (5 times)
    # to get each digit of our number
    while x <= len(image[0])-5:
        for elem in image:
            lista = [];
            lista.append(elem[x]); 
            lista.append(elem[x+1]); 
            lista.append(elem[x+2]); 
            lista.append(elem[x+3]);
            lists.append(lista);
            del lista;
        x += 4;
    # in lists i put each digit represented as:
    # (5 times 4 pixels) per digit
    y = 0;
    listd = [];
    liste = [];
    while y <= len(lists)-5:
        listc = [];
        listc.append(lists[y]);
        listc.append(lists[y+1]);
        listc.append(lists[y+2]);
        listc.append(lists[y+3]);
        listc.append(lists[y+4]);
        listd.append(sum(listc, []));
        y += 5;
        liste = [];
        del listc;
    first_result = [];
    # listd has each digit coded in a list as 20 times 0/1
    for element1 in listd:
        for element2 in digits:
            if compare(element1, element2) == True:
                first_result.append(digits.index(element2));
    endResult = intsToNumber(first_result);
    return endResult;
    
def compare(word, word2):
    result = [];
    for e in range(len(word)):
        result.append(word[e] ^ word2[e]);
    if sum(result) < 2:
        return True
    return False;
    
def intsToNumber(numList):  
    s = map(str, numList)  
    s = ''.join(s)          
    s = int(s)
    return s

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert recognize([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
                      [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                      [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                      [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                      [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]) == 394, "394 clear"
    assert recognize([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0],
                      [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                      [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                      [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
                      [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]) == 394, "again 394 but with noise"

    print("Earn cool rewards by using the 'Check' button!")

