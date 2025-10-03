# LeetCode 225 : Implement Stack Using Queues
# Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

# Implement the MyStack class:

# void push(int x) Pushes element x to the top of the stack.
# int pop() Removes the element on the top of the stack and returns it.
# int top() Returns the element on the top of the stack.
# boolean empty() Returns true if the stack is empty, false otherwise.

class MyStack:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))
        x = self.queue1.pop()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return x

    def top(self) -> int:
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))
        x = self.queue1.pop()
        self.queue2.append(x)
        self.queue1, self.queue2 = self.queue2, self.queue1
        return x

    def empty(self) -> bool:
        return not self.queue1 and not self.queue2

