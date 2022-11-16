# 1. Write a function to return a list of the first n numbers in the Fibonacci string.
import copy


def fibonacci_list(n):
    if n == 0:
        return []
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        result = [0, 1]
        index = 2
        while index < n:
            result.append(result[index - 1] + result[index - 2])
            index += 1
        return result


def f(n): return [round(1.618033988749895 ** i / 5 ** 0.5) for i in range(1, n + 1)]


# 2. Write a function that receives a list of numbers and returns a list of the prime numbers found in it.
def return_primes(l):
    return [x for x in l if len([y for y in range(2, x // 2 + 1) if x % y == 0]) == 0 and x > 1]


def return_primes_2(l):
    result = []
    for e in l:
        if e < 2:
            continue
        flag = False
        for i in range(2, int(e ** 0.5) + 1):
            if e % i == 0:
                flag = True
                break
        if not flag:
            result.append(e)
    return result


def is_prime(e):
    if e == 2:
        return True
    if e < 2 or e % 2 == 0:
        return False
    for i in range(3, int(e ** 0.5) + 1, 2):
        if e % i == 0:
            return False
    return True


def return_primes_3(l):
    return list(filter(is_prime, l))


print("2:", return_primes(range(-100, 100)))
print("2:", return_primes_2(range(0, 100)))
print("2:", return_primes_3(range(0, 100)))


# 3. Write a function that receives as parameters two lists a and b and returns: (a intersected with b, a reunited with b, a - b, b - a)
def two_lists_operation(l1, l2):
    a_intersected_b = [e for e in l1 if e in l2]
    a_reunited_b = l1 + l2
    a_minus_b = [e for e in l1 if e not in l2]
    b_minus_a = [e for e in l2 if e not in l1]
    return a_intersected_b, a_reunited_b, a_minus_b, b_minus_a


print("3:", two_lists_operation([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))


# 4. Write a function that receives as a parameters a list of musical notes (strings), a list of moves (integers) and a start position (integer).
# The function will return the song composed by going though the musical notes beginning with the start position and following the moves given as parameter.
#	Example : compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2) will return ["mi", "fa", "do", "sol", "re"]
def compose(notes, moves, start):
    notes_len = len(notes)
    index = start % notes_len
    song = [notes[index]]
    for move in moves:
        index = (index + move) % notes_len
        song.append(notes[index])
    return song


print("4:", compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))


#  5. Write a function that receives as parameter a matrix and will return the matrix obtained by replacing all the elements under the main diagonal with 0 (zero).
def replace_under_diagonal(matrix):
    new_matrix = [row[:] for row in matrix]
    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[0])):
            if i > j:
                new_matrix[i][j] = 0
    return new_matrix


def replace_under_diagonal_2(matrix):
    new_matrix = [[0 if i > j else matrix[i][j] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return new_matrix


matrix_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("5:", replace_under_diagonal(matrix_a))
print("5:", replace_under_diagonal_2(matrix_a))


# print(matrix_a)


# 6. Write a function that receives as a parameter a variable number of lists and a whole number x. Return a list containing the items that appear exactly x times in the incoming lists.
# Example: For the [1,2,3], [2,3,4],[4,5,6], [4,1, "test"] and x = 2 lists [1,2,3 ] # 1 is in list 1 and 4, 2 is in list 1 and 2, 3 is in lists 1 and 2.
def elements_showing_x_times(*lists, x):
    aux_list = sum([x for x in lists], [])
    result_list = list(set(e for e in aux_list if aux_list.count(e) == x))
    return result_list


print("6:", elements_showing_x_times([1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"], x=2))


# 7. Write a function that receives as parameter a list of numbers (integers) and will return a tuple with 2 elements.
# The first element of the tuple will be the number of palindrome numbers found in the list and
# the second element will be the greatest palindrome number.
def palindrome_number_and_biggest_palindrome(list):
    palindromes = [x for x in list if str(x) == str(x)[::-1]]
    # print(palindromes)
    return len(palindromes), max(palindromes)


print("7:", palindrome_number_and_biggest_palindrome([1, 2, 3, 11, 132, 133, -22, -23, 100, 101]))


# 8. Write a function that receives a number x, default value equal to 1, a list of strings, and a boolean flag set to True.
# For each string, generate a list containing the characters that have the ASCII code divisible by x if the flag is set to True,
# otherwise it should contain characters that have the ASCII code not divisible by x.
def strange_function(list, x=1, flag=True):
    result = []  # result=[[l for string in list for l in string if ord(l)%x==0 ]  ###This creates a single list
    for string in list:
        if flag == True:
            aux_list = [l for l in string if ord(l) % x == 0]
        else:
            aux_list = [l for l in string if ord(l) % x != 0]
        result.append(aux_list)
    return result


print("8:", strange_function(["test", "hello", "lab002"], x=2, flag=False))
print("8:", strange_function(["test", "hello", "lab002"], x=2))


# 9. Write a function that receives as paramer a matrix which represents the heights of the spectators in a stadium and
# will return a list of tuples (line, column) each one representing a seat of a spectator which can't see the game.
# A spectator can't see the game if there is at least one taller spectator standing in front of him.
# All the seats are occupied.
# All the seats are at the same level.
# Row and column indexing starts from 0, beginning with the closest row from the field.
# Example:
# FIELD
# [[1, 2, 3, 2, 1, 1],
# [2, 4, 4, 3, 7, 2],
# [5, 5, 2, 5, 6, 4],
# [6, 6, 7, 6, 7, 5]]

# Will return : [(2, 2), (3, 4), (2, 4)]
def check_seating(matrix):
    unsatisfiend_spectators = [];
    for i in range(1, len(matrix)):  # start from 2nd row since 1st row will always see
        for j in range(len(matrix[0])):
            front_spectators = [e[j] for e in matrix[:i]]
            if max(front_spectators) >= matrix[i][j]:
                unsatisfiend_spectators.append((i, j))
    return unsatisfiend_spectators


def test(matrix):
    print(list(zip(*matrix)))


print("9:", check_seating([[1, 2, 3, 2, 1, 1],
                           [2, 4, 4, 3, 7, 2],
                           [5, 5, 2, 5, 6, 4],
                           [6, 6, 7, 6, 7, 5]]))
print(test([[1, 2, 3, 2, 1, 1],
            [2, 4, 4, 3, 7, 2],
            [5, 5, 2, 5, 6, 4],
            [6, 6, 7, 6, 7, 5]]))


# 10. Write a function that receives a variable number of lists and returns a list of tuples as follows:
# the first tuple contains the first items in the lists,
# the second element contains the items on the position 2 in the lists, etc.
# Ex: for lists [1,2,3], [5,6,7], ["a", "b", "c"] return: [(1.5, "a ") ,(5, 6, "b"), (3,7, "c")].
def regroup_lists(*lists):
    return list(zip(*lists))


print("10:", regroup_lists([1, 2, 3], [5, 6, 7], ["a", "b", "c"]))


# 11. Write a function that will order a list of string tuples based on the 3rd character of the 2nd element in the tuple.
# Example: ('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]
def sort_touples(l):
    return sorted(l, key=lambda e: e[1][2])


print("11:", sort_touples([('abc', 'bcd'), ('abc', 'zza')]))


#  12. Write a function that will receive a list of words  as parameter and will return a list of lists of words, grouped by rhyme.
#  Two words rhyme if both of them end with the same 2 letters.
#  Example:
#  group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']) will return [['ana', 'banana'], ['carte', 'parte'], ['arme']]
def group_by_rhyme(l):
    result = []
    aux = sorted(l, key=lambda e: e[-2:])
    previous_word = aux[0]
    same_rhyme = []
    for word in aux:
        if word[-2:] == previous_word[-2:]:
            same_rhyme.append(word)
        else:
            result.append(same_rhyme)
            same_rhyme = [word]
        previous_word = word
    result.append(same_rhyme)
    return result


print("12:", group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']))
