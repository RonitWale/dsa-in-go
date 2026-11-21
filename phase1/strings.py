#strings in python

couple = "Rohan & Sonam"

#string length
print("Length of couple is:",len(couple))
#access a index
print("First element: ", couple[0])
#access to a index from one index
print(couple[0: 8])
print(couple[: 8])
print(couple[0: ])

boy = couple.split("&")
print(boy)

#last character of boy
print(couple[-1])

#skip variable in string
print(couple[0::2])

#reverse
reverse = couple[::-1] #-1 for reverse , 1 for straight
print(reverse)

# String operation
a = "20"
b = "10"
print(a+b, type(a+b))

#repitition in string
print(a * 3)

#Membership in string
print('1' in a)

'''
String methods
'''

message = " Learn Python!   "

# lowerCase
print(message.lower())

# Uppercase
print(message.upper())

#trim
print(message.strip())

#replace something in string
print(message.replace("Python", "To Code").strip())

#find something in string : returns index
print(message.find("P"))

#counting of something n a string: case sensitive
print(message.count("P"))

# check if star with something we want
print(message.startswith("L"), message.endswith(" "))

#isNumber string
print("123".isdigit())



csv_data = "apple, banana, guava"
print(csv_data.split(","))
