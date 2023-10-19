#Morning challenge, rewire this code without using if statements
#(or max or any inbuilt functions)
#
#num = 10
#num_1 = 20 
#
#if num > num_1:
#    print(num)
#
#else:
#    print(num_1)

#my method, pretty much same as if statement above
num = 30
num_2 = 20

while num > num_2:
    print(num)
    break
else:
    print(num_2)

### RESEARCH ONLY, LOOKING AT OTHER METHODS
# using boolean value
#num = 10
#num_1 = 20
#
#result = ((num > num_1) * num) + ((num <= num_1) * num_1)
#print(result)

## using a tuple and boolean value
#num = 10
#num_1 = 20
#
#result = (num_1, num)[num > num_1]
#print(result)