class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        frequency = defaultdict(int)
        for c in s:
            frequency[c] += 1
        
        for c in t:
            frequency[c] -= 1

        for val in frequency.values():
            if val != 0:
                return False

        return True