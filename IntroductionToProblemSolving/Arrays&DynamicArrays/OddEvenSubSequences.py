"""
Q3. Odd Even Subsequences

Given an array of integers A of size, N. Find the longest subsequence of A, which is odd-even.

A subsequence is said to be odd-even in the following cases:

The first element of the subsequence is odd; the second element is even, the third element is odd, and so on. For example: [5, 10, 5, 2, 1, 4], [1, 2, 3, 4, 5]

The first element of the subsequence is even, the second element is odd, the third element is even, and so on. For example: [10, 5, 2, 1, 4, 7], [10, 1, 2, 3, 4]

Return the maximum possible length of odd-even subsequence.

Note: An array B is a subsequence of an array A if B can be obtained from A by deleting several (possibly, zero, or all) elements.


Input Format

The only argument given is the integer array A.
Output Format

Return the maximum possible length of odd-even subsequence.
Constraints

1 <= N <= 100000
1 <= A[i] <= 10^9 
For Example

Input 1:
    A = [1, 2, 2, 5, 6]
Output 1:
    4
    Explanation 1:
        Maximum length odd even subsequence is [1, 2, 5, 6]

Input 2:
    A = [2, 2, 2, 2, 2, 2]
Output 2:
    1
    Explanation 2:
        Maximum length odd even subsequence is [2]
"""

def get_subsequence_length(A,check_even):
    subsequence_length = 0
    for i in range(len(A)):
            if check_even:
                if A[i]%2 == 0:
                    subsequence_length += 1
                    check_even = False
            else:
                if A[i]%2 == 1:
                    subsequence_length += 1
                    check_even = True
    return subsequence_length


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # get the subsequence starting with odd number
        check_even = False
        odd_subseq_len = get_subsequence_length(A,check_even)

        # get the subsequence starting with even number
        check_even = True
        even_subseq_len = get_subsequence_length(A,check_even)

        if odd_subseq_len>even_subseq_len:
            return odd_subseq_len
        else:
            return even_subseq_len
            

