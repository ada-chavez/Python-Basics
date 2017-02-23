# Python 2.7.13
#
# Date: 02/23/2017
#
# Author: Ada Chavez
#
# Purpose:  A drill to practice writing a program in Python 2.7 using IDLE
#           for The Tech Academy


# 1) Assign an integer to a variable
age = 27

# 2) Assign a string to a variable
name = "Ada"

# 3) Assign a float to a variable
height = 5.2

# 4) Use the print function and .format() notation to print out the variable you assigned

print ("\nHello there {}! She is {} years old, and stands {} tall " .format(name,age,height))

# 5) Use each of these operations +,-,*,/,+=, =, %

num_1 = 4
num_2 = 2

add = num_1 + num_2
sub = num_1 - num_2
mult = num_1 * num_2
div = num_1 / num_2
rem = num_1 % num_2


print "Addition: {} + {} = {}".format(num_1,num_2,add)
print "Subtraction: {} - {} = {}".format(num_1,num_2,sub)
print "Multiplication: {} * {} = {}".format(num_1,num_2,mult)
print "Division: {} / {} = {}".format(num_1,num_2,div)
print "Remainder: {} % {} = {}".format(num_1,num_2,rem)

num_2 += 3
print "num_2 += 3 is {}".format(num_2)

# 6) Use of Logical operators: and, or, not

x = True
y = False
AND = x and y
OR = x or y
NOT = x is not y

print "x and y is:",AND
print "x or y is:",OR
print "x is not y is:",NOT

# 7) Use of conditional statements: if, elif, else

i = 5

if i == 2:
    print 'i = 2'
elif i == 3:
    print 'i = 3'
else:
    print 'i is not 2 or 3'

# 8) Use of a while loop
count = 0
while (count < 3):
    print 'While loop count:', count
    count += 1


# 9) Use of for loop
for counter in range(0,3):
    print "for loop count:",counter

# 10) Create a list and iterate through that list using a for loop to print each item on a new line
pokemon_list = ["pikachu","charmander","squirtle","bulbasaur"]
for pokemon in pokemon_list:
    print pokemon
    
# 11) Create a tuple and iterate through it using a for loop to print each item out on a new line
tup_list = (1,2,3,4)
for num in tup_list:
    print num
    
# 12) Define a function that returns a string variable

def string_func(x):
    some_value = str(x)
    return some_value


# 13) Call the function you defined above and print the result to the shell

string_value = string_func(100)
print "The interger value 100 is now a string value: ",string_value

