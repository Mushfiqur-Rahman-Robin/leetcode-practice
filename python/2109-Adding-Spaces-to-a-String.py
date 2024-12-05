class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        prev = 0

        for i in spaces:
            res.append(s[prev:i])
            prev = i
        
        res.append(s[i:])
        
        return " ".join(res)

# check note
# time complexity: O(l+m)
# space complexity: O(l+m)
# Where:
# L is the length of the string s.
# M is the length of the spaces list.
        
