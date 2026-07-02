class Solution:

    def encode(self, strs: List[str]) -> str:
        for i, s in enumerate(strs):
            if s == '':
                strs[i] = '-*-'

        return '_#_'.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == '':
            return []
            
        strs = s.split('_#_')
        for i, s in enumerate(strs):
            if s == '-*-':
                strs[i] = ''

        return strs

