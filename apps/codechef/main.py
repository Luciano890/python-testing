# """..."""
# # importing the required module
# import timeit
# from itertools import filterfalse

# # code snippet to be executed only once
# mysetup = "from itertools import filterfalse"

# # code snippet whose execution time is to be measured
# codea = '''
# a = list(range(10000000))
# [x for x in a if x % 2]
# '''

# codeb = """
# a = list(range(10000000))
# filter(lambda x: x%2, a)
# """

# codec = """
# a = list(range(10000000))
# filterfalse(lambda x: x%2, a)
# """

# # timeit statement
# print("comprenhesion")
# print (timeit.timeit(
# 					stmt = codea,
# 					number = 1))

# print("filter")
# print (timeit.timeit(
# 					stmt = codeb,
# 					number = 1))

# print("filterfalse")
# print (timeit.timeit(
#                     setup= mysetup,
# 					stmt = codec,
# 					number = 1))

# # a = list(range(100))

# # for i in filterfalse(lambda x: x%2, a):
# #     print(i)
from string import ascii_uppercase

pairs = {j: i for i, j in enumerate(ascii_uppercase, 1)}

letter = input()
new_position = int(input())

current_position = pairs.get(letter)
pairs[letter] = new_position

pairs_slide = list(pairs.keys())[current_position: new_position]
for letter in pairs_slide:
    pairs[letter] -= 1

print(pairs)