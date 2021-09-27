# Your function takes two arguments:

# current father's age (years)
# current age of his son (years)
# Сalculate how many years ago the father was twice as old as his son (or in how many years he will be twice as old).


def twice_as_old(dad_years_old, son_years_old):
    years = son_years_old * 2
    return dad_years_old - years if dad_years_old >= years else years - dad_years_old
twice_as_old(36,7)
twice_as_old(55,30)
twice_as_old(42,21)
twice_as_old(22,1)
twice_as_old(29,0)


def twice_as_old(dad_years_old, son_years_old):
    return abs(dad_years_old - 2*son_years_old) #Best practice AND most clever