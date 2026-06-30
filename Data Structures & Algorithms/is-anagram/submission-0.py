class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_sort = ''.join(sorted(list(s)))
        t_sort = ''.join(sorted(list(t)))

        if s_sort == t_sort:
            return True
        else:
            return False