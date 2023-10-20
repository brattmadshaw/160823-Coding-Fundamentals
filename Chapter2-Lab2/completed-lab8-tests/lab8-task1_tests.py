def count(sequence, item):
    sum = 0
    for n in sequence:
        if n == item:
            sum += 1
    return sum

my_list = [1, 2, 3, 4, 1, 1, 5]
count_of_ones = count(my_list, 1)
print(count_of_ones)