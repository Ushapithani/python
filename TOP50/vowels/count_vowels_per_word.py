''' Count Vowels in Each Word
Given a sentence, return a list of vowel counts for each word.'''

def count_vowels_per_word(sentance):
    if not sentance : 
        return []
    vowels=set('aeiouAEIOU')
    word = sentance.split()
    counts=[]
    for words in word: # splits each word
        count = 0
        for char in words:
            if char in vowels:
                count +=1
        counts.append(count)
    return counts


input_sentence = "Hello Usha how are you"

print(count_vowels_per_word(input_sentence))  # Output: [2, 2, 1, 2, 2]
    

            

