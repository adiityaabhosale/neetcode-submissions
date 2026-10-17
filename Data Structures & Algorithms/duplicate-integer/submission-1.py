class Solution:
    def hasDuplicate(self, nums):
        while len(nums) > 1:
            first = nums.pop(0)
            if first in nums:
                return True
        return False
