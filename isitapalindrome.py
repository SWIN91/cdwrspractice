# Write a function that checks if a given string (case insensitive) is a palindrome.

def is_palindrome(s):
    return True if s.lower()[::-1] == s.lower() else False
is_palindrome('a')
is_palindrome('aba')
is_palindrome('Abba')
is_palindrome('malam')
is_palindrome('walter')
is_palindrome('kodok')
is_palindrome('Kasue')

def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]  #Best practice and most clever