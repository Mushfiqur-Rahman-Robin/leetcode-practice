class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start = 1, current = []):
            if len(current) == k:
                output.append(current[:])
                return

            for i in range(start, n + 1):
                current.append(i)
                backtrack(i + 1, current)
                current.pop()

        output = []
        backtrack()
        return output
