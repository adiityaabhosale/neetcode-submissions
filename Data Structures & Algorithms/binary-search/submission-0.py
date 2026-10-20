class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            guess = nums[mid]
            
            if guess == target:
                return mid       # Found it!
            
            if guess < target:
                left = mid + 1   # Too low, look right
            else:
                right = mid - 1  # Too high, look left
                
        return -1  # Looked everywhere, it's not here
