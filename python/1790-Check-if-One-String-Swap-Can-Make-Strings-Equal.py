class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        
        mismatches = [(a, b) for a, b in zip(s1, s2) if a != b]
        
        return len(mismatches) == 2 and (mismatches[0] == mismatches[1][::-1])

        
# time complexity: O(n)
# space complexity: O(1)
