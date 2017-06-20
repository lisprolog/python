def safe_pawns(pawns):
    coordinates = getCoord(pawns);
    listCoordinates = coordinates[0];
    listSavePositions = coordinates[1];
    #print(listCoordinates);
    #print(listSavePositions);
    safe = checkCoord(listCoordinates, listSavePositions);
    return safe
    
    # translates the chess coordinates into digits
    # 
def getCoord(pawns):
    testpawns = ["b4", "d4", "f4", "c3", "e3", "g5", "d2"];
    # (a == 0)
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'];
    # (1 == 0)
    num = ['1', '2', '3', '4', '5', '6', '7', '8'];
    #print(alpha.index("a"));
    coordinateList = [];
    saveCandidates = [];
    for elem in pawns:
        #print(elem[0]);
        letter = elem[0];
        pos_letter = alpha.index(letter);
        #print(alpha.index(letter));
        #print(elem[1]);
        digit = elem[1];
        pos_digit = num.index(digit);
        #print(num.index(digit));
        two = [pos_letter, pos_digit];
        coordinateList.append(two);
        twoCand_One = [pos_letter - 1, pos_digit + 1];
        twoCand_Two = [pos_letter + 1, pos_digit + 1];
        if twoCand_One not in saveCandidates:
            saveCandidates.append(twoCand_One);
        if twoCand_Two not in saveCandidates:
            saveCandidates.append(twoCand_Two);
    #saveCandidates2 = set(saveCandidates);
    twoLists = [coordinateList, saveCandidates];
    print (coordinateList);
    print (saveCandidates);
    return twoLists;

    #print(coordinateList);    
    return coordinateList;
    
def checkCoord(coordinates, candidates):
    count = 0;
    for elem in coordinates:
        if elem in candidates:
            count += 1;
    return count;

        
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1

