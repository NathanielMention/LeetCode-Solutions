class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #init 2 pointers
        l, r = 0, len(numbers) - 1
        
        while l < r:
            #current sum = current position left and right pointer
            curSum = numbers[l] + numbers[r]
            #move pointers
            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
                