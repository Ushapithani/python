   #Instead of just counting, return a dictionary
   # showing how many times each vowel appear

def frequency_map(s):
    if not s:
        return {}

    vowels = 'aeiou'
    s_lower = s.lower()
    freq = {v: 0 for v in vowels} #    freq = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    for char in s_lower:
        if char in vowels:
            freq[char] += 1  # += write only like this

    return freq


input_string = "Hello, Usha!"
print(frequency_map(input_string))   #{'a': 1, 'e': 1, 'i': 0, 'o': 1, 'u': 1}