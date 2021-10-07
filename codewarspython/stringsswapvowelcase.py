def swap_vowel_case(st): 
    return "".join(x.swapcase() if x in "aeiouAEIOU" else x for x in st)
# Best practice ^, pretty clever @ 11


T = str.maketrans("aiueoAIUEO", "AIUEOaiueo")

def swap_vowel_case(s):
    return s.translate(T)
# Clever ranked @ 12
