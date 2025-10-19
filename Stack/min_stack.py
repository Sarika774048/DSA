# LeetCode 155 - Min Stack

# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.
# Example 1:
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = None
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.mini = val
        else:
            if val > self.mini: self.stack.append(val)
            else:
                self.stack.append(2*val - self.mini)
                self.mini = val

    def pop(self) -> None:
        if not self.stack: return
        else:
            x = self.stack.pop()
            if x < self.mini:
                self.mini = 2* self.mini - x
                
        

    def top(self) -> int:
        if not self.stack: return -1
        x = self.stack[-1]
        if self.mini < x: return x
        return self.mini


    def getMin(self) -> int:
        return self.mini
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
