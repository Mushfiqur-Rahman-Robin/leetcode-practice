class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_points = []
        for p in points:
            x_points.append(p[0])
        x_points = sorted(x_points)
        # print(x_points)

        ans = 0
        for i in range(1, len(x_points)):
            ans = max(ans,(x_points[i]-x_points[i-1]))
        return ans
        
        
