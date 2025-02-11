class Solution:
    def clearDigits(self, s: str) -> str:
        tmp_arr = []

        for elem in s:
            if elem.isdigit():
                tmp_arr.pop()
            else:
                tmp_arr.append(elem)
        
        return "".join(tmp_arr)

# time complexity: O(n)
# space complexity: O(n)
# check note
        
