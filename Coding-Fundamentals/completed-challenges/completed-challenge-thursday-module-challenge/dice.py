#create 2 files, one called dice.py - write a function that will generate a random number between 1 and 6. In the second file use the dice module to simulate throwing 2 dice and print this value
import random

def dice():
    result = random.randint(1, 6)
    print(result)