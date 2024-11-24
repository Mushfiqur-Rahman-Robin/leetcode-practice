class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []

        if len(intervals) == 1:
            return intervals

        for i in range(1, len(intervals)):
            if intervals[i-1][1] >= intervals[i][0]:
                intervals[i] = [min(intervals[i-1][0], intervals[i][0]),
                            max(intervals[i-1][1], intervals[i][1])]
            else:
                res.append(intervals[i-1])
        
        res.append(intervals[-1])

        return res        

# time complexity: O(nlogn)
# space complexity: O(n)
# check note
