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
    item_count = 0 
    for number in sequence:
        if number == item:
            item_count += 1
    return item_count
