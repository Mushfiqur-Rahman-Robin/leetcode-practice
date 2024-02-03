class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = collections.Counter(s)
        count_t = collections.Counter(t)

        diff = 0 

        for elem in count_s:
            if (count_s[elem]- count_t[elem]) < 0:
                pass
            else:
                diff += count_s[elem]- count_t[elem]
        
        return diff
        
