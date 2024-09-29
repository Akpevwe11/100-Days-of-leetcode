# Problem 

You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

Merge `nums1` and `nums2` into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array `nums1`. To accommodate this, `nums1` has a length of `m + n`, where the first m elements denote the elements that should be merged, and the last `n` elements are set to 0 and should be ignored. `nums2` has a length of `n`.


## Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.


## Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

## Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.


## Constraints:

    nums1.length == m + n
    nums2.length == n
    0 <= m, n <= 200
    1 <= m + n <= 200
    -10^9 <= nums1[i], nums2[j] <= 10^9


Follow up: Can you come up with an algorithm that runs in O(m + n) time?



# Solution

To merge the two arrays `nums1` and `nums2` into a single sorted array in-place in `nums1`, we can approach the problem by working from the end of the arrays backwards. Since `nums1` has enough space to accommodate the merged result (it has m + n length, with the last n positions initialized to 0), we can avoid shifting elements unnecessarily.

## Approach 

1) Use three pointers:

   - p1 starting from the end of the meaningful part of nums1 (m - 1).
   - p2 starting from the end of nums2 (n - 1).
   - p starting from the end of nums1 (m + n - 1), where the merged result will be placed.

2) Compare elements from the back of nums1 and nums2, and place the larger one at the position p in  nums1.

3) Move the pointers p1, p2, and p accordingly.

4) If there are remaining elements in nums2, copy them to the beginning of nums1. There's no need to  worry about leftover elements in nums1 because they are already in place..


## Explanation:

- We start by comparing the largest elements in nums1 and nums2 (from their end) and place the         larger  one in the correct position in nums1.
-  Once all elements from nums1 or nums2 are placed, if any elements remain in nums2, they are copied to the beginning of nums1.
- This process works efficiently in-place and takes O(m + n) time.


```py

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

```


    Start by comparing nums1[2] (3) and nums2[2] (6). Since 6 > 3, set nums1[5] = 6.
        nums1 becomes [1, 2, 3, 0, 0, 6].

    Compare nums1[2] (3) and nums2[1] (5). Since 5 > 3, set nums1[4] = 5.
        nums1 becomes [1, 2, 3, 0, 5, 6].

    Compare nums1[2] (3) and nums2[0] (2). Since 3 > 2, set nums1[3] = 3.
        nums1 becomes [1, 2, 3, 3, 5, 6].

    Compare nums1[1] (2) and nums2[0] (2). Since 2 == 2, set nums1[2] = 2.
        nums1 becomes [1, 2, 2, 3, 5, 6].

    Compare nums1[0] (1) and nums2[0] (2). Since 2 > 1, set nums1[1] = 2.
        nums1 becomes [1, 2, 2, 3, 5, 6].

    The result is [1, 2, 2, 3, 5, 6].

## Time Complexity:

    The algorithm runs in `O(m + n)` time because we traverse both nums1 and nums2 only once.
    The space complexity is `O(1)` as the merge is done in-place in nums1.

This approach efficiently handles the merge and is optimal for this problem.