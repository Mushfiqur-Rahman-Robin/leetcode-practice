class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_str = str(num)

        for ch in num_str:
            if ch != "9":
                max_num = num_str.replace(ch, "9")
                break
            else:
                max_num = num_str
        
        min_num = num_str.replace(num_str[0], "0")
        
        return int(max_num) - int(min_num)

# Time complexity: O(n)
# Space complexity: O(n)
