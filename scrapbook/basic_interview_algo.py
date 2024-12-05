def bubble_sort(list1):
    n = len(list1)

    for i in range(n):
        for j in range(0, n-i-1):
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]

    return list1 


def selection_sort(list1):
    n = len(list1)

    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if list1[j] < list1[min_idx]:
                min_idx = j
        
        list1[i], list1[min_idx] = list1[min_idx], list1[i]

    return list1


def insertion_sort(list1):
    n = len(list1)

    for i in range(1, n):
        key = list1[i]

        j = i - 1
        while j >=0 and key < list1[j]:
            list1[j+1] = list1[j]
            j -= 1
        
        list1[j+1] = key

    return list1



def quick_sort(list1):
    if len(list1) <= 1:
        return list1
    
    pivot = list1[len(list1) // 2]
    right = [x for x in list1 if x > pivot]
    left = [x for x in list1 if x < pivot]
    mid = [x for x in list1 if x == pivot]

    return quick_sort(left) + mid + quick_sort(right)


def binary_search(list1, target):
    list1.sort()
    l = 0
    r = len(list1) - 1

    while l <= r:
        mid = l + (r - l) // 2

        if target == list1[mid]:
            return mid
        
        if target > list1[mid]:
            l = mid + 1
        
        if target < list1[mid]:
            r = mid - 1
        
    return -1


class TreeNode(): 
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def build_tree():
    pass

def invert_tree(root):
    if not root:
        return None
    
    root.left, root.right = root.right, root.left

    invert_tree(root.left)
    invert_tree(root.right)

    return root


class ListNode():
    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.next = next

def inverse_linkedlist(head):
    curr = head
    prev = None

    while curr:
        next = curr.next
        curr.next = prev 
        prev = curr
        curr = next

    return prev


from collections import deque
def construct_binary_tree(values):
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root
   
    
def find_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True

# print(find_prime(18))


def factorial(n):
    if n < 0:
        return "Invaid"
    
    return 1 if n == 0 else n * factorial(n-1)

# print(factorial(6))


def find_fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    fib = find_fibonacci(n-1)
    fib.append(fib[-1] + fib[-2])

    return fib

# print(find_fibonacci(4))


# print(bubble_sort([4, 1, 5, 3, 7]))
# print(selection_sort([4, 1, 5, 3, 7]))
# print(insertion_sort([4, 1, 5, 3, 7]))
# print(quick_sort([4, 1, 5, 3, 7]))
# print(binary_search([4, 1, 5, 3, 7], target=4))
