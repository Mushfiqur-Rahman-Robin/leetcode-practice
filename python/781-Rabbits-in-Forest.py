class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ans = 0
        rabbit_count = defaultdict(int)

        for val in answers:
            if rabbit_count[val] > val:
                rabbit_count[val] = 0
            if not rabbit_count[val]:
                ans += val + 1
            rabbit_count[val] += 1
        
        return ans
        

# Time complexity: O(n)
# Space complexity: O(n)
# check note
