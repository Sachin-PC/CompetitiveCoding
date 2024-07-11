"""

Problem Description
Given an array of integers, every element appears thrice except for one, which occurs once.

Find that element that does not appear thrice.

: Your algorithm should have a linear runtime complexity.

Could you implement it without using extra memory?




Problem Constraints
2 <= A <= 5*106

0 <= A <= INTMAX



Input Format
First and only argument of input contains an integer array A.



Output Format
Return a single integer.



Example Input
Input 1:

 A = [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
Input 2:

 A = [0, 0, 0, 1]


Example Output
Output 1:

 4
Output 2:

 1


Example Explanation
Explanation 1:

 4 occurs exactly once in Input 1.
 1 occurs exactly once in Input 2.


"""

import numpy as np

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bit_one_count_arr = np.zeros(32)
        bit_zero_count_arr = np.zeros(32)
        negative_num_count=0
        for num in nums:
            bit_pos=0
            if num < 0:
                num = abs(num)
                negative_num_count += 1
            while num > 0:
                # print("num = ",num)
                # print("num mode 2  = ",num%2)
                if num%2 == 0:
                    bit_zero_count_arr[bit_pos] = bit_zero_count_arr[bit_pos] + 1
                else:
                    bit_one_count_arr[bit_pos] = bit_one_count_arr[bit_pos] + 1
                num = int(num/2)
                bit_pos += 1

        pw_two_val = 1
        num = 0
        for i in range(32):
            if bit_one_count_arr[i]%3 != 0:
                num += pw_two_val
            pw_two_val = pw_two_val*2

        # print(bit_one_count_arr)
        # print(bit_zero_count_arr)

        if negative_num_count%3 ==0:
            return num
        else:
            return num*-1



