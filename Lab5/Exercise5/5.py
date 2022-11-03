#5) Write a function with one parameter which represents a list.
# The function will return a new list containing all the numbers found in the given list.
#Example: my_function([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]) will return [1, 5, 6, 3.0]
def my_function(list):
    return [e for e in list if isinstance(e,(int,float,complex))]

print(my_function([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))