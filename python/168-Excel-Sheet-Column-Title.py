class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""

        while columnNumber > 0:
            offset = (columnNumber - 1) % 26
            res += chr(ord('A') + offset)
            columnNumber = (columnNumber - 1) // 26

        return res[::-1]

# time complexity: O(log26(n))
# space complexity: O(log26(n))
# tutorial link: https://www.youtube.com/watch?v=X_vJDpCCuoA
