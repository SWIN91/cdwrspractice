# Complete the method that takes a boolean value and return a 
# "Yes" string for true, or a "No" string for false.


def bool_to_word(boolean):
    return "Yes" if boolean == True else "No"     
bool_to_word(True)
bool_to_word(False)

# Best practice ↓
def bool_to_word(bool):
    return "Yes" if bool else "No" # I guess bool evaluates to True???