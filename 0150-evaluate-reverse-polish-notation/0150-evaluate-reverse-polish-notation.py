class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        #iterate through char in tokens
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                #
                a, b = stack.pop(), stack.pop()
                #truncate towards zero
                stack.append(int(float(b) / a))
            else:
                #convert appended char to int
                stack.append(int(c))
        return stack[0]
