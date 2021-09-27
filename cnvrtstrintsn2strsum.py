# Create a function that takes 2 nonnegative integers in form of a string as an input, and outputs the sum (also as a string):

# Example: (Input1, Input2 -->Output)

# "4",  "5" --> "9"
# "34", "5" --> "39"
# Notes:

# If either input is an empty string, consider it as zero.

# Inputs and the expected output will never exceed the signed 32-bit integer limit (2^31 - 1)

def sum_str(a, b):
    return str(int(a or 0) + int(b or 0))
        
print(sum_str("4","5"))
print(sum_str("34","5"))
print(sum_str("9",""))
print(sum_str("","9"))
print(sum_str("",""))