#4) Write a function that receives a variable number of arguments and keyword arguments.
# The function returns a list containing only the arguments which are dictionaries, containing minimum 2 keys and at least one string key with minimum 3 characters.
#Example:
# my_function(
#  {1: 2, 3: 4, 5: 6},
#  {'a': 5, 'b': 7, 'c': 'e'},
#  {2: 3},
#  [1, 2, 3],
#  {'abc': 4, 'def': 5},
#  3764,
#  dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},
#  test={1: 1, 'test': True}
# ) will return: [{'abc': 4, 'def': 5}, {1: 1, 'test': True}]
def my_function(*args,**keyword_args):
    result=[]
    for e in [*args,*keyword_args.values()]:
        if type(e) is dict and len(e.keys())>=2:
            for key in e.keys():
                if len(str(key))>=3:
                    result.append(e)
                    break
    return result

def my_function_2(*args,**keyword_args):
    # result=[]
    # for e in [*args,*keyword_args.values()]:
    #     if type(e) is dict and len(e.keys())>=2:
    #         for key in e.keys():
    #             if len(str(key))>=3:
    #                 result.append(e)
    #                 break
    # return result
    # return list(filter(lambda e:(isinstance(e,dict) and len(e)>=2 and len(max(e,lambda key:str(key)))) ,[*args,*keyword_args.values()]))
    return list(filter(lambda e: (isinstance(e, dict) and (len(e)>=2) and max(e,key=lambda k:str(k))>=3),
                       [*args, *keyword_args.values()]))

res=my_function(
 {1: 2, 3: 4, 5: 6},
 {'a': 5, 'b': 7, 'c': 'e'},
 {2: 3},
 [1, 2, 3],
 {'abc': 4, 'def': 5},
 3764,
 dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},
 test={1: 1, 'test': True}
)
print(res)
res2=my_function_2(
 {1: 2, 3: 4, 5: 6},
 {'a': 5, 'b': 7, 'c': 'e'},
 {2: 3},
 [1, 2, 3],
 {'abc': 4, 'def': 5},
 3764,
 dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},
 test={1: 1, 'test': True}
)
print(res2)