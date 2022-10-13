""" 
    ============================================================
        By Code Wars  <3
    ============================================================
    You will be given a number and you will need to return it as a string

    expanded_form(12) # Should return '10 + 2'
    expanded_form(42) # Should return '40 + 2'
    expanded_form(70304) # Should return '70000 + 300 + 4'

"""

def expanded_form(num):
    result = []
    
    for index, digit in enumerate(str(num)[::-1]):
        if int(digit) != 0:
            result.append(digit + ('0' * index))

    return ' + '.join(result[::-1])