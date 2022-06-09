from itertools import cycle
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(start, answer, visit, graph):
    global cycle
    visit[start] = True
    cycle.append(start)
    next = graph[start]

    if visit[next]:
        if next in cycle:
            answer += cycle[cycle.index(next):]
            return
    else:
        dfs(next, answer, visit, graph)


t = int(input())
for _ in range(t):
    n = int(input())
    number = [0] + list(map(int, input().split()))
    visit = [False] * (n+1)
    answer = []

    for i in range(1, n+1):
        if not visit[i]:
            cycle = []
            dfs(i, answer, visit, number)
    
    print(n - len(answer))