class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) in [0, 1]:
            return [strs]
        
        d = {}

        for s in strs:
            s_sort = ''.join(sorted(s))
            if s_sort in d:
                d[s_sort].append(s)
            else:
                d[s_sort] = [s]
        
        return list(d.values())

            
