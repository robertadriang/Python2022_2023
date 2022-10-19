# 1.Write a function that receives as parameters two lists a and b and returns a list of sets containing: (a intersected with b, a reunited with b, a - b, b - a)
def operations_with_sets(a, b):
    a = set(a)
    b = set(b)
    return [a & b, a | b, a - b, b - a]


print("1:", operations_with_sets([1, 2, 3, 4], [3, 4, 5, 6]))


# 2. Write a function that receives a string as a parameter and returns a dictionary in which the keys are the characters in the character string and the values are the number of occurrences of that character in the given text.
def occurences_of_letters(string):
    result = dict.fromkeys(string, 0)
    for letter in string:
        result[letter] += 1
    return result


print("2:", occurences_of_letters("Ana has apples."))


# 3. Compare two dictionaries without using the operator "==" and return a list of differences as follows:
# (Attention, dictionaries must be recursively covered because they can contain other containers, such as dictionaries, lists, sets, etc.)
def compare_dictionaries(d1, d2):
    print(d1)
    print(d2)
    missmatches = []
    if type(d1)!=type(d2):
        missmatches.append("d1 and d2 have different types")
        return
    for i,e in enumerate(d1):
        if isinstance(d1,dict):
            if e not in d2:
                missmatches.append(e + " is only in d1")
                return missmatches
        elif isinstance(d1, list):
            if len(d1) != len(d2):
                missmatches.append("lists have different len")
                return missmatches
            e=i
        if isinstance(d1,(dict,list)):
            if type(d1[e]) != type(d2[e]):
                missmatches.append(e + " has different type in d1 and d2")
            elif isinstance(d1[e],(list,dict)):
                missmatches.append(compare_dictionaries(d1[e],d2[e]))
            elif d1[e]!=d2[e]:
                missmatches.append(f"{d1[e]} has a different value from {d2[e]}")
    return missmatches


