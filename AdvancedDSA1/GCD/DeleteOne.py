"""
Q1. Delete one
Problem Description
Given an integer array A of size N. You have to delete one element such that the GCD(Greatest common divisor) of the remaining array is maximum.

Find the maximum value of GCD.



Problem Constraints
2 <= N <= 105
1 <= A[i] <= 109



Input Format
First argument is an integer array A.



Output Format
Return an integer denoting the maximum value of GCD.



Example Input
Input 1:

 A = [12, 15, 18]
Input 2:

 A = [5, 15, 30]


Example Output
Output 1:

 6
Output 2:

 15


Example Explanation
Explanation 1:

 If you delete 12, gcd will be 3.
 If you delete 15, gcd will be 6.
 If you delete 18, gcd will 3.
 Maximum value of gcd is 6.
Explanation 2:

 If you delete 5, gcd will be 15.
 If you delete 15, gcd will be 5.
 If you delete 30, gcd will be 5.
 Maximum value of gcd is 15.
"""
def get_gcd(a,b):
    if a ==0 or b == 0:
        return a+b
    else:
        if a >= b:
            return get_gcd(a%b,b)
        else:
            return get_gcd(b%a,a)

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        prefix_gcd_array = []
        suffix_gcd_array = []
        n = len(A)
        prefix_gcd_array.append(A[0])
        suffix_gcd_array = [0]*n
        suffix_gcd_array[n-1] = A[n-1]
        for i in range(1,n):
            gcd_val = get_gcd(prefix_gcd_array[i-1],A[i])
            prefix_gcd_array.append(gcd_val)
            suffix_array_index = n - i
            gcd_val = get_gcd(suffix_gcd_array[suffix_array_index],A[suffix_array_index-1])
            suffix_gcd_array[suffix_array_index-1] = gcd_val

        # print("prefix_gcd_array = ",prefix_gcd_array)
        # print("suffix_gcd_array = ",suffix_gcd_array)

        max_gcd = suffix_gcd_array[1]
        for i in range(1,n):
            if i == n-1:
                gcd_val = prefix_gcd_array[i-1]
            else:
                gcd_val = get_gcd(prefix_gcd_array[i-1],suffix_gcd_array[i+1])
            if gcd_val > max_gcd:
                max_gcd = gcd_val

        return max_gcd