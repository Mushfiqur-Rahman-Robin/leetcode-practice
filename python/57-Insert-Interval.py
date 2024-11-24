class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[1]: # new interval ... interval
                res.append(newInterval)
                return res + intervals[i: ]

            elif intervals[i][1] < newInterval[0]: # interval ... new interval
                res.append(intervals[i])

            else:
                newInterval = [min(newInterval[0], intervals[i][0]),
                                max(newInterval[1], intervals[i][1])]

        res.append(newInterval) # ensures adding new interval if first if condition is not executed 
        return res
        
# tutorial link: https://www.youtube.com/watch?v=A8NUOmlwOlM
# time complexity: O(n)
# space complexity: O(n)
# check note   
        
