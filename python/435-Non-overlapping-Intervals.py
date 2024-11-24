class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count_of_remove = 0
        prevEnd = intervals[0][1]
        
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                count_of_remove += 1
                prevEnd = min(prevEnd, end)
        
        return count_of_remove


# tutorial link: https://www.youtube.com/watch?v=nONCGxWoUfM
# time complexity: O(nlogn)
# space complexity: O(1)
# check note
