import sys
input = sys.stdin.readline

class Node:
    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right


def printInorder(node):
    if node.left != ".":
        printInorder(binary_tree[node.left])
    print(node.item, end="")

    if node.right != ".":
        printInorder(binary_tree[node.right])

def printPostorder(node):
    if node.left != ".":
        printPostorder(binary_tree[node.left])
        
    if node.right != ".":
        printPostorder(binary_tree[node.right])
        
    print(node.item, end="")

def printPreorder(node):
    print(node.item, end="")
    if node.left != ".":
        printPreorder(binary_tree[node.left])
        
    if node.right != ".":
        printPreorder(binary_tree[node.right])
    

N = int(input())
binary_tree = {}
for _ in range(N):
    node, left, right = map(str, input().split())
    binary_tree[node] = Node(item = node, left=left, right=right)

printPreorder(binary_tree['A'])
print()
printInorder(binary_tree['A'])
print()
printPostorder(binary_tree['A'])