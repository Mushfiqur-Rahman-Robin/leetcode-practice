class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        div_list_sum = 0
        non_div_list_sum = 0

        for num in range(1, n+1):
            if num % m == 0:
                div_list_sum += num
            else:
                non_div_list_sum += num

        return non_div_list_sum - div_list_sum

# time complexity: O(n)
# space complexity: O(1)
