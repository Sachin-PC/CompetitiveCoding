"""
Q3. Min Stack
Solved

Problem Description

Design a stack that supports push, pop, top, and retrieve the minimum element in constant time.
push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
NOTE:
All the operations have to be constant time operations.
getMin() should return -1 if the stack is empty.
pop() should return nothing if the stack is empty.
top() should return -1 if the stack is empty.
Problem Constraints

1 <= Number of Function calls <= 107
Input Format

Functions will be called by the checker code automatically.
Output Format

Each function should return the values as defined by the problem statement.
Example Input

Input 1:
push(1)
push(2)
push(-2)
getMin()
pop()
getMin()
top()
Input 2:
getMin()
pop()
top()
Example Output

Output 1:
 -2 1 2
Output 2:
 -1 -1
Example Explanation

Explanation 1:
Let the initial stack be : []
1) push(1) : [1]
2) push(2) : [1, 2]
3) push(-2) : [1, 2, -2]
4) getMin() : Returns -2 as the minimum element in the stack is -2.
5) pop() : Return -2 as -2 is the topmost element in the stack.
6) getMin() : Returns 1 as the minimum element in stack is 1.
7) top() : Return 2 as 2 is the topmost element in the stack.
Explanation 2:
Let the initial stack be : []
1) getMin() : Returns -1 as the stack is empty.
2) pop() :  Returns nothing as the stack is empty.
3) top() : Returns -1 as the stack is empty.
"""
class MinStack:
    
    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.num_stack.append(x)
        if self.min_stack:
            self.min_stack.append(min(x,self.min_stack[-1]))
        else:
            self.min_stack.append(x)

    # @return nothing
    def pop(self):
        if self.num_stack:
            self.min_stack.pop()
            return self.num_stack.pop()
        else:
            return

    # @return an integer
    def top(self):
        if self.num_stack:
            return self.num_stack[-1]
        else:
            return -1
        

    # @return an integer
    def getMin(self):
        if self.num_stack:
            return self.min_stack[-1]
        else:
            return -1
        
    
    def __init__(self):
        self.num_stack = []
        self.min_stack = []