""" 
    ============================================================
        By Code Wars  <3
    ============================================================
    Given a 2D ( nested ) list ( array, vector, .. ) of size m * n,
    your task is to find the sum of the minimum values in each row.
    So the function should return 26 because the sum of the minimums is 1 + 5 + 20 = 26.

    [ [ 1, 2, 3, 4, 5 ]        #  minimum value of row is 1
    , [ 5, 6, 7, 8, 9 ]        #  minimum value of row is 5
    , [ 20, 21, 34, 56, 100 ]  #  minimum value of row is 20
    ]

"""

def sum_of_minimums(numbers):
    total = 0
    for i in numbers:
        total += min(i)
    return total