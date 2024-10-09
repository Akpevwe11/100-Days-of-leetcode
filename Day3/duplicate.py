from types import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Returns the length of the array after removing duplicates
        """

        if len(nums) == 0:
            return 0

        k = 0   # This pointer will track the position for unique elements

        for i in range(1, len(nums)):
            if nums[i] != nums[k]: # If the current element is not equal to the previous element
                k += 1  # Increment k
                nums[k] = nums[i] # Move the unique element to the front

        return k + 1