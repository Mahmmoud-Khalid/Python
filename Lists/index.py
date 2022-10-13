""" ============================================================
        By Solo_Learn <3
    ============================================================
    The seats in your ticketing program are stored in a 2D list.
    Each seat is assigned a letter code.

    Complete the program to take the seat row and column as input
    and output the corresponding code from the list
    (row and column indices start from 0).

    Sample Input
    3
    2

    Sample Output
    l

"""

seats = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i'],
    ['j', 'k', 'l']
]

#your code goes here
row = int(input("Enter the row >>> "))
col = int(input("Enter the col >>> "))
print(seats[row][col])
