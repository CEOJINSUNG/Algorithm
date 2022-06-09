import sys
sys.setrecursionlimit(10**6)

preOrder = []

def postOrder(start, end):
    if start > end:
        return
    
    root = preOrder[start]
    index = end + 1

    for i in range(start+1, end+1):
        if preOrder[start] < preOrder[i]:
            index = i
            break
    
    postOrder(start+1, index-1)
    postOrder(index, end)
    print(root)

while True:
    try:
        preOrder.append(int(sys.stdin.readline()))
    except:
        break

postOrder(0, len(preOrder) - 1)