def left_join(phrases):

    if(len(phrases) < 1 or len(phrases) > 41):
        return "Error"
        
    mytext = ','.join(phrases);

    mytext = mytext.replace("right", "left");

    return mytext

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
