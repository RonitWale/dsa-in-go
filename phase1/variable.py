# print statement
print("Hello Python family")

name = "Ronit Roy learning python"
age = 26
city = "Naihati"
height = 5.10


print(name, age, city, height)


# newline print
print("Endline", end="\n")

# separator operator
print(name, age, city, height, sep=" || ")

# breakline
print("This is line one data", "\n", "This should appear on line 2")

# tab separator
print("This is line one data", "\t", "This should appear on line 2")

#statement with multiple backtick printing
print('Ronit\'s favourite food imn monsoon is khichri')


#comment in python
print(name , "is", age, "years old")

"""

Multiline comment

"""




"""
Variables, Data Types Learning
in Python
"""

my_name = "Ronit Roy"
my_age = 26
my_height = 5.10
is_adult = my_age >= 18 

print(type(my_name))
print(type(my_age))
print(type(my_height))
print(type(is_adult), is_adult)

# Unsupported operation between different data types in python
# print(50+"10") => Not Allowed
# print(50-10) => Allowed