# The cockroach is one of the fastest insects. Write a function which takes its speed in km per hour and returns it in cm per second, rounded down to the integer (= floored).

# For example:

# 1.08 --> 30



def cockroach_speed(s):
    return s // 0.036     #Best practice AND most clever


def cockroach_speed(s):
    return int(s * 27.7778) #Makes the most sense to me