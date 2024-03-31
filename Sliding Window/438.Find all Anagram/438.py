from ast import List
class Solution:
    # def findAnagrams(self, s: str, p: str) -> List[int]:
    #     pL, sL = len(p), len(s)
    #     p_Count, s_Count = Counter(p), Counter()
    #     res = []

    #     l = 0
    #     for r in range(sL):
    #         s_Count[s[r]] += 1
    #         if r >= pL:
    #             if s_Count[s[r - pL]] == 1:
    #                 del s_Count[s[r - pL]]
    #             elif s_Count[s[r - pL]] > 1:
    #                 s_Count[s[r - pL]] -= 1
    #             l += 1
            
    #         if p_Count == s_Count:
    #             res.append(l)
            
    #     return res
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_Count, s_Count = [0] * 26, [0] * 26
        res = []
        for i in range(len(p)):
            p_Count[ord(p[i]) - ord('a')] += 1

        l = 0
        for r in range(len(s)):
            s_Count[ord(s[r]) - ord('a')] += 1
            if r >= len(p):
                s_Count[ord(s[l]) - ord('a')] -= 1
                l += 1
            if p_Count == s_Count:
                res.append(l)
        return res

