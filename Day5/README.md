##  Majority Element


Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

 

Constraints:

    n == nums.length
    1 <= n <= 5 * 104
    -109 <= nums[i] <= 109

## Solution 

To solve the Majority Element problem, we need to find the element in the array that appears more than n /2times, where `n` is the size of the array. One efficient approach to solve this problem is 
**Boyer-Moore Voting Algotithem** which operates on `O(n)` time and `O(1)` space.

### Steps for the Boyer-Moore Voting Algorithm:

1. We maintain two variables: 

- candidate -- The current majority candidate. 
- count -- the count of the candidate.

2. We traverse through the array: 

- If `count` is 0, we assign the current element as the new candidate.
- If the current element is the same as `candidate`, we increment `count`.
- Otherwise, we decrement `count`.

3. After completing the loop, the `candidate` will be the majoroity element.

### Example walkthrough

For nums = `[2, 2, 1, 1, 1, 2, 2]`
- Initially: `candiate = None`, `count = 0`.
- Process each element: 
    - First `2`: `candidate = 2`, count = 1.
    - Second `2`: `candidate = 2`, count = 2. 
    - First `1`: `count = 1` (decrement since 1 != 2).
    - Second `1`: `count = 0`.
    - Third `1`: `candidate = 1`, count = 1.
    - Fourth `2`: `count = 0`.
    - Fifth `2`: `candidate = 2`, `count = 1`.

-- The result isi 2.

## Time and Space Complexity: 

- Time complexity: O(n), where `n` is the length of the array. 
- Space complexity: O(1), because we use only a constant amount of extra space.

- The catch is one majority element is there more than N/2 times.
