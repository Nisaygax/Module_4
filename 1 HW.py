def IsPalindrome(s):
    return True if s == s[::-1] else False
    
print(IsPalindrome('шабаш'))