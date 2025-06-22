def count_vowels(s):
    if not s:  # Handles None or empty string
        return 0
    vowels = set('aeiou')
    return sum(1 for char in s.lower() if char in vowels)


print(count_vowels("HEllo, Usha!"))  # Output: 4