class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
    
# tutorial link: https://www.youtube.com/watch?v=wjYnzkAhcNk
# time complexity: O(n)
# space complexity: O(1)
# check note
# this is a kind of problem where having the concept memorized will help.
