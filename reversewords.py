# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"

def reverse_words(text):
    reversed = text.split(" ")
    new_reversed = [word[::-1] for word in reversed]
    new_sentence = " ".join(new_reversed)
    return new_sentence
reverse_words('The quick brown fox jumps over the lazy dog.')
reverse_words('apple')
reverse_words('a b c d')
reverse_words('double  spaced  words')

def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' ')) #Best practice AND most clever