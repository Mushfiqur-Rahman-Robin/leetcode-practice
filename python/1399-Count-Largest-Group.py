class Solution:
    def countLargestGroup(self, n: int) -> int:
        def sum_of_digits(num):
            return sum(int(d) for d in str(num))

        sum_count = {}
        for num in range(1, n + 1):
            digit_sum = sum_of_digits(num)
            if digit_sum not in sum_count:
                sum_count[digit_sum] = 1
            else:
                sum_count[digit_sum] += 1

        max_group_size = max(sum_count.values())
        
        return sum(1 for val in sum_count.values() if val == max_group_size)
        
# Time Complexity: O(n × log n)
# Space Complexity: O(1) (constant, because digit sum range is limited)
