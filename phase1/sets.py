'''

SET is a type of data structure which is unordered, unindexed collection of unique element. Mutable,
but elements must be immutable data types 


needed when union(), intersection(), difference() maths operation we do need sets
'''
my_set = {1,2,3,3,2,3}
print(my_set, type(my_set))

my_set.add(100)

my_set.remove(2)

print(my_set, type(my_set))

print(my_set.discard(4))


# Union 
my_union_set = { 3,5,6}
print(my_set.union(my_union_set), my_set.intersection(my_union_set), my_set & my_union_set, my_union_set - my_set)