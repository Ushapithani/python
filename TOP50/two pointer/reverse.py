def reverse_words(s):
    
    chars = list(s)

    def reverse_range(start, end):
        while start < end:
            chars[start], chars[end] = chars[end], chars[start]
            start += 1
            end -= 1

    # reverse the whole string 
    reverse_range(0, len(chars) - 1)

    #reverse ecah word
    n = len(chars)
    start = 0
    for end in range(n + 1):
        if end == n or chars[end] == ' ':
            reverse_range(start, end - 1)
            start = end + 1

    return ''.join(chars)
print(reverse_words("the sky is blue"))  # Output: "blue is sky the"