from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        nums_dict = {}
        for idx, i in enumerate(nums):
            if i in nums_dict:
                nums_dict[i].append(idx)
            else:
                nums_dict[i] = [idx]
        ans = []
        prev1 = 0
        for i in range(len(nums)):
            if i > 0 and nums[i] == prev1:
                continue
            prev1 = nums[i]
            for j in range(i+1, len(nums)):
                target = -nums[i]-nums[j]
                if target in nums_dict:
                    for k in nums_dict[target]:
                        if k != i and k != j:
                            ans.append(tuple(sorted([nums[i], nums[j], -nums[i]-nums[j]])))
                            break
        ans = list(set(ans))
        for idx in range(len(ans)):
            ans[idx] = list(ans[idx])
        return ans


input_list = [-1, 0, 1, 2, -1, -4]
solution = Solution().threeSum(input_list)
print(solution)
