'''
Write a module that enables the robots to easily recall their passwords through codes when they return home.

The cipher grille and the ciphered password are represented as an array (tuple) of strings.

Input: A cipher grille and a ciphered password as a tuples of strings.

Output: The password as a string.
'''

def recall_password(cipher_grille, ciphered_password):
    result = [];
    stepOne = basic_step(cipher_grille, ciphered_password);
    result.append(stepOne);
    cipher_grille = rotate_clockwise(cipher_grille, degree=90);
    cipher_grille = list(cipher_grille);
    stepOne = basic_step(cipher_grille, ciphered_password);
    result.append(list(stepOne));
    #print(result);
    stepTwo = basic_step(cipher_grille, ciphered_password);
    #result.append(stepTwo);
    cipher_grille = rotate_clockwise(cipher_grille, degree=90);
    cipher_grille = list(cipher_grille);
    stepThree = basic_step(cipher_grille, ciphered_password);
    result.append(list(stepThree));
    #print(result);
    stepFour = basic_step(cipher_grille, ciphered_password);
    #result.append(stepFour);
    cipher_grille = rotate_clockwise(cipher_grille, degree=90);
    cipher_grille = list(cipher_grille);
    stepFive = basic_step(cipher_grille, ciphered_password);
    result.append(list(stepFive));
    print(''.join(flatten(result)));
    return ''.join(flatten(result));
    
def basic_step(cipher_grille, ciphered_password):
    counter = 0;
    list_X = [];
    list_I = [];
    list_P = [];
    cipher_grille = flatten(cipher_grille);
    for elem in cipher_grille:
        if elem == 'X':
            list_I.append(counter);
        counter += 1;
    #print(list_I);
    ciphered_password = flatten(ciphered_password);
    counter = 0;
    for e in ciphered_password:
        if counter in list_I:
            list_P.append(ciphered_password[counter]);
        counter += 1;
    #print(list_P);
    return list_P;
            
def flatten(listi):
    listb = [];
    for e in listi:
        for f in e:
            listb.append(f);
    return listb;
    
def rotate_clockwise(matrix, degree=90):
    if degree not in [0, 90, 180, 270, 360]:
        print("Problem with degree");
    return matrix if not degree else rotate_clockwise(zip(*matrix[::-1]), degree-90)
            
        
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'

