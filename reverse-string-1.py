from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1


input_list = ["H","a","n","n","a","h"]
solution = Solution()
solution.reverseString(input_list)
print(input_list)

