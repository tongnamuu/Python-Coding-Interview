from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = dict()
        for idx, num in enumerate(nums):
            if num not in nums_dict:
                nums_dict[num] = [idx]
            else:
                nums_dict[num].append(idx)
            value = target - num
            if value in nums_dict:
                if idx != nums_dict[value][0]:
                    return [idx, nums_dict[value][0]]
                elif len(nums_dict[value]) > 1:
                    return [idx, nums_dict[value][1]]
        return [-1, -1]


input_list = [3, 2, 4]
target = 6
solution = Solution().twoSum(input_list, target)
print(solution)
