# In this kata, your job is to return the two distinct highest values in a list. If there're less than 2 unique values, return as many of them, as possible.

# The result should also be ordered from highest to lowest.

# Examples:

# [4, 10, 10, 9]  =>  [10, 9]
# [1, 1, 1]  =>  [1]
# []  =>  []

def two_highest(arg1):
    return sorted(list(set(arg1)), reverse=True)[:2]
two_highest([15, 20, 20, 17])



def two_highest(ls):
    result = sorted(list(set(ls)), reverse=True)[:2]
    return result if isinstance(ls, (list)) else False # Best practice


import heapq
def two_highest(list_):
    return heapq.nlargest(2, set(list_)) if type(list_) == list else False # Most clever
