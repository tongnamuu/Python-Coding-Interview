class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(l: int, r: int) -> str:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]

        if s == s[::-1]:
            return s

        ans = str(s[0])
        for i in range(len(s)):
            ans = max(ans, is_palindrome(i - 1, i + 1), is_palindrome(i, i+1), key=len)
        return ans


input_str = "bababe"
solution = Solution().longestPalindrome(input_str)
print(solution)