class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr_elem_freq = Counter(arr)

        max_lucky = -1

        for key, value in arr_elem_freq.items():
            if key == value:
                max_lucky = max(max_lucky, value)
        
        return max_lucky
        
# time complexity: O(n)
# space complexity: O(n)
