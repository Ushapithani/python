class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []

        def to_index(c):
            return ord(c) - ord('a')

        p_count = [0] * 26
        s_count = [0] * 26
        result = []

        for i in range(len(p)):
            p_count[to_index(p[i])] += 1
            s_count[to_index(s[i])] += 1

        if s_count == p_count:
            result.append(0)

        for i in range(len(p), len(s)):
            s_count[to_index(s[i])] += 1
            s_count[to_index(s[i - len(p)])] -= 1

            if s_count == p_count:
                result.append(i - len(p) + 1)

        return result
s = "cbaebabacd"
p = "abc"
sol = Solution()
print(sol.findAnagrams(s, p))  # Output: [0, 6]