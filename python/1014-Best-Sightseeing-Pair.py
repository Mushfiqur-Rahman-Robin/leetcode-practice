class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_score = float('-inf')
        i = 0
        j = 1

        while j < len(values):
            max_score = max(max_score, values[i] + values[j] + i - j)
            
            if values[j] + j > values[i] + i:
                i = j

            j +=1 

        return max_score

# time complexity: O(n)
# space complexity: O(1)
# check note
        
