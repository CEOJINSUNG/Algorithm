# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        
        answer = []
        def inorder(node):
            if node.left != None:
                inorder(node.left)
            answer.append(node.val)
            if node.right != None:
                inorder(node.right)
        
        inorder(root)
        return answer