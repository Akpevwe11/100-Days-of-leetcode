## Steps In Solving a Recursion Problem 

Write a recusive functionthat given an input n sums all nonnegative integers up to n. 

When solving a problem with recursion, use the following steps. 

1. What's the simplest possible input?: 
here the simplest case is `sum(0) -> 0` the simplest case often transforms to a base case for our recursive problem. 

The because of a recursive function is the only input where we provide an explicit answer. all other solution
to the problem will build on the base case. 


2. Visualize the problem.


3. Relate hard cases to simpler cases.

4. Generalize the pattern


Example Walkthrough

Let’s say the input list is [3, 5, 7]. Here’s what happens:

    First Call: list_sum_recursive([3, 5, 7])
        List is not empty, so it returns: 3 + list_sum_recursive([5, 7])

    Second Call: list_sum_recursive([5, 7])
        List is not empty, so it returns: 5 + list_sum_recursive([7])

    Third Call: list_sum_recursive([7])
        List is not empty, so it returns: 7 + list_sum_recursive([])

    Fourth Call: list_sum_recursive([])
        List is empty, so it returns 0.

Now, the recursive calls return their results:

    Third call: 7 + 0 = 7
    Second call: 5 + 7 = 12
    First call: 3 + 12 = 15

So, the sum of the list [3, 5, 7] is 15.
Key Concepts

    Recursion: The function solves the problem by calling itself with a smaller portion of the input list, until it reaches the base case.
    Base Case: The function returns 0 when the list is empty, providing a way for the recursion to stop.
    Decomposition: The function breaks down the problem (summing a list) into smaller sub-problems (summing a smaller list).

This approach is known as divide-and-conquer, where each recursive call reduces the input size until the smallest problem (an empty list) is reached.