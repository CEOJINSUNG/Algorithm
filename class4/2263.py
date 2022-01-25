import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N = int(input())
inOrder = list(map(int, input().split()))
postOrder = list(map(int, input().split()))
index = [0] * (N+1)

for i in range(N):
    index[inOrder[i]] = i

def preOrder(ins, ie, ps, pe):
    if (ins > ie) or (ps > pe): 
        return

    root = postOrder[pe]
    print(root, end=" ")

    left = index[root] - ins
    right = ie - index[root]
    preOrder(ins, ins+left-1, ps, ps+left-1)
    preOrder(ie-right+1, ie, pe-right, pe-1)

preOrder(0, N-1, 0, N-1)