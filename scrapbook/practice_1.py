# 1
def contains_duplicate(nums):
    return len(nums) != len(set(nums))

# 2
from collections import Counter
def check_valid_anagram(s, t):
    return Counter(s) == Counter(t)

# 3
def two_sum(nums, target):
    dictionary = {}

    for index, value in enumerate(nums):
        difference = target - value
        if difference in dictionary:
            return [dictionary[difference], index]
        dictionary[value] = index
    return 

# 4
from collections import defaultdict
def group_anagram(strs):
    ans = defaultdict(list)

    for s in strs:
        key = "".join(sorted(s))
        ans[key].append(s)

    return list(ans.values())

# 5
def top_k_freq_elem(nums, k):
    frequency_of_numbers = Counter(nums)

    top_k_freq = frequency_of_numbers.most_common(k)
    
    return [elem[0] for elem in top_k_freq]

# 6 
def productExceptSelf(nums):
    prod = 1
    res = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]

    return res

# 7
def longest_consecutive_sequence(nums):
    nums.sort()
    if not nums:
        return 0

    current_seq_count = 1
    longest_seq_count = 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            continue # avoid duplicate numbers, we can also use set at the beginning of the code
        if nums[i] == nums[i-1] + 1:
            current_seq_count += 1
        else:
            longest_seq_count = max(longest_seq_count, current_seq_count)
            current_seq_count = 1 # this is done for the cases where we can have few occurance in the list where consective sequence may be present. [1, 2, 3, -1, 0, 4, 5, 6, 7]

    return max(longest_seq_count, current_seq_count)

# 8
def ispalindrome(s):
    plain_str = ''.join(char.lower() for char in s if char.isalnum())
    return plain_str == plain_str[::-1]


# 9
def three_sum(nums):
    pass

# 10
def container_with_most_water(height):
    max_contain = 0
    i = 0
    j = len(height) - 1

    while i < j:
        x_axis = j - i
        y_axis = min(height[i], height[j])
        water_contained = x_axis * y_axis
        max_contain = max(max_contain, water_contained)

        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    
    return max_contain


# 11
def maxprofit(prices):
    max_profit_so_far = 0
    lowest_price_so_far = prices[0]

    for current_price in prices[1:]:
        if current_price < lowest_price_so_far:
            lowest_price_so_far = current_price
        
        current_profit = current_price - lowest_price_so_far
        max_profit_so_far = max(max_profit_so_far, current_profit)
    
    return max_profit_so_far

# 12
def longest_substr_without_repeating_char(s):
    max_len = 0
    l = 0
    char_set = set()
    
    for r in range(len(s)):
        if s[r] in char_set:
            char_set.remove(s[l])
            l += 1
        char_set.add(s[r])
        max_len = max(max_len, len(char_set))
    
    return max_len

# 13
def longest_repeating_char_replacement(s, k):
    max_repeat = 0
    l = 0
    freq_count = {}

    for r in range(len(s)):
        freq_count[s[r]] = 1 + freq_count.get(s[r], 0)

        while r - l + 1 -  max(freq_count.values()) > k:
            freq_count[s[l]] -= 1
            l += 1
        
        max_repeat = max(r - l + 1, max_repeat)

    return max_repeat

# print(longest_repeating_char_replacement("ABAB", 2))

# 14
def minimum_window_substring(s,t):
    pass

# 15
def valid_parenthesis(s):
    stack = []
    bracket_dict = {")": "(", "}": "{", "]": "["}

    for bracket in s:
        if bracket in bracket_dict.values():
            stack.append(bracket)
        
        elif bracket in bracket_dict.keys():
            if stack == [] or bracket_dict[bracket] != stack.pop():
                return False

        else:
            return False
        
    return stack == []

# print(valid_parenthesis("{[]}"))

# 16
def find_minimum_in_rotated_sorted_arr(nums):
    l = 0
    r = len(nums) - 1
    res = nums[0]

    while l <= r:
        if nums[l] < nums[r]:
            res = min(res, nums[l])
            break

        else:
            mid = l + (r - l) // 2
            res = min(res, nums[mid])


            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        
    return res
        
