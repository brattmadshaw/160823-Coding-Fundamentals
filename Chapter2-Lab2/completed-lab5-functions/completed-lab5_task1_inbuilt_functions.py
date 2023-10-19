#modules
import statistics

#list of data
data="100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"
print(data)

#convert to list of ints
grades = list(map(int, data.split(',')))

#obtain values
smallest = min(grades)
largest = max(grades)

#testing statistics module
mean = statistics.mean(grades)
median = statistics.median(grades)
std_deviation = statistics.stdev(grades)
variance = statistics.variance(grades)
mode = statistics.mode(grades)
median_low = statistics.median_low(grades)
median_high = statistics.median_high(grades)

#print largest/smallest value
print("Min Grade:",smallest)
print("Max Grade:",largest)

#print statistics value of list
print("Mean Grade: :", mean)

rounded_mean = mean = round(statistics.mean(grades), 2)
print("Mean Grade: (Rounded)", rounded_mean)

print("Median Grade:",median)
print(std_deviation)
print(variance)
print(mode)
print(median_low)
print(median_high)