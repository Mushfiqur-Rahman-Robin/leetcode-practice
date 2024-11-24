class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        abs_min = float("inf")
        neg_count = 0 
        abs_sum = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] < 0:
                    neg_count += 1

                abs_sum += abs(matrix[i][j])
                abs_min = min(abs_min, abs(matrix[i][j]))

        return abs_sum if neg_count % 2 == 0 else (abs_sum - abs_min * 2) 
        

# tutorial link: https://www.youtube.com/watch?v=XonYlqE049I
# Time Complexity: O(n⋅m), where n is the number of rows and m is the number of columns.
# Space Complexity: O(1), as the algorithm uses constant space.

