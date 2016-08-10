def checkio(game_result):
    countx0 = 0;
    countx1 = 0;
    countx2 = 0;
    counto0 = 0;
    counto1 = 0;
    counto2 = 0;
              
    # check vertical lines
    for elem in game_result:
        if elem[0] == "X":
            countx0 += 1;
        if elem[1] == "X":
            countx1 += 1;
        if elem[2] == "X":
            countx2 += 1;
        if elem[0] == "O":
            counto0 += 1;
        if elem[1] == "O":
            counto1 += 1;
        if elem[2] == "O":
            counto2 += 1;
            
    if countx0 == 3 or countx1 == 3 or countx2 == 3:
        return "X"
    if counto0 == 3 or counto1 == 3 or counto2 == 3:
        return "O"

    
    lista = [];
    for elem in game_result:
        for item in elem:
            lista.append(item);
            
    # check horizontal lines    
    if lista[0] == "X" and lista[1] == "X" and lista[2] == "X":
        return "X"
    if lista[3] == "X" and lista[4] == "X" and lista[5] == "X":
        return "X"
    if lista[6] == "X" and lista[7] == "X" and lista[8] == "X":
        return "X"
    if lista[0] == "O" and lista[1] == "O" and lista[2] == "O":
        return "O"
    if lista[3] == "O" and lista[4] == "O" and lista[5] == "O":
        return "O"
    if lista[6] == "O" and lista[7] == "O" and lista[8] == "O":
        return "O"
        
    # check diagonal lines            
    if lista[2] == "X" and lista[4] == "X" and lista[6] == "X":
        return "X"
    if lista[0] == "X" and lista[4] == "X" and lista[8] == "X":
        return "X"
    if lista[2] == "O" and lista[4] == "O" and lista[6] == "O":
        return "O"
    if lista[0] == "O" and lista[4] == "O" and lista[8] == "O":
        return "O"
        
    return "D"

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"


