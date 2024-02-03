class Solution:
    def minCost(self, colors: str, neededTime) -> int: 
        count = 0

        for index in range(1, len(colors)):
            if colors[index] == colors[index - 1]:
                count += min(neededTime[index], neededTime[index - 1])
                neededTime[index] = max(neededTime[index], neededTime[index - 1])
            
        return count
