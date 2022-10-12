"""
    # All Rights to SoloLearn <3
    Now that we know how to combine multiple conditions,
    let's improve our gold purity checker program
    and output the corresponding purity level in Karats!

    Here is the purity chart we'll be using:
    24K - 99.9%
    22K - 91.7%
    20K - 83.3%
    18K - 75.0%

    If the percentage is between 75 and 83.3, the gold is considered to be 18K.
    If it's between 83.3 and 91.7 - then it's 20K, and so on.

    Given the percentage as input, output the corresponding Karat value, including the letter K.

    Sample Input:
    92.4

    Sample Output:
    22K

"""
purity = float(input())

if purity >= 99.9:
    print("24K")
elif purity >= 91.7:
    print("22K")
elif purity >=83.3:
    print("20K")
elif purity >=75.0:
    print("18K")
