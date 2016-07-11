# Count inversions in a sequence of numbers
def count_inversion(sequence):
    if (len(sequence) < 1 or len(sequence) > 199):
        return "Error1"
    for element in sequence:
        if (element < -99 or element > 199):
            return "Error2"
            
    sequencel = list(sequence);    

    count = 0;
    fake = 0;

    for i in reversed(range(len(sequencel))):
        for j in reversed(range(len(sequencel))):
            if j > i:
                fake += 1;
            elif sequence[j] > sequence[i]:
                count += 1;    
    return count;

    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3, "Example"
    assert count_inversion((0, 1, 2, 3)) == 0, "Sorted"
    assert count_inversion((99, -99)) == 1, "Two numbers"
    assert count_inversion((5, 3, 2, 1, 0)) == 10, "Reversed"
