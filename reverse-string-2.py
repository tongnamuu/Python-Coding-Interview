from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()


input_list = ["H","a","n","n","a","h"]
solution = Solution()
solution.reverseString(input_list)
print(input_list)

