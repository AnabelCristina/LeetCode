class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()

        if (nums[-1] <= 0 or nums[0] > 1):
            return 1

        for i in range(len(nums)):
            if i != 0 and nums[i] > 1:
                if nums[i-1] <= 0 :
                    return 1
                if nums[i] - nums[i-1] > 1:
                    return nums[i-1]+1
        
        return nums[-1] + 1

