class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        length = len(nums)

        for i in range(length):
            cur = nums[i]
            reminder = target - cur
            if reminder in nums[i+1:]:
                return i, nums.index(reminder, i+1)
                break



solution = Solution()
solution.twoSum()

# Testcase

# [2,7,11,15]
# 9 

# [3,2,4]
# 6

# [3,3]
# 6
