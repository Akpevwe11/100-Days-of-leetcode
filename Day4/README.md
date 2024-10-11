## Example

Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

## Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}

If all assertions pass, then your solution will be accepted.

 

## Example 1:

Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

## Example 2:

Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

 

## Constraints:

    1 <= nums.length <= 3 * 104
    -104 <= nums[i] <= 104
    nums is sorted in non-decreasing order.

# Solution 

## Explanation 

1. Base Case: if `nums` has fewer than 3 elements, return the length as all elements are valid. 

2. Iterate and Compare: We start from index `2`, as the first two elements are always allowed to stay. For every element `nums[i]`, check if it's greater than `nums[j-2]`. 
if it is, we place it at nums[j] and increment `j`.

3. In-Place Modfitication: The array is modified in place by overwriting elements that appear more than twice with valid elements. 

4. Result: After the loop, `j` will be the new length hof the array with duplicates removed.

Example Walkthrough:

For nums = [1,1,1,2,2,3]:

    Start with j = 2.
    i = 2, nums[2] = 1 is not greater than nums[0] = 1, so it's skipped.
    i = 3, nums[3] = 2 is greater than nums[1] = 1, so nums[2] = 2 and j = 3.
    i = 4, nums[4] = 2 is greater than nums[2] = 1, so nums[3] = 2 and j = 4.
    i = 5, nums[5] = 3 is greater than nums[3] = 2, so nums[4] = 3 and j = 5.

The final array will be [1,1,2,2,3,_], and the function returns 5.

For nums = [0,0,1,1,1,1,2,3,3]:

    Start with j = 2.
    i = 2, nums[2] = 1 is greater than nums[0] = 0, so nums[2] = 1 and j = 3.
    i = 3, nums[3] = 1 is greater than nums[1] = 0, so nums[3] = 1 and j = 4.
    i = 4, nums[4] = 1 is not greater than nums[2] = 1, so it's skipped.
    i = 5, nums[5] = 1 is not greater than nums[3] = 1, so it's skipped.
    i = 6, nums[6] = 2 is greater than nums[4] = 1, so nums[4] = 2 and j = 5.
    i = 7, nums[7] = 3 is greater than nums[5] = 2, so nums[5] = 3 and j = 6.
    i = 8, nums[8] = 3 is greater than nums[6] = 2, so nums[6] = 3 and j = 7.

The final array will be [0,0,1,1,2,3,3,_,_], and the function returns 7.

## Time Complexity:

    O(n) where n is the length of nums. We iterate through the array once.


## Space Complexity:

    O(1) as we are modifying the array in-place and not using any extra space.


## Key Points:

    We only modify the array when we find a valid element that should be kept.
    The approach works in O(n) time, where n is the length of the array, because we make only one pass through the array.
    The solution uses O(1) extra space because we don't use any additional arrays or data structures; we modify the array in-place.

Let me know if you need any further clarification!