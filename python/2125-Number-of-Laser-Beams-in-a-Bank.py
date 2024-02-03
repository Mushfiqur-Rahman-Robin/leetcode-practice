class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = 0
        res = 0 

        for string in bank:
            current = string.count('1')
            if current:
                res += prev * current
                prev = current

        return res
        
# Time complexity: O(m * n)
# space complexity: O(1)
