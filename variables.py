# Showing how variables work
# Author: Juergen Lier
# Date: 20 September 2024
# Version: 1


# Different types of variables
# Store a number
num_1 = 80 # assigning 80 to num_1
print(num_1) # This displays what num_1 contains

# Store a string
name_1 = "Juergen,"
print(name_1)
#name = "aaskjdha" # reassinging value to an existing variable
# print(name)

# Do calculations in a variable and store the result
# sum=5+5 # not good practice 
sum = 5 + 5 # follows PEP8 Python conventions
print(sum) 
sum_string = " 5 + 5 = 10" # this is a string
print(sum_string)

# Adding strings together is called concatenation
concatenation = name_1 + sum_string
print(concatenation)