class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        symmetric_count = 0

        for num in range(low, high + 1):
            s = str(num)
            if len(s) % 2 != 0:
                continue

            mid = len(s) // 2
            first_half = s[:mid]
            second_half = s[mid:]

            if sum(int(d) for d in first_half) == sum(int(d) for d in second_half):
                symmetric_count += 1

        return symmetric_count

# time complexity: O(n^2)
# space complexity: O(1)
