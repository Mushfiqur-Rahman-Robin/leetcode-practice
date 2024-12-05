class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr_mapping = {}
        res = []

        for i, num in enumerate(sorted(set(arr))):
                arr_mapping[num] =  i + 1

        # {10: 1, 20: 2, 30: 3, 40: 4}
        for i in range(0, len(arr)):
            res.append(arr_mapping[arr[i]])
        
        return res
                
# time complexity: O(nlogn)
# space complexity: O(n)
# check note   
