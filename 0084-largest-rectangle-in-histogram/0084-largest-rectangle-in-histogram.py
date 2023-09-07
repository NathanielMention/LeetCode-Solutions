class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0 #keep track of area
        stack = []  # pair: (index, height)
        #iterate through rectangle heights
        for i, h in enumerate(heights):
            start = i
            #if stack isnt empty and if top value in stack and top val height > cur h 
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                # i - index = width
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea
