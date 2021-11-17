from collections import deque, defaultdict

# 정점의 수 입력 받기
vertices = int(input())

# 트리 구조 입력받가
graphs = [[] for _ in range(vertices+1)]
for _ in range(vertices-1):
    one, two = map(int, input().split())
    graphs[one].append(two)
    graphs[two].append(one)

# 비교해야 하는 DFS 순서
final_dfs = list(map(int, input().split()))

# 방문여부를 확인하는 함수
visited = [0] * (vertices + 1)

# 부모 자식간의 위치를 확인해야 하므로 리스트를 선언함
relation = defaultdict(list)

# 시작은 무조건 1로 시작해야함
if final_dfs[0] != 1:
    print(0)
else:
    # bfs 함수 이용
    queue = deque()

    # 1로 시작해야 하므로 선언
    queue.append(1)
    visited[1] = 1

    # 큐를 이용해 방문 여부를 확인
    while queue:
        node = queue.popleft()
        for i in graphs[node]:
            if visited[i] != 0: continue
            visited[i] = visited[node] + 1
            relation[node].append(i)
            queue.append(i)
    
    # 주어진 함수와 우리가 검증한 트리와 맞는지 확인
    q = deque()
    q.append(1)
    # 위치
    position = 1

    while q:
        test = q.popleft()

        compare = set(relation[test])
        order = final_dfs[position:position + len(compare)]
        q.extend(order)
        position += len(compare)

        if compare != set(order):
            print(0)
            break
    else:
        print(1)