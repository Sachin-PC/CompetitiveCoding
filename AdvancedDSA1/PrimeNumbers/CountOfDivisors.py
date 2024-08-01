"""
Q1. Count of divisors

Problem Description
Given an array of integers A, find and return the count of divisors of each element of the array.

NOTE: The order of the resultant array should be the same as the input array.



Problem Constraints
1 <= length of the array <= 100000
1 <= A[i] <= 106



Input Format
The only argument given is the integer array A.



Output Format
Return the count of divisors of each element of the array in the form of an array.



Example Input
Input 1:

 A = [2, 3, 4, 5]
Input 2:

 A = [8, 9, 10]


Example Output
Output 1:

 [2, 2, 3, 2]
Output 1:

 [4, 3, 4]


Example Explanation
Explanation 1:

 The number of divisors of 2 : [1, 2], 3 : [1, 3], 4 : [1, 2, 4], 5 : [1, 5]
 So the count will be [2, 2, 3, 2].
Explanation 2:

 The number of divisors of 8 : [1, 2, 4, 8], 9 : [1, 3, 9], 10 : [1, 2, 5, 10]
 So the count will be [4, 3, 4].
"""
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        n = len(A)
        max_num = max(A)

        spf = [1]*(max_num+1)

        i = 2
        while i*i <= max_num:
            if spf[i] == 1:
                for k in range(i*i,max_num+1,i):
                    spf[k] = i
            i +=1

        # print("spf = ",spf)
        no_of_divisors = []
        
        for num in A:
            prime_factors = {}
            n = num
            while n > 1:
                pf = spf[n]
                if pf == 1:
                    pf = n
                if pf in prime_factors:
                    prime_factors[pf] += 1
                else:
                    prime_factors[pf] = 1
                n = int(n/pf)
            total_divisors = 1
            # print("num = ",num," prime_factors = ",prime_factors)
            for prime_factor in prime_factors.keys():
                total_divisors *= (prime_factors[prime_factor]+1)
            no_of_divisors.append(total_divisors)

        return no_of_divisors
