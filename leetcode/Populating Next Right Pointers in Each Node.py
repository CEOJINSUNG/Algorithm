"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None
        left, right, n = root.left, root.right, root.next
        if left:
            left.next = right
            if n: 
                right.next = n.left
            self.connect(left)
            self.connect(right)
        return root