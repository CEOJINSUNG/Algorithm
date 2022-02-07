import sys
from collections import deque
input = sys.stdin.readline

# 위상 정렬 알고리즘, degree : 진입 차수, graph : 그래프, dp : 걸리는 시간, node_time : 노드별 걸리는 시간, n : 노드 개수
def topology_sort(Degree, Graph, Dp, Node_time, n):
    result = []
    queue = deque()

    for i in range(1, n+1):
        if Degree[i] == 0:
            queue.append(i)
            Dp[i] = Node_time[i]
    
    while queue:
        current = queue.popleft()
        result.append(current)

        for i in Graph[current]:
            Degree[i] -= 1
            Dp[i] = max(Dp[current] + Node_time[i], Dp[i])
            if Degree[i] == 0:
                queue.append(i)
    
    # 위상 정렬 배열 순서
    return Dp

# 테스트 케이스
T = int(input())

# 정답 저장
answer = [0 for _ in range(T)]

for _ in range(T):
    N, K = map(int, input().split())
    # 각 노드별 걸리는 시간 1부터 시작이므로 [0]을 더해줌
    node_time = [0] + list(map(int, input().split()))
    degree = [0] * (N+1)
    graph = [[] for _ in range(N+1)]
    dp = [0 for _ in range(N+1)]

    for _ in range(K):
        X, Y = map(int, input().split())
        graph[X].append(Y)
        degree[Y] += 1
    W = int(input())

    total_time = topology_sort(degree, graph, dp, node_time, N)
    print(total_time[W])
