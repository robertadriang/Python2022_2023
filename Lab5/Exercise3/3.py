#3) Using functions, anonymous functions, list comprehensions and filter, implement three methods to generate a list with all the vowels in a given string.
#For the string "Programming in Python is fun" the list returned will be ['o', 'a', 'i', 'i', 'o', 'i', 'u'].
VOWELS ='aeiou'

#1
def return_vowels(string):

    result=[]
    for letter in string:
        if letter.lower() in VOWELS:
            result.append(letter)
    return result

print(return_vowels("Programming in Python is fun"))

#2
return_vowels_anonymous=lambda string: [l for l in string if l.lower() in VOWELS]
print(return_vowels_anonymous("Programming in Python is fun"))

#3
filtered=filter(lambda l:l.lower() in VOWELS,"Programming in Python is fun")
print(list(filtered))