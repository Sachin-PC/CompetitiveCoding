"""
Q2. Min XOR value

Problem Description
Given an integer array A of N integers, find the pair of integers in the array which have minimum XOR value. Report the minimum XOR value.



Problem Constraints
2 <= length of the array <= 100000
0 <= A[i] <= 109



Input Format
First and only argument of input contains an integer array A.



Output Format
Return a single integer denoting minimum xor value.



Example Input
Input 1:

 A = [0, 2, 5, 7]
Input 2:

 A = [0, 4, 7, 9]


Example Output
Output 1:

 2
Output 2:

 3


Example Explanation
Explanation 1:

 0 xor 2 = 2
"""

def check_min_val(A,checked_bit_pos,cur_bit_pos,check_number,n):
    if cur_bit_pos == -1:
        return 0

    count_ones = 0
    count_zeros = 0
    res = 0
    ones_check_number = 0
    zeros_check_number = 0
    for j in range(n):
        if cur_bit_pos == 31 or (A[j] >=0 and ((A[j]>>checked_bit_pos) == check_number)):
            new_check_number = A[j] >> cur_bit_pos
            if ( (A[j] >> cur_bit_pos) & 1 ) == 1:
                count_ones += 1
                ones_check_number = new_check_number
            else:
                count_zeros += 1
                zeros_check_number = new_check_number
    # if cur_bit_pos <= 3:
        # print("bit_pos = ",cur_bit_pos)
        # print("count_ones = ",count_ones)
        # print("count_zeros = ",count_zeros)
    if count_ones < 2 and count_zeros <2:
        # print("1")
        res += 2**cur_bit_pos
        res += check_min_val(A,checked_bit_pos,cur_bit_pos-1,check_number,n)
    elif count_ones >= 2 and count_zeros <2:
        # print("2")
        checked_bit_pos = cur_bit_pos
        check_bit = 1
        res += check_min_val(A,checked_bit_pos,cur_bit_pos-1,ones_check_number,n)
    elif count_ones < 2 and count_zeros >= 2:
        # print("3")
        checked_bit_pos = cur_bit_pos
        check_bit = 0
        res += check_min_val(A,checked_bit_pos,cur_bit_pos-1,zeros_check_number,n)
    else:
        # print("4")
        checked_bit_pos = cur_bit_pos
        check_bit = 0
        res += check_min_val(A,checked_bit_pos,cur_bit_pos-1,zeros_check_number,n)
        check_bit = 1
        res += check_min_val(A,checked_bit_pos,cur_bit_pos-1,ones_check_number,n)

    return res

class Solution:
	# @param A : list of integers
	# @return an integer
	def findMinXor(self, A):
        n = len(A)
        checked_bit_pos = -1
        cur_bit_pos = 31
        check_number = 0
        res = check_min_val(A,checked_bit_pos,cur_bit_pos,check_number,n)
        
        return res