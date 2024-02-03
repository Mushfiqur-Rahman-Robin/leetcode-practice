
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def is_unique(s):
            return len(set(s)) == len(s)

        def backtrack(start, current):
            nonlocal max_length
            max_length = max(max_length, len(current))

            for i in range(start, len(arr)):
                if is_unique(current + arr[i]):
                    backtrack(i + 1, current + arr[i])

        max_length = 0
        backtrack(0, "")
        return max_length
