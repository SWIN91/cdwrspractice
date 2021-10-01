# Philip's just turned four and he wants to know how old he will be in various years in the future such as 2090 or 3044. His parents can't keep up calculating this so they've begged you to help them out by writing a programme that can answer Philip's endless questions.

# Your task is to write a function that takes two parameters: the year of birth and the year to count years in relation to. As Philip is getting more curious every day he may soon want to know how many years it was until he would be born, so your function needs to work with both dates in the future and in the past.

# Provide output in this format: For dates in the future: "You are ... year(s) old." For dates in the past: "You will be born in ... year(s)." If the year of birth equals the year requested return: "You were born this very year!"

# "..." are to be replaced by the number, followed and proceeded by a single space. Mind that you need to account for both "year" and "years", depending on the result.

# Good Luck!

def calculate_age(year_of_birth, current_year):
    if year_of_birth < current_year:
        age = current_year-year_of_birth
        if age > 1:
            return f"You are {age} years old."
        elif age == 1:
            return f"You are {age} year old."
    if year_of_birth > current_year:
        age = year_of_birth-current_year
        if age > 1:
            return f"You will be born in {age} years."
        elif age ==1:
            return f"You will be born in {age} year."
    if year_of_birth == current_year:
        age = current_year
        return "You were born this very year!"

# My solution ^

def calculate_age(year_of_birth, current_year):
    diff = abs(current_year - year_of_birth)
    plural = '' if diff == 1 else 's'
    if year_of_birth < current_year:
        return 'You are {} year{} old.'.format(diff, plural)
    elif year_of_birth > current_year:
        return 'You will be born in {} year{}.'.format(diff, plural)
    return 'You were born this very year!'
# Best practice ^

def calculate_age(birth, curr):
    diff = abs(curr - birth)
    age = "%d year%s" % (diff, "s" * bool(diff-1))
    return "You were born this very year!" if not diff else "You are %s old." % age if curr > birth else "You will be born in %s." % age
# Most clever though I don't understand this implementation

calculate_age=lambda b, y: (lambda d: "You are %s year%s old." %(d,"s" if d!=1 else "") if d>0 else "You will be born in %s year%s." %(-d,"s" if d!=-1 else "") if d<0 else "You were born this very year!")(y-b)
# Lambda version of it ^