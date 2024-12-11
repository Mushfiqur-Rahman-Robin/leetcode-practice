class MinStack:

    def __init__(self):
        self.s = []
        self.minstack = [] # Auxiliary stack to store the minimum values
        

    def push(self, val: int) -> None:
        self.s.append(val)
        if not self.minstack or val <= self.minstack[-1]:
            return self.minstack.append(val)
        

    def pop(self) -> None:
        # If the popped element is the current minimum, remove it from min_stack
        if self.s.pop() == self.minstack[-1]:
            return self.minstack.pop()
        

    def top(self) -> int:
        return self.s[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
    

# tutorial link: https://www.youtube.com/watch?v=RfMroCV17-4
# time complexity: O(1)
# space complexity: O(n)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
