from typing import List


def list_sum(a_list: List[int]) -> int:
    result = 0
    for val in a_list:
        result += val 
    return result

"""
The first thing  the function checks is if the list is empty by evaluating len(a_list) == 0. 
Reason: In recursion, you need a base case to prevent the function from calling itself indefinitely. 
The base case handles the situation where there are no more elements left to sum. 

If the list is empty, the function returns 0. This acts as the stopping point for the recursion. 

Rercursive case  

If the list is not empty, the function takes the first element of the list and adds it to the result 
of a recursive call to list_sum_recursive(a_list[1:]).

The function calls itself with the rest of the list, and this process repeats until the lis becomes empty.
(base case), where it returns 0.

Explanation of the Recursive case 

return a_list[0] + list_sum_recursive(a_list[1:])

Explanation: If the list is not empty, the function takes the first element of the list (a_list[0])
and adds it to the result of a recusive call to list_sum_recursive(a_list[1:]).

What's Happening?:

- a_list[0]: This is the first element of the list. 

- a_list[1:]: This is the rest of the list(from the second element onward).

- The function calls itself with the rest of the list, and this process repeats until the list becomes empty(base case),
where it returns 0.


Key Concepts

RECURSION: The function solves the problem by calling itself with a smaller portion of the input list, 
until it reaches the base case.

BASE CASE: The function returns 0 when the list is empty, providing a way for the recusion to stop.

DECOMPOSITION: The function breakes down the problem (summing a list) into smaller sub-problems (summing a smaller list).

This approach is known as divide and conquer, where each recursive call reduces the input size until the smallest problem (an empty list) is reached.


"""


def list_sum_recursive(a_list: List[int]) -> int:
    if len(a_list) == 0:
        return 0
    return a_list[0] + list_sum_recursive(a_list[1:])


assert list_sum([2, 3, 5, 7]) == 17
assert list_sum_recursive([2, 3, 5, 7]) == 17

print(list_sum_recursive([2, 3, 5, 7]))  # 17