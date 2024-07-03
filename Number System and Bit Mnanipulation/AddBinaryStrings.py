"""
Problem Description
Given two binary strings A and B. Return their sum (also a binary string).


Problem Constraints
1 <= length of A <= 105

1 <= length of B <= 105

A and B are binary strings



Input Format
The two argument A and B are binary strings.



Output Format
Return a binary string denoting the sum of A and B



Example Input
Input 1:
A = "100"
B = "11"
Input 2:
A = "110"
B = "10"


Example Output
Output 1:
"111"
Output 2:
"1000"


Example Explanation
For Input 1:
The sum of 100 and 11 is 111.
For Input 2:
 
The sum of 110 and 10 is 1000.

"""

import numpy as np

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        bits_sum_arr = np.zeros(32, dtype=int)
        sum_arr = ''
        carry = 0
        a_bit = 0
        b_bit=0
        index = 31
        a_len = len(a)
        b_len = len(b)
        a_index = len(a)-1
        b_index = len(b)-1
        while a_index>=0 or b_index>=0:
            if a_index >=0:
                a_bit = int(a[a_index])
            else:
                a_bit = 0
            if b_index >=0:
                b_bit = int(b[b_index])
            else:
                b_bit = 0
            bit_sum = a_bit + b_bit + carry
            bits_sum_arr[index] = bit_sum%2
            carry = int(bit_sum/2)
            a_index -= 1
            b_index -= 1
            sum_arr = sum_arr+str(bit_sum%2)
            # print("bit_sum%2 = ",bit_sum%2)
            # print("chr(bit_sum%2) = ",str(bit_sum%2))
            # print("sum_arr = ",sum_arr)
        if carry != 0:
            bits_sum_arr[index] = carry
            sum_arr = sum_arr + str(carry)

        # print("sum_arr = ",sum_arr)
        return sum_arr[::-1]