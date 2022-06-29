import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n, r, q = map(int, input().split())

tree = [[] for _ in range(n+1)]
check = [0]*(n+1)
for _ in range(n-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

def countSubtreeNodes(currentNode):
    check[currentNode] = 1 
    for Node in tree[currentNode]:
        if check[Node] == 0:
            countSubtreeNodes(Node)
            check[currentNode] += check[Node]

countSubtreeNodes(r)

for _ in range(q):
    u = int(input())
    print(check[u])