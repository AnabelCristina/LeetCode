class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []

        for number in nums:
            index = abs(number) - 1
        
            if nums[index] < 0:
                result.append(abs(number))
            else:
                nums[index] *= -1 

        return result