def checkio(expression):
    print(expression);
    check = " ";
    list_a = [];
    count_one = 0;
    count_two = 0;
    count_three = 0;
    last_elem = 0;
    result = False;
    broken = False;
    for elem in expression:
        print("elem: " +str(elem));
        if elem == "(":
            list_a.append(elem);
            count_one += 1;
        elif elem == "[":
            list_a.append(elem);
            count_two += 1;
        elif elem == "{":
            list_a.append(elem);
            count_three += 1;
        elif elem == ")":
            try:
                check = list_a.pop();
                print("check: "+ str(check));
                if check == "(":
                    count_one -= 1;
                else:
                    return False;
            except IndexError:
                return False;
        elif elem == "]":
            try:
                check = list_a.pop();
                print("check: "+ str(check));
                if check == "[":
                    count_two -= 1;
                else:
                    return False;
            except IndexError:
               return False; 
        elif elem == "}":
            try:
                check = list_a.pop();
                print("check: "+ str(check));
                if check == "{":
                    count_three -= 1;
                else:
                    return False;
            except IndexError:
                return False;
            
    if count_one == 0 and count_two == 0 and count_three == 0 and broken == False:
        result = True;
        
    print("next");
    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
    assert checkio("[(3)+(-1)]*{3}") == True, "Test 6"
    assert checkio("(((([[[{{{3}}}]]]]))))") == False, "Test 7"
    assert checkio("(((1+(1+1))))]") == False, "Test 11"

