from math import floor


def get_fuel_for_mass(mass):
    #divide by 3
    number_divided_by_three = int(mass) / 3
    #round down to nearest whole number
    number_rounded_down = floor(number_divided_by_three)
    #subtract 2
    number_subtracted_by_two = number_rounded_down - 2
    if number_subtracted_by_two < 0:
        return 0
    else:
        return number_subtracted_by_two


def get_fuel_for_fuel(fuel_mass, total):
    #get the fuel needed
    fuel_needed = get_fuel_for_mass(fuel_mass)
    #if it was zero
    if fuel_needed == 0:
        #return the total
        return total
    #otherwise
    else:
        #add to the total and get the fuel needed for this fuel
        return get_fuel_for_fuel(fuel_needed, total + fuel_needed)


#read the text file
with open("inputs/day1.txt", 'r') as inputfile:
    numbers = inputfile.readlines()
numbers = [x.strip() for x in numbers]

total = 0

#for each number in the file
for number in numbers:
    #work out how much fuel it needs
    fuel_for_module = get_fuel_for_mass(int(number))
    #work out how much fuel the fuel needs
    fuel_for_fuel = get_fuel_for_fuel(fuel_for_module, 0)
    #add it to the total
    total = total + fuel_for_module + fuel_for_fuel

#print the total
print(total)