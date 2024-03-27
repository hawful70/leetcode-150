class Solution:
    # def characterReplacement(self, s: str, k: int) -> int:
    #     frequency = defaultdict(int)
    #     start = 0
    #     res = 0

    #     for end in range(len(s)):
    #         frequency[s[end]] += 1

    #         while (end - start + 1) - max(frequency.values()) > k:
    #             frequency[s[start]] -= 1
    #             start += 1
    #         res = max(res, end - start + 1)

    #     return res

    def characterReplacement(self, s: str, k: int) -> int:
        frequency = defaultdict(int)
        start = 0
        res = 0
        maxF = 0

        for end in range(len(s)):
            frequency[s[end]] += 1
            maxF = max(maxF, frequency[s[end]])
            while (end - start + 1) - maxF > k:
                frequency[s[start]] -= 1
                start += 1
            res = max(res, end - start + 1)

        return res