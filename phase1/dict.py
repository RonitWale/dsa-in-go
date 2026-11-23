'''
A dictionry in Python is an unordered, mutable collection of key-value pairs.
It is one of the most powerful built in data structures , used to map unique keys to values.

Why dictionary
1. fast lookups by key
2. keys are unique , values can be duplicated
3. greate for structured data(like JSON, db rows)
4. More readable and meaningful than lists for labled data

keys must be immutable type
values can be any type
duplicate keys are not allowed - the last value is retained

'''
my_dict = {
    "Ronit": "Misti",
    "Rohan": "Kim",
    "Rambabu": "Elizabeth"    
}

print(my_dict["Rambabu"], my_dict.get("Rohan"))


# Add / update in dictionary
my_dict["Montu"] = "Bhromor"

print(my_dict)

# Print all keys
print(my_dict.keys())

# Print all values
print(my_dict.values())

# remove keys : returns value of the key
print(my_dict.pop("Rambabu"))

'''
if you remove a key that is not there in dict that will throw error that key not exists
'''
print(my_dict)


# key value pair as tuple
print(my_dict.items())

( a, b , c) = my_dict.items()
print(a)
