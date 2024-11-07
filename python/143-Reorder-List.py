# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return 
        
        fast = head # 1
        slow = head # 1

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow # 3

        # [1,2,3,4] -> [1,2] [3,4]

        # reverse second half
        prev = None
        curr = mid  # curr is now at 3, which is the start of the second half

        while curr:
            next_node = curr.next  # 4
            curr.next = prev       # Reverse the current node's pointer (3 -> None) (4 -> 3)
            prev = curr            # 3
            curr = next_node       # 4

        head_of_second_reversed = prev  # 4

        # Before starting the reversal:

        # mid points to 3.
        # curr = mid, so curr also starts at 3.
        # prev is None.

        # First iteration of the while loop:

        # next_node = curr.next, which is 4.
        # curr.next = prev makes 3 -> None.
        # Then, prev = curr, so prev now points to 3.
        # Finally, curr = next_node, so curr moves to 4.

        # Second iteration of the while loop:

        # next_node = curr.next, which is None (since 4 was the last node).
        # curr.next = prev, so now 4 -> 3.
        # prev = curr, so prev now points to 4.
        # curr = next_node, which sets curr to None, ending the loop.

        # After the loop completes:

        # prev points to 4, which is now the head of the reversed second half (4 -> 3).
        # So, head_of_second_reversed = prev indeed points to 4.
        # Therefore, after reversing the second half:

        # head_of_second_reversed points to 4, marking the start of the reversed segment [4 -> 3].

        # Update link between first half and reversed second half

        first = head # 1
        second = head_of_second_reversed # 4

        while second.next:
            
            next_hop = first.next
            first.next = second
            first = next_hop
            
            next_hop = second.next
            second.next = first
            second = next_hop

        
        # Here’s a step-by-step breakdown of how the pointers first and second move during the loop, with example comments based on a list [1, 2, 3, 4] (where first starts at 1, and second starts at 4):

        # First iteration of the loop:

        # next_hop = first.next saves 2 (the node after 1).

        # first.next = second makes 1 -> 4 (linking the first node to the beginning of the reversed half).

        # first = next_hop moves first to 2.

        # next_hop = second.next saves 3 (the next node after 4 in the reversed half).

        # second.next = first makes 4 -> 2.

        # second = next_hop moves second to 3.

        # The list now looks like 1 -> 4 -> 2.


        # Second iteration of the loop:

        # next_hop = first.next saves None (end of the list after 2).

        # first.next = second makes 2 -> 3 (linking 2 to the next node of the reversed half).

        # first = next_hop moves first to None (ending the first half iteration).

        # Since second.next is None, the loop exits here.

        # After this process, the list is reordered as [1, 4, 2, 3]. This code alternately links nodes from the original first half and the reversed second half until they’re completely merged, and it stops when second.next is None.

        
# Time complexity: O(n)
# Space complexity: O(1) - LL, O(n) - List
# 2 solutions: https://leetcode.com/problems/reorder-list/solutions/801971/python-o-n-by-two-pointers-w-visualization/
# Tutorial link: https://www.youtube.com/watch?v=S5bfdUTrKLM
