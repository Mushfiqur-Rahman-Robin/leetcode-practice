# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        val = 0
        while head:
            val = val * 2 + head.val
            head = head.next
        return val


## 🔍 Explanation (Step-by-Step)

# Let’s say the input linked list is:
# `[1] -> [0] -> [1]`
# Which represents the binary number **101**.

# ### Step-by-step execution:

# * Initialize `val = 0`

# #### First node: `1`

# ```python
# val = 0 * 2 + 1 = 1
# ```

# #### Second node: `0`

# ```python
# val = 1 * 2 + 0 = 2
# ```

# #### Third node: `1`

# ```python
# val = 2 * 2 + 1 = 5
# ```

# ✅ Final result: `5`, which is the decimal equivalent of binary `101`.

# Time Complexity: O(n) — where n is the number of nodes in the list (you visit each node once).
# Space Complexity: O(1) — constant space used (no extra data structures, just a single integer val).
