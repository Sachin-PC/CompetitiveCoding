"""
Q2. Lucky Numbers

Problem Description
A lucky number is a number that has exactly 2 distinct prime divisors.

You are given a number A, and you need to determine the count of lucky numbers between the range 1 to A (both inclusive).



Problem Constraints
1 <= A <= 50000



Input Format
The first and only argument is an integer A.



Output Format
Return an integer i.e the count of lucky numbers between 1 and A, both inclusive.



Example Input
Input 1:

 A = 8
Input 2:

 A = 12


Example Output
Output 1:

 1
Output 2:

 3


Example Explanation
Explanation 1:

 Between [1, 8] there is only 1 lucky number i.e 6.
 6 has 2 distinct prime factors i.e 2 and 3.
Explanation 2:

 Between [1, 12] there are 3 lucky number: 6, 10 and 12.
"""
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

        spf = [1]*(A+1)

        i = 2
        while i*i <= A:
            if spf[i] == 1:
                for k in range(i*i,A+1,i):
                    spf[k] = i

            i += 1

        no_of_lucky_nums = 0

        for i in range(2,A+1):
            n = i
            distinct_primes = set()

            while n > 1:
                prime_divisor = spf[n]
                if prime_divisor == 1:
                    prime_divisor = n
                if prime_divisor not in distinct_primes:
                    distinct_primes.add(prime_divisor)
                n = int(n/prime_divisor)
            
            if len(distinct_primes) == 2:
                no_of_lucky_nums += 1

        return no_of_lucky_nums