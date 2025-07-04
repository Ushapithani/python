def checkInclusion(s1, s2):  # leetcoee 567
    if len(s1) > len(s2):
        return False

    def char_to_index(c):
        return ord(c) - ord('a')

    
    s1_freq = [0] * 26
    s2_freq = [0] * 26

    for i in range(len(s1)):
        s1_freq[char_to_index(s1[i])] += 1
        s2_freq[char_to_index(s2[i])] += 1

    if s1_freq == s2_freq:
        return True

    for i in range(len(s1), len(s2)):
        s2_freq[char_to_index(s2[i])] += 1 # add
        s2_freq[char_to_index(s2[i - len(s1)])] -= 1 # remove

        if s1_freq == s2_freq:
            return True

    return False


s1 = "ab"
s2 = "eidbaooo"
print(checkInclusion(s1, s2))  # Output: True