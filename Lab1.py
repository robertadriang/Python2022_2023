# Find The greatest common divisor of multiple numbers read from the console.
import re
import string


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def pb_1():
    number1 = int(input("First:"))
    number2 = int(input("Second:"))
    result = gcd(number1, number2)
    print(result)


# # Write a script that calculates how many vowels are in a string.
def count_vowels(text):
    sum = 0
    for vowel in "aeiou":
        sum += text.lower().count(vowel)
    print("Vowels in text:", sum)


def count_vowels_oneliner(text):
    print("Vowels in text:", sum([1 for e in text.lower() if e in 'aeiou']))


def pb_2():
    text = "Write a script that calculates how many vowels are in a string."
    count_vowels(text)
    count_vowels_oneliner(text)


# Write a script that receives two strings and prints the number of occurrences of the first string in the second.
def count_occurences(str1, str2):
    print("Case sensitive:", str1.count(str2))
    print("Case insensitive:", str1.lower().count(str2))


def pb_3():
    str1 = "The string.count() is an in-built function in Python2022_2023 that returns the quantity or number of occurrences of a substring in a given particular string. " \
           "Moreover, it has additional parameters start and end to specify the indices of starting and ending positions."
    str2 = "the"
    count_occurences(str1, str2)


# Write a script that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.
from functools import reduce
import copy


def camel_to_snake(text):
    return reduce(lambda a, b: a + ('_' if b in "QWERTYUIOPASDFGHJKLZXCVBNM" else '') + b, text).lower()


# lambda :expression

def pb_4():
    str3 = "UpperCamelCaseText"
    print(camel_to_snake(str3))


# Given a square matrix of characters write a script that prints the string obtained by going through the matrix in spiral order (as in the example):
# firs      1  2  3  4    =>   first_python_lab
# n_lt      12 13 14 5
# oba_      11 16 15 6
# http

MAX_ROWS = 4
MAX_COLUMNS = 4


def is_inside(i, j):
    if (i < 0 or i >= MAX_ROWS or j < 0 or j >= MAX_COLUMNS):
        return False
    return True


def is_blocked(matrix, i, j):
    if not is_inside(i, j) or matrix[i][j] == -1:
        return True
    return False


def traverse_DFS(matrix, i, j, Dir, res):
    if is_blocked(matrix, i, j):
        return

    all_blocked = True
    for k in range(-1, 2, 2):
        all_blocked = all_blocked and is_blocked(matrix, k + i, j) and is_blocked(matrix, i, j + k)

    res.append(matrix[i][j])
    matrix[i][j] = -1
    if all_blocked:
        return

    nxt_i = i
    nxt_j = j
    nxt_dir = Dir
    if Dir == 0:
        if not is_blocked(matrix, i, j + 1):
            nxt_j += 1
        else:
            nxt_dir = 1
            nxt_i += 1

    elif Dir == 1:
        if not is_blocked(matrix, i + 1, j):
            nxt_i += 1
        else:
            nxt_dir = 2
            nxt_j -= 1

    elif Dir == 2:
        if not is_blocked(matrix, i, j - 1):
            nxt_j -= 1
        else:
            nxt_dir = 3
            nxt_i -= 1

    elif Dir == 3:
        if not is_blocked(matrix, i - 1, j):
            nxt_i -= 1
        else:
            nxt_dir = 0
            nxt_j += 1

    traverse_DFS(matrix, nxt_i, nxt_j, nxt_dir, res)


def spirally_traverse(matrix):
    res = []
    traverse_DFS(matrix, 0, 0, 0, res)
    return res


# firs      1  2  3  4    =>   first_python_lab
# n_lt      12 13 14 5
# oba_      11 16 15 6
# htyp
def pb_5():
    matrix = [['f', 'i', 'r', 's'],
              ['n', '_', 'l', 't'],
              ['o', 'b', 'a', '_'],
              ['h', 't', 'y', 'p']]
    res = spirally_traverse(matrix)
    print(res)


# Write a function that validates if a number is a palindrome.
def is_palindrome(number):
    return str(number) == str(number)[::-1]


def pb_6():
    number1 = 12345
    number2 = 12321
    number3 = 0
    for n in [number1, number2, number3]:
        print("Is {} palindrome? A: {}".format(n, is_palindrome(n)))


# Write a function that extract a number from a text (for example if the text is "An apple is 123 USD", this function will return 123,
# or if the text is "abc123abc" the function will extract 123). The function will extract only the first number that is found.
def extract_number(text):
    number = re.search('[0-9]+', text).group(0)
    print(number)


def pb_7():
    text1 = "An apple is 123 USD"
    text2 = "abc123abc"
    text3 = text1 + text2
    extract_number(text1)
    extract_number(text2)
    extract_number(text3)


# Write a function that counts how many bits with value 1 a number has. For example for number 24, the binary format is 00011000, meaning 2 bits with value "1"
def count_bits(number):
    bindata = format(number, "b")
    print(number, bindata, bindata.count('1'))


def pb_8():
    for number in [1, 23, 555, 2048, 432]:
        count_bits(number)


# Write a functions that determine the most common letter in a string. For example if the string is "an apple is not a tomato", then the most common character is "a" (4 times). Only letters (A-Z or a-z) are to be considered. Casing should not be considered "A" and "a" represent the same character.
def get_most_common_letter(text):
    most_common=max([(i, text.count(i)) for i in set(text.lower()).intersection(string.ascii_lowercase)],key=lambda e:e[1])[0]
    print(most_common)

def pb_9():
    get_most_common_letter("an apple is not a tomato")

#Write a function that counts how many words exists in a text. A text is considered to be form out of words that are separated by only ONE space. For example: "I have Python2022_2023 exam" has 4 words.
def count_words(text):
    words=text.split(" ")
    print(text,len(words))

def pb_10():
    count_words("I have Python2022_2023 exam")
    count_words("I have Python2022_2023 exam...")
    count_words("I have Python2022_2023 exam .")

if __name__ == '__main__':
    # pb_1()
    pb_2()
    pb_3()
    pb_4()
    pb_5()
    pb_6()
    pb_7()
    pb_8()
    pb_9()
    pb_10()
