# Remove All Vowels

def remove_vowels(text):
    vowels = set('aeiouAEIOU')
    result  = ''.join([char for char in text if char not in vowels])
    return result

input_string = "Beautiful Day in the Neighborhood"
print(remove_vowels(input_string)) #Btfl Dy n th Nghbrhd

