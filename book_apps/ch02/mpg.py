#!/usr/bin/env python3

# display a welcome mes450sage
print("The Miles Per Gallon program")
print()

# get input from the user
miles_driven= (input("Enter miles driven:\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t"))

# calculate and round miles per gallon
mpg = miles_driven / gallons_used
mpg = round(mpg, 2)

# display the result
print()
print(f"Miles Per Gallon:\t\t{mpg}")
print()
print("Bye!")


