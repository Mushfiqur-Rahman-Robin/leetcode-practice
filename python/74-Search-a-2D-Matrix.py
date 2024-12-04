class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)

        if m == 0:
            return False
        
        n = len(matrix[0])
        left = 0
        right = m * n - 1

        while left <= right:
            mid = left + (right - left) // 2
            rows = mid // n
            cols = mid % n
            mid_elem = matrix[rows][cols]

            if target == mid_elem:
                return True
            if target > mid_elem:
                left = mid + 1
            if target < mid_elem:
                right = mid - 1
        
        return False
    
# time complexity: O(log(m*n))
# space complexity: O(1)
