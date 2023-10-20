"""
Add docstring here
"""
def count(sequence, item):
    '''
    Add docstring for function/methods
    Parameters
    ----------
        sequence: str
            the sequence
        item:
            the item
    '''
    y = 0 
    for n in sequence:
        if n == item:
            y += 1
    return y

# C0303: Trailing whitespace (trailing-whitespace)
# C0304: Final newline missing (missing-final-newline)
#-----------------------------------
#Your code has been rated at 6.67/10