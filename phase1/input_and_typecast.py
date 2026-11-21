"""
Typecasting and User Input

"""

#input() => Builtin python for taking user input from client end, return input as string
print("<<< sHello, welcome to my python program >>>")
name = None
age = None

name = input("Enter name -> ")
age = input("Enter age -> ")
print("Hello", name, "it's nice to mett you. You're", age, "years old.", "You were born on the year: ", 2026 - int(age))


"""
Typecasting 

"""

is_adult = int(age) >= 18 
print(name, "is an adult : ", bool(is_adult))