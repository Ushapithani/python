'''vowel vs Consonant Ratio*  
   Calculate the ratio of vowels to consonants in a string.'''
def vowel_consonant_ratio(text):
    vowels = set('aeiouAEIOU')
    c_count = 0
    v_count = 0
    for char in text:
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count +=1
    if c_count == 0:
        return "no consonant found , ratio undefined"
    return {
    "vowels": v_count,
    "consonants": c_count,
    "ratio": round(v_count / c_count, 2)}
    
inp = "hello this is usha"
print(vowel_consonant_ratio(inp)) #{'vowels': 6, 'consonants': 9, 'ratio': 0.67}

