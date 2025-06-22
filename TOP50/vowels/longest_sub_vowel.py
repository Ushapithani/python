'''longesr substring with Only Vowels*  
   Given a string, find the length of the longest
    contiguous substring that contains only vowels'''




def longest_vowel_substring(s):
    vowels = set('aeiouAEIOU')    # BY using set we can reduce time complexity 0(n) to 0(1)
    max_len = 0
    current_len=0
    for char in s:
        if char in vowels:
            current_len += 1
            max_len = max(max_len, current_len)
        else:
            current_len =0  # reset when a non vowel is found
    return max_len
input_string = "hellooouuuaeiobbbbiiieee"
print("Longest vowel substring length:", longest_vowel_substring(input_string)) #10


