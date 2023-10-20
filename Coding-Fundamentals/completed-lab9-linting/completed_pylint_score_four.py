"""
Add docstring here
"""
def count(sequence, item):
    '''
    Count the number of times 'item' appears in 'sequence'.

    Parameters:
    sequence (iterable): The sequence to search.
    item: The item to count in the sequence.

    Returns:
    int: The count of 'item' in 'sequence'.
    '''
    i = 0 
    for n in sequence:
        if n == item:
            i += 1
    return i
