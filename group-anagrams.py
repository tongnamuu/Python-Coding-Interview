import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = collections.defaultdict(list)
        for str in strs:
            anagram_dict[tuple(sorted(str))].append(str)
        return list(anagram_dict.values())


input_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
solution = Solution().groupAnagrams(input_list)
print(solution)
