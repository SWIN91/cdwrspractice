# You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.

# Array can contain numbers or strings. X can be either.

# Return true if the array contains the value, false if not.

def check(seq, elem):
    if elem in seq:
        return True
    else:
        return False


def check(seq, elem):
    return elem in seq  #Best Practice Clever 129



from operator import contains as check #Clever 131