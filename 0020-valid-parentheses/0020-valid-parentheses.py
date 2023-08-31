class Solution:
    def isValid(self, s: str) -> bool:
        #map close to open brackets
        Map = {")": "(", "]": "[", "}": "{"}
        #init 
        stack = []
        #loop through char in string
        for c in s:
            # add missing bracket to stack
            if c not in Map:
                stack.append(c)
                continue
            # stack has brackets in it that isnt in map pop
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()

        return not stack
