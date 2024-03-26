class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        start, end = 0, 0
        charSet = set()

        while end < len(s):
            if s[end] not in charSet:
                charSet.add(s[end])
                maxLength = max(maxLength, end - start + 1)
            else:
                while s[end] in charSet:
                    charSet.remove(s[start])
                    start += 1
                charSet.add(s[end])
            end += 1

        return maxLength

