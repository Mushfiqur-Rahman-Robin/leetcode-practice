class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        freq_s = Counter(s)
        freq_p = Counter(p) - Counter("*")
    
        for key in freq_p:
            if key not in freq_s or freq_p[key] > freq_s[key]:
                return False
    
        str_to_search = p.split("*")
        str_to_search = [st for st in str_to_search if st]
    
        start = 0
        for st in str_to_search:
            idx = s.find(st, start)
            if idx == -1:
                return False
            start = idx + len(st)
            
        return True

# time complexity: O(n*k)
# space complexity: O(n)
