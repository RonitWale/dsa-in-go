'''

A list is an ordered , mutable collection of items , it can hold multiple values of different type of data

'''

my_list = []
print(type(my_list))

# push to list
my_list.append("apple")
my_list.append("cherry")
my_list.append("banana")
my_list.append("avocado")
my_list.append("kiwi")
my_list.append("mango")
print(my_list)


# modify list value 
my_list[0] = "guava"

print(my_list)

# pop an item
my_list.pop(3)
my_list.pop() #returns item that it deleted , if no index is set deletes the last item of the list
print(my_list)

# add at a position
my_list.insert(3, "avocado")
print(my_list)

# list appends another list
my_list_of_foods = ["Biryani", "Dal Chawal", "Tandoori Roti", "Chicken Chap"]
my_list.extend(my_list_of_foods)
print(my_list)



# copying a list
copy_list = my_list.copy()
print(copy_list)

# address check of both list
print(id(copy_list), id(my_list)) # Hence shallow copy

copy2_list = my_list
print(id(copy2_list), id(my_list)) # deep copy

# remove a partcular variable mentioned
my_list.remove("banana")
print(my_list)

# index and count cehckimg of an element in list
print(my_list.index("Biryani"), my_list.count("apple"), my_list_of_foods.count("Dal Chawal"))


# random list of numbers
number_list = [9,3,4,1,2,7,5]
number_list.sort()
number_list.reverse()
print(f"Sorted list {number_list}")


# Slicing 
print(my_list[1:4])
print(my_list[::-1])
print(my_list[-1])

my_list.clear()

print(my_list)


