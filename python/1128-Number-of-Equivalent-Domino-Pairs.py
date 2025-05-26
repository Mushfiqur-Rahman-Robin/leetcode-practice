class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count_pairs = 0
        count_dict = defaultdict(int)

        for a, b in dominoes:
            key = (min(a, b), max(a, b))
            count_pairs += count_dict[key] 
            count_dict[key] += 1
        
        return count_pairs
  
# Time complexity: O(n)
# Space	complexity: O(n)
