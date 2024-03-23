class Solution:
    def isPalindrome(self, s: str) -> bool:
        first = 0
        end = len(s) - 1

        if len(s) == 1:
            return True

        while first < end:
            if not s[first].isalnum():
                first += 1
            elif not s[end].isalnum():
                end -= 1
            else:
                if s[first].lower() != s[end].lower():
                    return False
                first += 1
                end -= 1

        return True