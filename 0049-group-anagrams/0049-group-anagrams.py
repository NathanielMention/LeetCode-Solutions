class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #mapping char's to list of anagrams
        
        for s in strs:
            #count how many char each str has
            count = [0] * 26 # a - z
            #iterate every char and count each char
            for c in s:
                #take aschii val of char - a
                count[ord(c) - ord("a")] += 1
                
            res[tuple(count)].append(s)
            
        return res.values()    