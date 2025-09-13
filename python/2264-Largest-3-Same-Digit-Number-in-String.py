class Solution:
    def largestGoodInteger(self, num: str) -> str:
        # max_substr = ""
        # curr_max = 0

        # left, right = 0, 3

        # while right <= len(num):
        #     if len(Counter(num[left:right])) == 1:
        #         curr_max = str(num[left:right])
        #         if curr_max > max_substr:
        #             max_substr = curr_max
            
        #     left += 1
        #     right += 1

        max_substr = ""
        
        for i in range(len(num) - 2):
            sub_str = num[i:i+3]

            if sub_str[0] == sub_str[1] == sub_str[2]:
                if sub_str > max_substr:
                    max_substr = sub_str

        return max_substr

# time complexity: O(n)
# space complexity: O(1)
