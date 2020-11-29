""" day 1"""
from math import floor

#read the text file
with open("inputs/day1.txt", 'r') as inputfile:
    numbers = inputfile.readlines()
numbers = [x.strip() for x in numbers]

total = 0

#for each number in the file
for number in numbers:
    #divide by 3
    number_divided_by_three = int(number) / 3
    #round down to nearest whole number
    number_rounded_down = floor(number_divided_by_three)
    #subtract 2
    number_subtracted_by_two = number_rounded_down - 2
    #add it to the total
    total = total + number_subtracted_by_two
    #print("Fuel required for module of mass {} is {}", number, number_subtracted_by_two)

#print the total
print(total)