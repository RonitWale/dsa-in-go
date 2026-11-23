'''

A tuple is an ordered , immutable collection of values in python , defined using parenthesis () instead of square brackets []

faster than lists
safe from accidental mutation
used for fixed data collections
can be used as dictionary key

'''

# example tuple 
my_tuple = ("blue", "orange", "white")


print(my_tuple, type(my_tuple))


# access 
print(my_tuple[0], my_tuple[1], my_tuple[2])

#count an element in tuple
print(my_tuple.count("blue"))

# second tuple 
my_2nd_tuple = ("red", "black")

#concat
print(my_tuple + my_2nd_tuple)

# tuple multiple notification
print(2 * my_tuple)

info = ("Ronit", "26 yrs", "Kolkata")

# packing & unpacking [destructure]
name, age , city = info

print(name, age, city)


