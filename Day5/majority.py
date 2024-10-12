from types import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None # Initialize the candidate to None
        count = 0

        # Boyer-Moore Voting Algorithm
        for num in nums:
            if count == 0:
                candidate = num # Set the candidate to the current number
            count += 1 if num == candidate else -1

        return candidate

        