"""
2. Sub-matrix Sum Queries

Problem Description
Given a matrix of integers A of size N x M and multiple queries Q, for each query, find and return the submatrix sum.

Inputs to queries are top left (b, c) and bottom right (d, e) indexes of submatrix whose sum is to find out.

NOTE:

Rows are numbered from top to bottom, and columns are numbered from left to right.
The sum may be large, so return the answer mod 109 + 7.
Also, select the data type carefully, if you want to store the addition of some elements.
Indexing given in B, C, D, and E arrays is 1-based.
Top Left 0-based index = (B[i] - 1, C[i] - 1)
Bottom Right 0-based index = (D[i] - 1, E[i] - 1)


Problem Constraints
1 <= N, M <= 1000
-100000 <= A[i] <= 100000
1 <= Q <= 100000
1 <= B[i] <= D[i] <= N
1 <= C[i] <= E[i] <= M



Input Format
The first argument given is the integer matrix A.
The second argument given is the integer array B.
The third argument given is the integer array C.
The fourth argument given is the integer array D.
The fifth argument given is the integer array E.
(B[i], C[i]) represents the top left corner of the i'th query.
(D[i], E[i]) represents the bottom right corner of the i'th query.



Output Format
Return an integer array containing the submatrix sum for each query.



Example Input
Input 1:

 A = [   [1, 2, 3]
         [4, 5, 6]
         [7, 8, 9]   ]
 B = [1, 2]
 C = [1, 2]
 D = [2, 3]
 E = [2, 3]
Input 2:

 A = [   [5, 17, 100, 11]
         [0, 0,  2,   8]    ]
 B = [1, 1]
 C = [1, 4]
 D = [2, 2]
 E = [2, 4]


Example Output
Output 1:

 [12, 28]
Output 2:

 [22, 19]


Example Explanation
Explanation 1:

 For query 1: Submatrix contains elements: 1, 2, 4 and 5. So, their sum is 12.
 For query 2: Submatrix contains elements: 5, 6, 8 and 9. So, their sum is 28.
Explanation 2:

 For query 1: Submatrix contains elements: 5, 17, 0 and 0. So, their sum is 22.
 For query 2: Submatrix contains elements: 11 and 8. So, their sum is 19.
 
"""

class Solution:
    # @param A : list of list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @param D : list of integers
    # @param E : list of integers
    # @return a list of integers
    def solve(self, A, B, C, D, E):
        n = len(A)
        m = len(A[0])
        mod_val = 10**9 + 7


        #Setting the first column values
        for i in range(1,n):
            A[i][0] = (A[i-1][0] + A[i][0])%mod_val

        #Setting the first row values
        for j in range(1,m):
            A[0][j] = (A[0][j-1] + A[0][j])%mod_val 


        for i in range(1,n):
            for j in range(1,m):
                # print("i = ",i," j = ",j)
                A[i][j] = (((A[i][j-1] + A[i-1][j])%mod_val - A[i-1][j-1])%mod_val + A[i][j])%mod_val

        num_queries = len(B)

        # print("A = ",A)
        query_submat_sums = []
        for q in range(num_queries):
            # print("q = ",q)
            i,j,x,y = B[q]-1,C[q]-1,D[q]-1,E[q]-1
            # print("i = ",i,"j = ",j," x = ",x,"y = ",y)
            submat_sum = A[x][y]
            rx1, ry1 = i-1, y
            rx2, ry2 = x, j-1
            ax1, ay1 = i-1, j-1
            # print("rx1 = ",rx1,"ry1 = ",ry1)
            # print("rx2 = ",rx2,"ry2 = ",ry2)
            # print("ax1 = ",ax1,"ay1 = ",ay1)
            if rx1 >= 0:
                submat_sum = (submat_sum -A[rx1][ry1])%mod_val
            if ry2 >= 0:
                submat_sum = (submat_sum - A[rx2][ry2])%mod_val
            if ax1 >=0 and ay1 >=0:
                submat_sum = (submat_sum + A[ax1][ay1])%mod_val
            
            query_submat_sums.append(submat_sum)

        return query_submat_sums