print(compare_dictionaries({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'},
                     {'a': [3, 4], '{1, 2} | {2, 3}': {1, 2, 3}, '{1, 2} & {2, 3}': {2}, '{1, 2} - {2, 3}': {1},
                      '{2, 3} - {1, 2}': {3}, '{2, 3} | {2, 3}': {2, 3}, '{2, 3} & {2, 3}': {2, 3},
                      '{2, 3} - {2, 3}': set()}))


# 4. The build_xml_element function receives the following parameters: tag, content, and key-value elements given as name-parameters.
# Build and return a string that represents the corresponding XML element.
# Example: build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid ")
# returns  the string = "<a href=\"http://python.org \"_class = \" my-link \"id = \"someid \"> Hello there </a>"
def build_xml_element(tag, content, **name_parameters):
    xml_element = "<"
    xml_element += tag
    for element in name_parameters.items():
        xml_element += " " + element[0] + "=" + element[1].replace(" ", "\"")
    xml_element += "> "
    xml_element += content
    xml_element += " </" + tag + ">"
    return xml_element


print("4:", build_xml_element("a", "Hello there", href=" http://python.org ", _class=" my-link ", id=" someid "))


# 5. The validate_dict function that receives as a parameter a set of tuples ( that represents validation rules for a dictionary that has strings as keys and values) and a dictionary.
# A rule is defined as follows: (key, "prefix", "middle", "suffix"). A value is considered valid if it starts with "prefix", "middle" is inside the value (not at the beginning or end) and ends with "suffix".
# The function will return True if the given dictionary matches all the rules, False otherwise.
# Example: the rules  s={("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}  and d= {"key1": "come inside, it's too cold out", "key3": "this is not valid"} => False because although the rules are respected for "key1" and "key2" "key3" that does not appear in the rules.
def matches_structure(e, rule_set):
    return e.startswith(rule_set[1]) and e[1:-1].find(rule_set[2]) != -1 and e.endswith(rule_set[3])


def validate_dict_function(rules, dictionary):
    for d_element in dictionary:
        rules_for_element = {e for e in rules if e[0] == d_element}
        if len(rules_for_element) == 0:
            return False
        for rule in rules_for_element:
            if not matches_structure(dictionary[d_element], rule):
                return False
    return True


def test_validate():
    print("5: (example)", validate_dict_function({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")},
                                                 {"key1": "come inside, it's too cold out",
                                                  "key3": "this is not valid"}))
    print("5: (valid dict)", validate_dict_function({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")},
                                                    {"key1": "come inside, it's too cold out"}))
    print("5: (wrong start)",
          validate_dict_function({("key1", "a", "inside", ""), ("key2", "start", "middle", "winter")},
                                 {"key1": "come inside, it's too cold out"}))
    print("5: (wrong end)", validate_dict_function({("key1", "", "inside", "b"), ("key2", "start", "middle", "winter")},
                                                   {"key1": "come inside, it's too cold out"}))
    print("5: (wrong middle)",
          validate_dict_function({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")},
                                 {"key1": "come inside"}))
    print("5: (wrong middle 2)",
          validate_dict_function({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")},
                                 {"key1": "come, it's too cold out"}))


test_validate()


# 6. Write a function that receives as a parameter a list and returns a tuple (a, b), representing the number of unique elements in the list, and b representing the number of duplicate elements in the list
# (use sets to achieve this objective).
def unique_and_duplicate_count(a):
    set_from_a = set(a)
    unique = 0
    duplicated = 0
    for element in set_from_a:
        if a.count(element) == 1:
            unique += 1
        else:
            duplicated += 1
    return (unique, duplicated)


print("6:", unique_and_duplicate_count([1, 2, 3, 4, 5, 1, 1, 6, 7, 7, 8]))


# 7. Write a function that receives a variable number of sets and returns a dictionary with the following operations from all sets two by two: reunion, intersection, a-b, b-a.
# The key will have the following form: "a op b", where a and b are two sets, and op is the applied operator: |, &, -.
# Ex: {1,2}, {2, 3} =>
# {
#    "{1, 2} | {2, 3}": 3,
#    "{1, 2} & {2, 3}": 1,
#    "{1, 2} - {2, 3}": 1,
#    ...
# }
def create_unique_pairs(*sets):
    # pairs_of_sets=[(x,y) for x in sets for y in sets if x!=y] # this option won't return a pair when we give the same set multiple times
    # unique_pairs=[]
    # for e in pairs_of_sets:
    #     if (e[1],e[0]) not in unique_pairs and e not in unique_pairs:
    #         unique_pairs.append(e)
    # return unique_pairs
    unique_pairs = []
    for i in range(len(sets) - 1):
        for j in range(i + 1, len(sets)):
            if (sets[i], sets[j]) not in unique_pairs:
                unique_pairs.append((sets[i], sets[j]))
    return unique_pairs


def dictionary_from_sets(*sets):
    unique_pairs = create_unique_pairs(*sets)
    # print(unique_pairs)
    dictionary = {}
    for pair in unique_pairs:
        dictionary[str(pair[0]) + " | " + str(pair[1])] = pair[0] | pair[1]
        dictionary[str(pair[0]) + " & " + str(pair[1])] = pair[0] & pair[1]
        dictionary[str(pair[0]) + " - " + str(pair[1])] = pair[0] - pair[1]
        dictionary[str(pair[1]) + " - " + str(pair[0])] = pair[1] - pair[0]
    return dictionary


print("7:", dictionary_from_sets({1, 2}, {2, 3}, {2, 3}))


# 8. Write a function that receives a single dict parameter named mapping. This dictionary always contains a string key "start". Starting with the value of this key you must obtain a list of objects by iterating over mapping in the following way: the value of the current key is the key for the next value, until you find a loop (a key that was visited before). The function must return the list of objects obtained as previously described.
# Ex: loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}) will return ['a', '6', 'z', '2']
def loop(mapping):
    current = mapping['start']
    traversed = [current]
    while mapping[current] not in traversed:
        traversed.append(mapping[current])
        current = mapping[current]
    return traversed


print("8:", loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))


# 9. Write a function that receives a variable number of
# positional arguments and
# a variable number of keyword arguments
# and will return the number of positional arguments whose values can be found among keyword arguments values.
# Ex: my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5) will return returna 3
#Suprascriere de obiecte de apeleaza a doua functie
def my_function(*positional_arguments, **keyword_arguments):
    keyword_values = keyword_arguments.values()
    matches = 0
    for p_arg in positional_arguments:
        if p_arg in keyword_values:
            matches += 1
    print("@")
    return matches


def my_function(*positional_arguments, **keyword_arguments):
   p_set=set(positional_arguments)
   k_set=set(keyword_arguments.values())
   return len(p_set & k_set)


print("9:", my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5))
