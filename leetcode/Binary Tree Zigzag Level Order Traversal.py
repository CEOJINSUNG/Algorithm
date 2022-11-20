# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        
        tree = defaultdict(list)
        q = deque()
        q.append((root, 0))

        while q:
            node, num = q.popleft()
            
            tree[num].append(node.val)
            if node.left != None:
                q.append((node.left, num + 1))
            if node.right != None:
                q.append((node.right, num + 1))
        
        answer = []
        tree = list(tree.values())
        for index in range(len(tree)):
            if index%2 != 0:
                answer.append(reversed(tree[index]))
            else:
                answer.append(tree[index])
        return answer