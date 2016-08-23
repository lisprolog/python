'''
Count Ingots

To create an accurate accounting of our stock, incoming ingots in cargo shipments are numbered.

Ingots in each consignment are numbered in the row from A1 to Z9 as A1, A2,..., A9, B1, B2, ..., Z9. Each consignment is marked with the number of the last ingot in it. So you can define the quantity of ingots by the number of marks.

You are given a report of daily consignments as number marks written in a string separated by commas. Count the total quantity of ingots. Take the report "A2,B1" for example. Here we can see two consignments with 2 (A2) and 10 (B1) ingots, giving us a result of 12.

Input: A daily report as a string.

Output: The total quantity of ingots as an integer.

Example:

count_ingots("A2,B1") == 12
count_ingots("A1,A1,A1") == 3
count_ingots("Z9,X8,Y7") == 672
count_ingots("C1,D1,B1,E1,F1") == 140

Precondition:

report match with regexp expression "[A-Z][1-9](,[A-Z][1-9])*"

How it is used:

This concept uses a modified numeral system and provides you with a basis for working with strings.
'''
def count_ingots(report):
    alist = report.split(",");
    print(alist);
    alpha = ["0", "A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E9", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9", "H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "I1", "I2", "I3", "I4", "I5", "I6", "I7", "I8", "I9", "J1", "J2", "J3", "J4", "J5", "J6", "J7", "J8", "J9", "K1", "K2", "K3", "K4", "K5", "K6", "K7", "K8", "K9", "L1", "L2", "L3", "L4", "L5", "L6", "L7", "L8", "L9", "M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8", "M9", "N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8", "N9", "O1", "O2", "O3", "O4", "O5", "O6", "O7", "O8", "O9", "P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", "P9", "Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8", "Q9", "R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8", "T9", "U1", "U2", "U3", "U4", "U5", "U6", "U7", "U8", "U9", "V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8", "V9", "W1", "W2", "W3", "W4", "W5", "W6", "W7", "W8", "W9", "X1", "X2", "X3", "X4", "X5", "X6", "X7", "X8", "X9", "Y1", "Y2", "Y3", "Y4", "Y5", "Y6", "Y7", "Y8", "Y9", "Z1", "Z2", "Z3", "Z4", "Z5", "Z6", "Z7", "Z8", "Z9"];
    sum = 0;
    for elem in alist:
        elem_converted = alpha.index(elem);
        print(str(elem) + " " + str(elem_converted));
        sum += elem_converted;
        print(sum);
    return sum

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_ingots("A2,B1") == 12, "Two and ten"
    assert count_ingots("A1,A1,A1") == 3, "One, two, three"
    assert count_ingots("Z9,X8,Y7") == 672, "XYZ"
    assert count_ingots("C1,D1,B1,E1,F1") == 140, "Daily normal"
