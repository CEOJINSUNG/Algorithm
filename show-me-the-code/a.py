# from collections import defaultdict

# # the number of medicine
# n = int(input())

# # medicine
# medicine = list(map(int, input().split()))

# if n == 1:
#     print(medicine[0])

# else:
#     # 할인 정보
#     sale_info = {i: [] for i in range(n)}
#     order = defaultdict(list)

#     for i in range(n):
#         p = int(input())
#         total = 0
#         for j in range(p):
#             medi, cost = map(int, input().split())
#             total += cost

#             sale_info[i].append((cost, medi-1))
        
#         order[total].append(i)

#     sorted_order = sorted(order.items(), key = lambda item: item[0], reverse=True)

#     buy = []
#     answer = 0

#     for cost, position in sorted_order:
#         sorted_position = sorted(position, key = lambda item: medicine[item])
#         for element in sorted_position:
#             if element in buy:
#                 continue
            
#             answer += medicine[element]
#             buy.append(element)

#             for decrease, medi in sale_info[element]:
#                 medicine[medi] -= decrease

#                 if medicine[medi] <= 0:
#                     medicine[medi] = 1

#     print(answer)

from collections import deque

n = int(input())

medicine = list(map(int, input().split()))

# 진입 차수 테이블 초기화
indegree = [0] * (n+1)

# 그래프 데이터 담을 인접 리스트 초기화
graph = [[] for _ in range(n+1)]

for i in range(n):
    p = int(input())
    for j in range(p):
        medi, cost = map(int, input().split())
        graph[i].append(medi)
        # 진입차수 추가 a -> b이기 때문에 b입장에서 진입차수 +1
        indegree[medi] += 1

print(indegree)

def topology_sort():
    result = []
    q = deque()
    # 초기에 진입차수 0인 노드들 큐에 넣기
    for i in range(1, n+1):
        if indegree[i] == 1:
            q.append(i)

    # 큐가 빌때 까지 반복
    while q:
        node = q.popleft()
        # 꺼낸 원소는 위상 정렬 결과값에 append
        result.append(node)
        # 꺼낸 노드랑 연결된 노드들 탐색
        for next in graph[node]:
            indegree[next] -= 1
            # 새롭게 진입차수가 0이 된 노드들 큐에 넣기
            if indegree[next] == 0:
                q.append(next)
    
    for i in result:
        print(i, end=' ')

topology_sort()