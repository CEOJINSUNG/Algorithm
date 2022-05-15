from collections import deque

T = int(input())

while T:
    K, M, P = map(int, input().split())
    arr = [[] for _ in range(M + 1)]
    indegree = [0] * (M + 1)
    count = [[0, 0]] * (M + 1) # [값, 개수]의 배열
    order = [0] * (M + 1)
    queue = deque()

    for i in range(P):
        first, second = map(int, input().split())
        arr[first].append(second)
        indegree[second] += 1

    for i in range(1, M + 1):
        if indegree[i] == 0:
            count[i] = [1, 1]
            queue.append(i)

    while queue:
        temp = queue.popleft()

        if count[temp][1] >= 2: # 개수를 비교해서 값을 갱신한다.
            order[temp] = count[temp][0] + 1
        else:
            order[temp] = count[temp][0]

        for second in arr[temp]:
            indegree[second] -= 1
            if count[second][0] == order[temp]: # 같으면 개수를 증가 시켜준다.
                count[second][1] += 1
            elif count[second][0] < order[temp]: # 이번에 들어오는 값이 더 크다면 바꿔준다.
                count[second] = [order[temp], 1]

            if indegree[second] == 0: # 0 이 됐을 때가 모든 값들을 다 처리 했을 때니깐, 큐에 넣어서 order 값을 갱신 할 수 있도록 한다.
                queue.append(second)

    print(K, end = " ")
    print(order[M])
    T -= 1