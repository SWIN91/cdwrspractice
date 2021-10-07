# Given an array of integers.

# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.

# If the input array is empty or null, return an empty array.

# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

def count_positives_sum_negatives(arr):
    pos = []
    neg = []
    if arr == []:
        return []
    for n in arr:
        if n > 0:
            pos.append(n)
        if n < 0:
            neg.append(n)

    newlist = [len(pos), sum(neg)]
    return newlist  
    ## My solution

def count_positives_sum_negatives(arr):
    if not arr:
        return []
    pos = 0
    neg = 0
    for x in arr:
        if x > 0:
            pos += 1
        if x < 0:
            neg += x
    return [pos, neg]

    ## best practice clever 33

def count_positives_sum_negatives(arr):
    pos = sum(1 for x in arr if x > 0)
    neg = sum(x for x in arr if x < 0)
    return [pos, neg] if len(arr) else []
    ## clever 163

def count_positives_sum_negatives(arr):
    return [len([x for x in arr if x > 0])] + [sum(y for y in arr if y < 0)] if arr else []
    ## clever 259

