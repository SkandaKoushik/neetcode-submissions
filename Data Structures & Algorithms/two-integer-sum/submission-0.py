class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            if target - n in nums[i+1:]:
                j = nums[i+1:].index(target - n)
                return [i, j+i+1]
        
        return []