class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        d = [[0]*len(s) for _ in range(len(s))]
        s_index = 0
        e_index = 1
        for i in range(len(s)):
            d[i][i] = 1
            if i + 1 < len(s) and s[i] == s[i + 1]:
                d[i][i + 1] = 1
                s_index = i
                e_index = i + 2

        for l in range(3, len(s) + 1):
            for i in range(len(s)):
                j = l + i - 1
                if j >= len(s):
                    break
                if d[i + 1][j - 1] == 1 and s[i] == s[j]:
                    d[i][j] = 1
                    s_index = i
                    e_index = j + 1
        return s[s_index:e_index]


input_str = "abcda"
solution = Solution().longestPalindrome(input_str)
print(solution)
