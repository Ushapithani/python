''' Vowel Palindrome Check
Check if the vowels in a string form a palindrome (ignoring consonants'''

def vowel_palindrome_check(text):
    vowels = set('aeiouAEIOU')
    vowels_list = []
    for char in text:
        if char in vowels:
            vowels_list.append(char.lower())
    return vowels_list[: : ] == vowels_list[: : -1]
input_string = "Usha saw I was Ashu"
print(vowel_palindrome_check(input_string)) #true
            

