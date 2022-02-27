from collections import deque

N, M = map(int, input().split())

degree = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    singer = list(map(int, input().split()))
    for i in range(1, singer[0]):
        graph[singer[i]].append(singer[i+1])
        degree[singer[i+1]] += 1

def topology_sort():
    result = []
    q = deque()
    # 초기에 진입차수 0인 노드들 큐에 넣기
    for i in range(1, N+1):
        if degree[i] == 0:
            q.append(i)

    # 큐가 빌때 까지 반복
    while q:
        node = q.popleft()
        # 꺼낸 원소는 위상 정렬 결과값에 append
        result.append(node)
        # 꺼낸 노드랑 연결된 노드들 탐색
        for next in graph[node]:
            degree[next] -= 1
            # 새롭게 진입차수가 0이 된 노드들 큐에 넣기
            if degree[next] == 0:
                q.append(next)
    return result

is_cycle = topology_sort()

if len(is_cycle) == N:
    for i in is_cycle:
        print(i)
else:
    print(0)