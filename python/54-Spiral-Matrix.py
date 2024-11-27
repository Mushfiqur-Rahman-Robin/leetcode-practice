class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left = 0
        top = 0
        right = len(matrix[0])
        bottom = len(matrix)

        while left < right and top < bottom:
            for i in range(left, right): # every top row elems
                res.append(matrix[top][i])
            top += 1
            
            for i in range(top, bottom): # every right row elems
                res.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break

            for i in range(right - 1, left - 1, -1): # every bottom row elems
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            for i in range(bottom - 1, top - 1, -1): # every left row elems
                res.append(matrix[i][left])
            left += 1

        return res

# tutorial link: https://www.youtube.com/watch?v=BJnMZNwUk1M
# time complexity: O(m×n)
# space complexity: O(1) (excluding the result list) or O(m×n) (including the result list).
 



        
