#!/usr/bin/env python3

# display a welcome message
print("The Test Scores program")
print()
print("Enter 3 test scores")
print("======================")

# get scores from the user
total_score = 0       # initialize the variable for accumulating scores
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

# calculate average score
average_score = round((a+b+c) / 3)
             
# format and display the result
print("======================")
print("Total Score:  ", a+b+c,
      "\nAverage Score:", average_score)
print()
print("Bye")