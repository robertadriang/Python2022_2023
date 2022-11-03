#7) Write a function called process that receives a variable number of keyword arguments
# The function generates the first 1000 numbers of the Fibonacci sequence and then processes them in the following way:
# If the function receives a parameter called filters, this will be a list of predicates (function receiving an argument and returning True/False) and will retain from the generated numbers only those for which the predicates are True.
# If the function receives a parameter called limit, it will return only that amount of numbers from the sequence.
# If the function receives a parameter called offset, it will skip that number of entries from the beginning of the result list.
# The function will return the processed numbers.
# Example:

#
# process(
#     filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],
#     limit=2,
#     offset=2
# ) returns [34, 144]

# Explanation:
# Fibonacci sequence will be: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610...
# Valid numbers are: 2, 8, 34, 144, 610, 2584, 10946, 832040
# After offset: 34, 144, 610, 2584, 10946, 832040
# After limit: 34, 144

def process(**keyword_args):
    fibonacci_sequence=[0,1]
    while len(fibonacci_sequence)<1000:
        fibonacci_sequence.append(fibonacci_sequence[-1]+fibonacci_sequence[-2])

    if 'filters' in keyword_args.keys():
        for f_term in keyword_args['filters']:
            fibonacci_sequence=list(filter(f_term,fibonacci_sequence))
        #print(fibonacci_sequence)

    if 'offset' in keyword_args.keys():
        fibonacci_sequence=fibonacci_sequence[keyword_args['offset']:]
        #print(fibonacci_sequence)

    if 'limit' in keyword_args.keys():
        fibonacci_sequence=fibonacci_sequence[:keyword_args['limit']]
        #print(fibonacci_sequence)

    return fibonacci_sequence


def sum_digits(x):
    return sum(map(int, str(x)))

print(process(
    filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],
    limit=2,
    offset=2
))