# print(find_minimum_in_rotated_sorted_arr([3,4,5,1,2]))

# 17
def search_in_rotated_sorted_arr(nums, target):
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = l + (r - l) // 2

        if target == nums[mid]:
            return mid
        
        if nums[l] <= nums[mid]:
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        
        else:
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1

    return - 1

# print(search_in_rotated_sorted_arr([4,5,6,7,0,1,2], 0))

# 18
def reverse_linked_list(head):
    curr = head
    prev = None

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev

# 19
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_sorted_list(list1, list2):
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

# 20
def reorder_list(head):
    pass

# 21
def remove_nth_node_from_end(head, n):
    dummy = ListNode(0, head)
    left = dummy
    right = head

    while n > 0:
        right = right.next # placing right pointer
        n -= 1

    while right:
        left = left.next
        right = right.next

    left.next = left.next.next # establishing link correctly

    return dummy.next  

# 22
def linked_list_cycle(head):
    dummy = ListNode(0, head)
    slow = dummy
    fast = dummy
    dummy.next = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            return True
    
    return False

# 23
def merge_k_sorted_list(lists):
    pass # will try

# 24
def invert_binary_tree(root):
    if not root:
        return None
    
    root.left, root.right = root.right, root.left

    invert_binary_tree(root.left)
    invert_binary_tree(root.right)

    return root

# 25
def max_depth_of_binary_tree(root):
    if not root:
        return 0
    
    return 1 + max(max_depth_of_binary_tree(root.left), max_depth_of_binary_tree(root.right))

# 26
def same_tree(p, q):
    if not p and not q:
        return False
    
    if not p or not q:
        return False
    
    return (p.val == q.val) \
            and same_tree(p.left, q.left) \
            and same_tree(p.right, q.right)

# 27
def subtree_of_another_tree(root, subroot):
    if not root:
        return False
    if not subroot:
        return True
    
    if isSameTree(root, subroot):
        return True
    
    return isSameTree(root.left, subroot.left) or \
            isSameTree(root.right, subroot.right)
    

def isSameTree(a, b):
    if not a and not b:
        return False
    
    if not a or not b:
        return False
    
    return (a.val == b.val) and isSameTree(a.left, b.left) and isSameTree(a.right, b.right)

# 28
def least_common_ancestor(root, p, q):
    lca = [root]

    def search(root):
        if not root:
            return None
        
        lca[0] = root
        if root is p and root is q:
            return None
        elif root.val < p.val and root.val < q.val:
            search(root.right)
        elif root.val > p.val and root.val > q.val:
            search(root.left)
        else:
            return None
    search(root)
    return lca[0]

# 29
from collections import deque
def binary_tree_level_order_traversal(root):
    if not root:
        return []

    res = []
    queue = deque()
    queue.append(root)

    while queue:
        level = []
        n = len(queue)

        for i in range(n):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
        
        res.append(level)

    return res

# 30
def validate_bst(root):
    def is_valid(node, minn, maxx):
        if not node:
            return True
        
        if node.val <= minn or node.val >= maxx:
            return False
        
        return is_valid(root.left, minn, node.val) and \
                is_valid(root.right, node.val, maxx)

    return is_valid(root, float('-inf'), float('inf'))

# 31
def kth_smallest_in_bst(root, k):
    n = 0
    stack = []
    curr = root

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        n += 1

        if n == k:
            return curr.val
        
        curr = curr.right

# 32
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def construct_binary_tree_from_preorder_and_inorder(preorder, inorder):
    if not preorder and not inorder:
        return None
    
    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    root.left = construct_binary_tree_from_preorder_and_inorder(preorder[1: mid+1], inorder[ :mid])
    root.right = construct_binary_tree_from_preorder_and_inorder(preorder[mid+1: ], inorder[mid+1: ])

    return root


# 33
def binary_tree_max_path_sum(root):
    res = [root.val]

    def dfs(root):
        if not root:
            return 0
        
        maxleft = dfs(root.left)
        maxright = dfs(root.right)

        maxleft = max(maxleft, 0)
        maxright = max(maxright, 0)

        res[0] = max(res[0], maxleft + root.val + maxright)

        return root.val + max(maxleft, maxright)
    
    dfs(root)
    return res[0]

