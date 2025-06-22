class VowelCounter:
    def __init__(self):
        self.vowel_count = 0
        self.vowels = set('aeiouAEIOU')  

    def process_char(self, char):
        if char in self.vowels:
            self.vowel_count += 1
        return self.vowel_count
vc = VowelCounter()
stream = "Copilot is amazing!"

for ch in stream:
    count = vc.process_char(ch)
    print(f"After '{ch}': Vowel Count = {count}")


'''After 'C': Vowel Count = 0
After 'o': Vowel Count = 1
After 'p': Vowel Count = 1
After 'i': Vowel Count = 2
After 'l': Vowel Count = 2
After 'o': Vowel Count = 3
After 't': Vowel Count = 3
After ' ': Vowel Count = 3
After 'i': Vowel Count = 4
After 's': Vowel Count = 4
After ' ': Vowel Count = 4
After 'a': Vowel Count = 5
After 'm': Vowel Count = 5
After 'a': Vowel Count = 6
After 'z': Vowel Count = 6
After 'i': Vowel Count = 7
After 'n': Vowel Count = 7
After 'g': Vowel Count = 7
After '!': Vowel Count = 7'''