# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # using Floyd'd hare and tortoise algorithm (slow and fast pointer)
        dummy = ListNode()
        slow = dummy
        fast = dummy
        dummy.next = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True
        
        return False

# Time complexity: O(n)
# Space complexity: O(1)
# Tutorial link: https://www.youtube.com/watch?v=y-ckZ2hpC8Y

        
        
