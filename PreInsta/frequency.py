def frequency_count(s):
    freq={}
    for char in s:
        freq[char]=freq.get(char, 0)+1
    return freq
word=input("enter the string :")
print("frequency count of the given string :" , frequency_count(word))

    