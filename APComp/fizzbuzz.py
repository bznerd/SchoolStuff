"""
Ben Campbell 9/7/22
Fizzbuzz
Num 0 - 100 prints fizz if divisble by 3 and buzz if divisible by 5
"""

#Black magic fuckery basically
#List comprehension looping 0-100 making fstrings that use conditionals for adding fizz and buzz all added into one string by .join
print(''.join([f"{str(x)}: {'fizz' if x%3 == 0 else ''}{'buzz' if x%5 == 0 else ''}\n" for x in range (101)]))
