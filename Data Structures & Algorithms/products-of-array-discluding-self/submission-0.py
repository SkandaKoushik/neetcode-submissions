import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            n = nums.copy()
            n.pop(i)
            res.append(math.prod(n))
        
        return res
