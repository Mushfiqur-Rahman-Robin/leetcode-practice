class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == "+":
                a, b = stack.pop(), stack.pop()
                stack.append(a + b)
            elif t == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif t == "*":
                a, b = stack.pop(), stack.pop()
                stack.append(a * b)
            elif t == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(t))
        
        return stack[0]

# tutorial link: https://www.youtube.com/watch?v=iu0082c4HDE
# time complexity: O(n)
# space complexity: O(n)
# check note
