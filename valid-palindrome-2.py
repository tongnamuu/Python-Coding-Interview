import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^a-z0-9]', '', s.lower())
        return s == s[::-1]


input_str = "A man, a plan, a canal: Panama"
solution = Solution()
answer = solution.isPalindrome(input_str)
print(answer)
