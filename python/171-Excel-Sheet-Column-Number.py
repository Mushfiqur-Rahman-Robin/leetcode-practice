class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        x = len(columnTitle) - 1
        ans = 0

        for char in columnTitle:
            letter = ord(char) - 64
            ans += letter * (26 ** x)
            x -= 1

        return ans
        

# solution details: https://leetcode.com/problems/excel-sheet-column-number/solutions/4405357/python-explained-solution
# tutorial link: https://www.youtube.com/watch?v=g-l4UpF62x0

# Time complexity:O(n)
# Space complexity: O(1)
