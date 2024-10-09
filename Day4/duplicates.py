from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Returns the length of the array after removing duplicates
        """

        if len(nums) <= 0:   ## If the length of nums is less than 3, all elements are allowed
            return len(nums)
        
        j = 2 # start from the third element since the first two elements are allowed to be duplicates
        for i in range(2, len(nums)):
            if nums[i] > nums[j - 2]:
                nums[j] = nums[i]
                j += 1

        return j

        
        