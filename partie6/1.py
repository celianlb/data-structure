nb = [5, 8, 15, 39, 4, 12, 785, 14, 54, 128, 75]

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def construct_bst(nums):
    if not nums:
        return None
    nums.sort()
    mid = len(nums) // 2
    root = Node(nums[mid])
    root.left = construct_bst(nums[:mid])
    root.right = construct_bst(nums[mid+1:])
    return root

def find_minimum(root):
    if not root:
        return None
    while root.left:
        root = root.left
    return root.value
