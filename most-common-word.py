from typing import List
import re
from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        fixed_paragraph = re.sub(r'[^\w]', ' ', paragraph).lower().split()
        word_list = Counter([word for word in fixed_paragraph if word not in banned])
        return word_list.most_common(1)[0][0]


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
solution = Solution().mostCommonWord(paragraph, banned)
print(solution)
