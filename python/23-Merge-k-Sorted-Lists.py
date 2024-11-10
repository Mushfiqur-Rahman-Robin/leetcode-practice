# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
            # Since we're merging linked lists, returning None is more appropriate as it signifies an empty     linked list.
        
        while len(lists) > 1:
            mergedlist = []

            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if (i+1) < len(lists) else None
                mergedlist.append(self.mergeTwoList(list1, list2))
            
            lists = mergedlist
        return lists[0]

# The lists = merged_lists line updates lists to contain only the merged lists after each pass.
# The return lists[0] line returns the fully merged linked list when only one list remains in lists.
# This process continues until all lists are fully merged into one sorted linked list.
        

    def mergeTwoList(self, list1, list2):
        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                curr = list1
                list1 = list1.next

            else:
                curr.next = list2
                curr = list2
                list2 = list2.next

        curr.next = list1 if list1 else list2

        return dummy.next
                
        
# Tutorial link: https://www.youtube.com/watch?v=q5a5OiGbT6Q
# Time complexity: O(nlogk)
# Space complexity: O(n)
