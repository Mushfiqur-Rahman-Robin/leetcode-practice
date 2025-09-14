class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        x_needs = abs(x - z)
        y_needs = abs(y - z)
        
        if x_needs < y_needs: 
            return 1
        elif y_needs < x_needs: 
            return 2
        return 0

# time complexity: O(1)
# space complexity: O(1)
