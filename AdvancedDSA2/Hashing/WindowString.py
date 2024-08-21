"""
Q2. Window String
Solved
Asked in:

DI
feature icon
Get your doubts resolved blazing fast with Chat GPT Help
Check Chat GPT
feature icon
Using hints except Complete Solution is Penalty free now
Use Hint
Problem Description
Given a string A and a string B, find the window with minimum length in A, which will contain all the characters in B in linear time complexity.
Note that when the count of a character c in B is x, then the count of c in the minimum window in A should be at least x.

Note:

If there is no such window in A that covers all characters in B, return the empty string.
If there are multiple such windows, return the first occurring minimum window ( with minimum start index and length )


Problem Constraints
1 <= size(A), size(B) <= 106



Input Format
The first argument is a string A.
The second argument is a string B.



Output Format
Return a string denoting the minimum window.



Example Input
Input 1:

 A = "ADOBECODEBANC"
 B = "ABC"
Input 2:

 A = "Aa91b"
 B = "ab"


Example Output
Output 1:

 "BANC"
Output 2:

 "a91b"


Example Explanation
Explanation 1:

 "BANC" is a substring of A which contains all characters of B.
Explanation 2:

 "a91b" is the substring of A which contains all characters of B.
"""
class Solution:
	# @param A : string
	# @param B : string
	# @return a strings
	def minWindow(self, A, B):
        char_freq = {}
        cur_char_freq = {}
        no_of_unique_chars = 0
        for i in range(len(B)):
            char = B[i]
            if char in char_freq:
                char_freq[char] += 1
            else:
                char_freq[char] = 1
                no_of_unique_chars += 1
        
        # print("Number of unique characters = ",no_of_unique_chars)
        # print("char_freq = ",char_freq)
        start_index = 0
        end_index = -1
        total_chars_covered = 0
        best_sub_str_len = len(A) + 1
        best_start_index = -1
        best_end_index = -1
        for i in range(len(A)):
            char = A[i]
            # if i > 250:
            #     print("char[",i,"] = ",char)
            if char in char_freq:
                if char in cur_char_freq:
                    cur_char_freq[char] += 1
                else:
                    cur_char_freq[char] = 1
                if (cur_char_freq[char] - 1) < char_freq[char] and cur_char_freq[char] == char_freq[char]:
                    total_chars_covered += 1
                    if total_chars_covered == no_of_unique_chars:
                        # print("cur_char_freq = ",cur_char_freq)
                        end_index = i
                        sub_str_len = end_index - start_index + 1
                        if sub_str_len < best_sub_str_len:
                            best_sub_str_len = sub_str_len
                            best_start_index = start_index
                            best_end_index = end_index
                        # print("i = ",i)
                        # if i == 276:
                        # print("1.Substring considered = ",A[start_index:start_index+10],"...",A[end_index-10:end_index+1], "total_chars_covered = ",total_chars_covered)
                        
                        while total_chars_covered == no_of_unique_chars:
                            sub_str_len = end_index - start_index + 1
                            if sub_str_len < best_sub_str_len:
                                best_sub_str_len = sub_str_len
                                best_start_index = start_index
                                best_end_index = end_index
                            if A[start_index] in char_freq:
                                cur_char_freq[A[start_index]] -= 1
                                if cur_char_freq[A[start_index]] < char_freq[A[start_index]]:
                                    # print("cur_char_freq[",A[start_index],"] = ",cur_char_freq[A[start_index]]," char_freq[A[start_index]] = ",char_freq[A[start_index]])
                                    total_chars_covered -= 1
                            start_index += 1
                        
                        updated_start_index = start_index
                        
                        # print("2.Substring considered = ",A[start_index:start_index+10],"...",A[end_index-10:end_index+1], "total_chars_covered = ",total_chars_covered)
                        for k in range(start_index, end_index):
                            if A[k] in char_freq:
                                break
                            else:
                                updated_start_index += 1
                        start_index = updated_start_index
                        # print("3.Substring considered = ",A[start_index:start_index+10],"...",A[end_index-10:end_index+1], "total_chars_covered = ",total_chars_covered)
                        # sub_str_len = end_index - start_index + 1
                        # if sub_str_len < best_sub_str_len:
                        #     best_sub_str_len = sub_str_len
                        #     best_start_index = start_index
                        #     best_end_index = end_index


        if end_index == -1:
            return ""
        else:
            return A[best_start_index:best_end_index+1]
