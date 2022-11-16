# 9) Write a function that receives a list of pairs of integers (tuples with 2 elements) as parameter (named pairs).
# The function should return a list of dictionaries for each pair (in the same order as in the input list) that contain the following keys (as strings):
# sum (the value should be sum of the 2 numbers),
# prod (the value should be product of the two numbers),
# pow (the value should be the first number raised to the power of the second number)
# Example:

# f9(pairs = [(5, 2), (19, 1), (30, 6), (2, 2)] )  will return [{'sum': 7, 'prod': 10, 'pow': 25}, {'sum': 20, 'prod': 19, 'pow': 19}, {'sum': 36, 'prod': 180, 'pow': 729000000}, {'sum': 4, 'prod': 4, 'pow': 4}]
def f9(pairs):
    res = []
    for e in pairs:
        pair_dict = dict()
        pair_dict['sum'] = e[0] + e[1]
        pair_dict['prod'] = e[0] * e[1]
        pair_dict['pow'] = e[0] ** e[1]
        res.append(pair_dict)
    return res


print(f9(pairs=[(5, 2), (19, 1), (30, 6), (2, 2)]))