# 34
def combination_sum(candidates, target):
    res = []

    def dfs(i, curr, total):
        if total == target:
            res.append(curr.copy())
            return

        if i >= len(candidates) or total > target:
            return 

        curr.append(candidates[i])
        dfs(i, curr, total+candidates[i])
        curr.pop()
        dfs(i+1, curr, total)

    dfs(0, [], 0)
    return res


# 35
def word_search(board, word):
    row = len(board)
    col = len(board[0])

    path = set()

    def dfs(r, c, index):
        if index == len(word):
            return True
        
        if (r < 0 and c < 0 or
            r >= row and c >= col or
            word[index] != board[r][c] or
            (r,c) in path):
            return False
        
        path.add((r,c))

        res = (
            dfs(r, c + 1, index + 1) or
            dfs(r, c - 1, index + 1) or
            dfs(r + 1, c, index + 1) or
            dfs(r - 1, c, index + 1)
        )

        path.remove((r,c))

        return res
    
    for i in range(row):
        for j in range(col):
            if dfs(i, j, 0):
                return True
            
    return False

# print(word_search([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))


# 36
def num_of_island(grid):
    row = len(grid)
    col = len(grid[0])
    island = 0

    def dfs(r, c, grid):
        if not grid:
            return
        
        if (r < 0 or c < 0 or
            r >= row or c >= col or
            grid[r][c] != '1'):
            return 

        grid[r][c] = "#"
        dfs(r, c + 1, grid)
        dfs(r, c - 1, grid)
        dfs(r + 1, c, grid)
        dfs(r - 1, c, grid)

    for r in range(row):
        for c in range(col):
            if grid[r][c] == '1':
                dfs(r, c, grid)
                island += 1
    
    return island

# print(num_of_island([
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]))


# 37
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def clone_graph(node):
    oldToNew = {}

    def dfs(node):
        if node in oldToNew:
            return oldToNew[node]
        
        copy = Node(node.val)
        oldToNew[node] = copy

        for nei in node.neighbors:
            copy.neighbors.append(dfs(nei))

        return copy
    
    return dfs(node) if node else None

# 38
def climbing_stairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    dp = [0] * n
    dp[0] = 1
    dp[1] = 2

    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n-1]

# print(climbing_stairs(3))

# 39
def house_robber(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])
    
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):
        dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
    
    return dp[n - 1]

# print(house_robber([1,2,3,1]))

# 40
def house_robber_ii(nums):
    if len(nums) == 1:
        return nums[0]
    return max(house_robber(nums[1:]), house_robber(nums[:-1]))

def house_robber(nums):
    n = len(nums)

    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])
    
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):
        dp[i] = max(dp[i-2]+nums[i], dp[i-1])

    return dp[n-1]

# print(house_robber_ii([2,3,2]))

# 41
def longest_palindromic_substr(s):
    res = ""
    reslen = 0

    for i in range(len(s)):
        l, r = i, i # odd length
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > reslen:
                res = s[l: r+1]
                reslen = r - l + 1
            
            l -= 1
            r += 1
        
        l, r = i, i + 1 # even length
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > reslen:
                res = s[l: r+1]
                reslen = l - r + 1
            
            l -= 1
            r += 1
    
    return res

# print(longest_palindromic_substr("babad"))

# 42
def plaindromic_substr(s):
    res = 0

    for i in range(len(s)):
        l, r = i, i 
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
    
    return res

# print(plaindromic_substr("abc"))

# 43
def decode_ways(s):
    dp = {len(s): 1}

    for i in range(len(s) - 1, -1, -1):
        if s[i] == '0':
            dp[i] = 0
        else:
            dp[i] = dp[i+1]

        if (i+1 < len(s) and (
            s[i] == '1' or 
            s[i] == '2' and s[i+1] in '0123456'
        )):
            dp[i] = dp[i] + dp[i+2]

    return dp[0]

# print(decode_ways("226"))

