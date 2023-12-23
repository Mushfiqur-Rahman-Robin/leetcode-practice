from collections import Counter
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        list_end = len(grid) * len(grid)
        flat_list = []
        for i in range(len(grid)):
            for elem in grid:
                flat_list.append(elem[i])

        frequency_count = Counter(flat_list)
        for key, value in frequency_count.items():
            if value == 2:
                double_appearence = key

        if list_end not in flat_list:
            missing = list_end
        elif list_end in flat_list:
            for i in range(1, len(flat_list)):
                if i not in flat_list:
                    missing = i
        return [double_appearence, missing]
        
