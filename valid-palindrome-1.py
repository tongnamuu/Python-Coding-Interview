class Solution:
    def isPalindrome(self, s: str) -> bool:
        ch_list = [ch.lower() for ch in s if ch.isalnum()]
        while len(ch_list) > 1:
            if ch_list.pop(0) != ch_list.pop():
                return False
        return True


input_str = "A man, a plan, a canal: Panama"
solution = Solution()
answer = solution.isPalindrome(input_str)
print(answer)
