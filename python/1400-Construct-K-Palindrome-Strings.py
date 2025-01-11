class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        odd_count = 0
        for nums in Counter(s).values():
            if nums % 2 == 1:
                odd_count += 1
        
        return odd_count <= k


# tutorial lonk: https://www.youtube.com/watch?v=D00qGvqmqN0
# time complexity: O(n)
# space complexity: O(26)
