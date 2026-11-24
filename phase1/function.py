def function_name(parameters):
    """ optional docstring"""
    # function body
    return parameters

print(function_name("Hello World"))


def summation(a, b) :
    return a + b
print(summation(3,6))


#args
def summationArgs(*nums) :
    return sum(nums)
print(summationArgs(3,6))
