def is_palindrome(s):
    s = s.lower().replace(" ", "")  
    return s == s[::-1]  

word = input("enter the word :")
print(f"{word} is a palindrome: {is_palindrome(word)}")