class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #init hashmap
        prevMap = {}  # val -> index
        #iterate through array
        for i, n in enumerate(nums):
            diff = target - n
            #if we find solution return
            if diff in prevMap:
                return [prevMap[diff], i]
            #update hashmap
            prevMap[n] = i