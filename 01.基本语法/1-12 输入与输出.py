import re

def reverse(text):
   strs= text.split()
   spe=' '
   print(spe.join(strs[::-1]))
   return spe.join(strs[::-1])

def is_palindrome(text):
    return text==reverse(text)

something=input('Enter Text:')

if is_palindrome(something):
    print('Yes,it is a palindrome')
else:
    print('No,it is not a palindrome')


