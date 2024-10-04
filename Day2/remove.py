from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Retruns the length of the array after removing all instances of val
        """

        k = 0 #This pointer will track the position for elements not equal to val

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i] # Move the non-val element to the front
                k += 1 # Increment k for the next non-val element
        return k

        