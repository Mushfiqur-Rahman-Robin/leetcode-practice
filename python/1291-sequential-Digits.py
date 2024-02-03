class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        queue = deque(range(1, 10))
        
        while queue:
            n = queue.popleft()
            if n > high:
                break
            
            if low <= n <= high:
                res.append(n)

            ones = n % 10 # for example, n = 12, n % 10 = 2, (2 + 1 = 3), (2 * 10 + 3 = 23)
            if ones < 9:
                queue.append(n * 10 + (ones + 1))
        return res


# https://www.youtube.com/watch?v=Q-ca65wRJyI
# Time Complexity O(n)