# 44 
def coin_change(coins, amount):
    coins.sort()
    dp = [0] * (amount + 1)

    for i in range(1, amount+1):
        min_coin = float('inf')

        for coin in coins:
            diff = i - coin
            if diff < 0:
                break
            min_coin = min(min_coin, dp[diff]+1)
        
        dp[i] = min_coin

    if dp[amount] < float('inf'):
        return dp[amount]
    else:
        return -1
    
# print(coin_change([1,2,5], 11))

# 45
def max_product(nums):
    max_p = nums[0]
    min_p = nums[0]
    maximum_product = max_p

    for i in nums[1:]:
        tmp = min_p
        min_p = min(i, min_p * i, max_p * i)
        max_p = max(i, tmp * i, max_p * i)

        maximum_product = max(max_p, maximum_product)

    return maximum_product

# print(max_product([2,3,-2,4]))

# 46
def word_break(s, wordDict):
    dp = [False] * (len(s) + 1)
    dp[len(s)] = True

    for i in range(len(s) - 1, -1, -1):
        for w in wordDict:
            if (i + len(w)) <= len(s) and s[i: i+len(w)] == w:
                dp[i] = dp[i + len(w)]
            if dp[i]:
                break
    return dp[0]

# print(word_break("leetcode", ["le", "leet", "de", "code"]))

# 47
def longest_increasing_subsequence(nums):
    n = len(nums)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] < nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
    
    return max(dp)

# print(longest_increasing_subsequence([10,9,2,5,3,7,101,18]))


# xx
def unique_paths(m, n):
    dp = [[0 for j in range(n)] for i in range(m)]
    dp[0][0] = 1

    for i in range(m):
        for j in range(n):
            if i == j == 0:
                continue

            val = 0
            if i > 0:
                val += dp[i-1][j]
            if j > 0:
                val += dp[i][j-1]

            dp[i][j] = val
    
    return dp[m-1][n-1]

# print(unique_paths(3, 7))

# xx
def longest_common_subsequence(text1, text2):
    dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

    for i in range(len(text1) - 1, -1, -1):
        for j in range(len(text2) -1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i][j+1], dp[i+1][j])
    
    return dp[0][0]

# print(longest_common_subsequence("abcde", "ace"))




# xx
def max_subarr(nums):
    curr_sum = float('-inf')
    max_sum = float("-inf")

    for n in nums:
        curr_sum = max(curr_sum+n, n)
        max_sum = max(curr_sum, max_sum)

    return max(curr_sum, max_sum)

# print(max_subarr([-2,1,-3,4,-1,2,1,-5,4]))

# xx
def canjump(nums):
    goal = len(nums) - 1

    for i in range(len(nums) - 1, -1, -1):
        if i + nums[i] >= goal:
            goal = i
    
    return True if goal == 0 else False

# print(canjump([2,3,1,1,4]))

# xx
def rotate_image(matrix):
    n = len(matrix)
    
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]
    
    return matrix


# print(rotate_image([[1,2,3],[4,5,6],[7,8,9]]))

# xx
def num_of_one_bits(n):
    res = 0
    for i in range(32):
        if (n >> i) & 1:
            res += 1
    
    return res

# print(num_of_one_bits(11))

# xx
def counting_bits(n):
    offset = 1
    dp = [0] * (n+1)

    for i in range(1, n+1):
        if offset * 2 == i:
            offset = i
        
        dp[i] = 1 + dp[i - offset]

    return dp

# print(counting_bits(5))

# xx
def reverse_bits(n):
    reversed_n = 0

    for _ in range(32):
        reversed_n = (reversed_n << 1) | (n & 1)
        n >>= 1
        
    return reversed_n

# print(reverse_bits(43261596)) # 00000010100101000001111010011100

# xx
def missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)

    return expected_sum - actual_sum

# print(missing_number([3,0,1]))

# xx
def sum_of_two_int(a, b):
    mask = 0xffffffff

    while (mask & b) > 0:
        carry = (a & b) << 1 # carry
        a = a ^ b # sum without carry
        b = carry
    
    return (mask & a) if b > 0 else a
    

# print(sum_of_two_int(2, 3))