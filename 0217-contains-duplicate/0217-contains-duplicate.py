class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #init hashset
        hashset = set()

        #loop through input array nums
        for n in nums:
            #if n is in hashet return true
            if n in hashset:
                return True
            #if not in n add to hashset and continue loop    
            hashset.add(n)
        #exit loop    
        return False    

