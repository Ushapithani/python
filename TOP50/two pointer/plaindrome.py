def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True

text = input("Enter a string: ")
if is_palindrome(text):
    print("It's a palindrome!")
else:
    print("Not a palindrome.")