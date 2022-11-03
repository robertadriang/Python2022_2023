#8) a) Write a function called print_arguments with one parameter named function.
# # The function will return one new function which prints the arguments and the keyword arguments received and will return the output of the function receives as a parameter.
# Example:
# def multiply_by_two(x):
#     return x * 2

# def add_numbers(a, b):
#     return a + b
#
# augmented_multiply_by_two = print_arguments(multiply_by_two)
# x = augmented_multiply_by_two(10)  # this will print: Arguments are: (10,), {} and will return 20.
# augmented_add_numbers = print_arguments(add_numbers)
# x = augmented_add_numbers(3, 4)  # this will print: Arguments are: (3, 4), {} and will return 7.
def print_arguments(function):
    def result(*arg,**k_arg):
        print("Arguments are:", arg, k_arg)
        return function(*arg,**k_arg)
    return result

def multiply_by_two(x):
    return x * 2

def add_numbers(a, b):
    return a + b

augmented_multiply_by_two = print_arguments(multiply_by_two)
x = augmented_multiply_by_two(10)  # this will print: Arguments are: (10,), {} and will return 20.
print(x)
augmented_add_numbers = print_arguments(add_numbers)
x = augmented_add_numbers(3, 4)  # this will print: Arguments are: (3, 4), {} and will return 7.
print(x)


#b) Write a function called multiply_output with one parameter named function.
#The function will return one new function which returns the output of the function received multiplied by 2.
# Example:
# def multiply_by_three(x):
#     return x * 3
#
# augmented_multiply_by_three = multiply_output(multiply_by_three)
#
# x = augmented_multiply_by_three(10)  # this will return 2 * (10 * 3)
def multiply_output(function):
    def result(*arg,**k_arg):
        return 2*function(*arg,**k_arg)
    return result

def multiply_by_three(x):
    return x * 3

augmented_multiply_by_three = multiply_output(multiply_by_three)
x = augmented_multiply_by_three(10)  # this will return 2 * (10 * 3)
print(x)

#c) Write a function called augment_function with two parameters named function and decorators.
# decorators will be a list of functions which will have the same signature as the previous functions (print_arguments, multiply_output).
# augment_function will create a new function which is augmented using all the functions in the decorators list.
# Example:
# def add_numbers(a, b):
#     return a + b
#
# decorated_function = augment_function(add_numbers, [print_arguments, multiply_output])
# x = decorated_function(3, 4)  # this will print: Arguments are: (3, 4), {} and will return (2 * (3 + 4))
def augment_function(function,decorators):
    def result(*arg,**k_arg):
        res=function(*arg,**k_arg)
        for d in decorators:
            print("Res:",res)
            res=d(res)
            #res=res(*arg,**k_arg)
        return res
    return result

decorated_function = augment_function(add_numbers, [print_arguments, multiply_output])
x = decorated_function(3, 4)  # this will print: Arguments are: (3, 4), {} and will return (2 * (3 + 4))
print(x)

# @dec2
# @dec1
# def a(b):
#     print(b)