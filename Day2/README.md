## 27. Remove Element

 Given an integer array `nums` and an integer `val`, remove all occurrences of val in `nums` in-place. The order of the elements may be changed. Then return the number of elements in `nums` which are not equal to val.

Consider the number of elements in `nums` which are not equal to `val` be `k`, to get accepted, you need to do the following things:

    Change the array `nums` such that the first `k` elements of `nums` contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.

    Return k.


Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}

If all assertions pass, then your solution will be accepted.


## Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

## Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).

 

Constraints:

    0 <= nums.length <= 100
    0 <= nums[i] <= 50
    0 <= val <= 100


## Solution 

To solve this problem, the approach involves modifying the array `nums` in-place, moving elements 
that are not equal to `val` to the front of the array, and returning the count of those elements (
    let's call it `k`). We need to ensure that the first `k` elements are the ones not equal to `val`, 
and the remaining elements of the arrayy don't matter.

## Approach: 

1. Pointer Approach: 
    - Use two pointers: one pointer `(i)` to iterate through the array, and another pointer `(k)` to 
    keep track of where the next element (that is not equal to `val`) should be placed. 

2. Iteration:
    - Traverse the array using pointer `i`.
    - Every time you encounter an lement that is not equaul to `val`, assign it to the `k`-th position of the array and increment `k`. 

3. Return `k`:
    - After the loop finishes, `k` will represent the number of lements in `nums` that are not equal to `val`, and the first `k` elements will be those elements. 


    ## Explanation: 

    - We initialize `k` to 0. 
    - We loop through the array `nums`. For each element nums[i]:
        - If nums[i] is not equal to `val`, we copy it to the `k`-thh position and increment `k`.
    - After the loops ends, `k` will hold the number of elements in `nums` that are not equal to `val`.

    ## Example Walkthrough

    ```py
            nums = [3, 2, 2, 3]
            val = 3
    ```

    - initially, `k = 0`.
    - At `i = 0`, `nums[0] == 3`, so we skip it. 
    - At  `i = 1`, `nums[1] == 2`, so we set `nums[k] = nums[1]` -> `nums[0] = 2` and increment `k` to 1.
    - At `i = 2`, `nums[2] == 2`, so we set `nums[k] = nums[2]` -> `nums[1] = 2` and increment `k` to 2.
    - At `i = 3`, `nums[3] == 3`, so we skip it. 
    - Final `nums = [2, 2, _, _], and `k = 2`.


    ## Example 2:

     ```py

        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2

     ``` 

      - Iniially, `k = 0`. 
      - At `i = 0`, `nums[0] == 0`, se we set `nums[k] = nums[0]` -> `nums[0] = 0` and increment `k` to 1.
      - At `i = 1`, nums[1] == 1, so we set `nums[k] = nums[1]` -> `nums[1] = 1` and increment `k to 2`.
      - At `i = 2`, `nums[2] == 2`, so we skip it. 
      - At `i = 3`, `nums[3] == 2` so we skip it.
      - At  `i = 4`, `nums[4] == 3`, so we set `nums[k] = nums[4]` -> `nums[4] -> nums[2] = 3` and increment `k` to 3. 

      - At `i = 5`, `nums[5] == 0`, so we set `nums[k] = nums[5]` -> `nums[3] = 0` and increment `k` to 4.

      - At `i = 6`, `nums[6] == 4`, so we set `nums[k] = nums[6]` → `nums[4] = 4` and increment `k` to 5.
      - At `i = 7`, `nums[7] == 2`, so we skip it.
      - Final `nums = [0, 1, 3, 0, 4, _, _, _]`, and `k = 5`.




    ## Time Complexity: 

    - O(n) where `n` is the length of `nums` because we only iterate through the array once. 

    ## Space Complexity: 

    - O(1)  since we do the operation in-place without needing any additional memory. 



