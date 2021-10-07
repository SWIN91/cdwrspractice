# Write a function which converts the input string to uppercase.

def make_upper_case(s):
    s = s.upper()
    return s
make_upper_case("hello")

def make_upper_case(s): 
    return s.upper() # Best practice


make_upper_case = str.upper # most clever, but not a function