# 알고리즘 유형별 정리하기

- 알고리즘 유형은 이것이 코테다에 나온 코딩테스트 유형 분석에 따라 정리하였습니다. 
- 정렬, 그리디, 구현, BFS/DFS, 최단 경로, 다이나믹 프로그래밍, 기타 그래프 이론, 이진탐색
- 빈도수 기준이 아니고 책에 나온 유형 분석 순대로 나열하였습니다.

## 1. 정렬

- 정렬 알고리즘은 N개의 숫자가 입력되었을 때, 사용자가 지정한 기준에 맞춰 정렬하고 출력하는 알고리즘
- 종류 : 선택 정렬, 삽입 정렬, 버블 정렬, 합병 정렬, 퀵 정렬

### 1) 선택 정렬

#### 특징

1. 선택 정렬은 정렬된 값을 배열의 맨 앞부터 하나씩 채워나가게 됩니다. 따라서, 뒤에 있는 index로 갈수록 비교 범위가 하나씩 점점 줄어드는 특성을 가지고 있습니다.
2. 입력 배열이 이미 정렬된 여부와 상관없이 동일한 연산량을 가지고 있어 최적화 여지가 적어서 다른 O(N^2)과 비교해도 성능이 떨어지는 편입니다.
3. 성능의 한계로 실전에서 보여지지 않지만 가장 기본적인 정렬 알고리즘입니다.

#### 구현

```
def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
```

### 2) 삽입 정렬

#### 특징

1. 선택/거품 정렬은 패스가 거듭될 수록 탐색 범위가 줄어드는 반면에 삽입 정렬은 오히려 점점 정렬 범위가 넓어집니다.
2. 큰 그림에서 봤을 때 바깥 쪽 루프는 순방향, 안 쪽 루프는 역방향으로 진행하고 있습니다.

#### 구현

두 개의 반복문을 사용하는데 내부 반복문에서는 정렬 범위에 새롭게 추가된 값과 기존 값들을 뒤에서 부터 계속해서 비교해나가면서 앞의 값이 뒤의 값보다 클 경우 자리 교대(swap)를 합니다. 외부 반복문에서는 정렬 범위를 2에서 N으로 확대해 나갑니다.

```
def insertion_sort(arr):
    for end in range(1, len(arr)):
        for i in range(end, 0, -1):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
```

#### 최적화

기존에 있던 값들이 이전에 모두 정렬되었다는 점을 고려해 불필요한 비교 작업을 제거할 수 있습니다.

```
def insertion_sort(arr):
    for end in range(1, len(arr)):
        i = end
        while i > 0 and arr[i-1] > arr[i]:
            arr[i-1], arr[i] = arr[i], arr[i-1]
            i -= 1
```

### 3) 버블 정렬

#### 특징

1. 거품 정렬은 점점 큰 값들을 뒤에서부터 앞으로 하나씩 쌓여 나가게 하기 때문에 후반으로 갈수록 정렬 범위가 하나씩 줄어들게 됩니다. 왜냐하면 다음 패스에서는 이전 패스에서 뒤로 보내놓은 가장 큰 값이 있는 위치 전까지만 비교해도 되기 때문입니다.
2. 제일 작은 값을 찾아서 맨 앞에 위치시키는 선택 정렬과 비교했을 때 정반대의 정렬 방향을 가집니다.
3. 다른 정렬 알고리즘에 비해서 자리 교대가 빈번하게 일어하는 경향을 가지고 있습니다. 예를 들어, 선택 정렬의 경우 각 패스에서 자리 교대가 딱 한번만 일어납니다.
4. 최적화 여지가 많은 알고리즘입니다.

#### 구현

```
def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
```

#### 최적화

이전 패스에서 앞뒤 자리 비교가 있었는지 여부를 체크하는 대신 마지막으로 앞뒤 자리 비교가 있었던 index를 기억해두면 다음 패스에서는 그 자리 전까지만 정렬해도 됩니다. 따라서 한 칸씩 정렬 범위를 줄여나가는 대신 한번에 여러 칸씩 정렬 범위를 줄여나갈 수 있습니다.

```
def bubble_sort(arr):
    end = len(arr) - 1
    while end > 0:
        last_swap = 0
        for i in range(end):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                last_swap = i
        end = last_swap
```

### 4) 합병 정렬

#### 특징

1. 알고리즘을 큰 그림에서 보면 분할 단계와 합병 단계로 나눌 수 있으며, 단순히 중간 인덱스를 찾아야 하는 분할 비용보다 모든 값들을 비교해야하는 합병 비용이 큽니다. 
2. 두 개의 배열을 병합할 때 병합 결과를 담아 놓을 배열이 추가로 필요합니다.
3. 다른 정렬 알고리즘과 달리 인접한 값들 간에 상호 자리 교대가 일어나지 않습니다.

#### 구현

```
def merge_sort(arr):
    if len(arr) < 2:
        return arr
    
    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])
    
    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr
```

#### 최적화

병합 결과를 담을 새로운 배열을 매번 생성해서 리턴하지 않고, 인덱스 접근을 이용해 입력 배열을 계속해서 업데이트하면 메모리 사용량을 대폭 줄일 수 있습니다. (In-place sort)

```
def merge_sort(arr):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)
    
    def merge(low, mid, high):
        temp = []
        l, h = low, mid
        
        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1
        
        while l < mid:
            temp.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1
        
        for i in range(low, high):
            arr[i] = temp[i - low]
    
    return sort(0, len(arr))
```

### 5) 퀵 정렬

#### 특징

1. 파이썬의 list.sort() 함수는 프로그래밍 언어 차원에서 기본적으로 지원되는 내장 정렬 함수는 대부분 퀵 정렬을 기본으로 합니다.
2. 일반적으로 원소의 개수가 적어질수록 나쁜 중간값이 선택될 확률이 높아지기에, 원소의 개수에 따라 퀵 정렬에 다른 정렬을 혼합해서 쓰는 경우가 많습니다.
3. 합병 정렬과 퀵 정렬은 분할 정복과 재귀 알고리즘을 사용한다는 측면에서는 유사해보이지만, 내부적으로 정렬을 하는 방식에서는 큰 차이가 있습니다.
4. 합병 정렬은 항상 정중앙을 기준으로 단순 분할 후 합병 시점에서 값의 비교 연산이 발생하는 반면, 퀵 정렬은 분할 시점부터 비교 연산이 일어나기 때문에 그 이후 병합에 들어가는 비용이 매우 적거나 구현 방법에 따라서 아예 병합을 하지 않을 수도 있습니다.

#### 구현

```
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)
```

#### 최적화

매번 재귀 호출 때마다 새로운 리스트를 생성하여 리턴하기 때문에 메모리 사용 측면에서 비효율적이므로 메모리 사용이 적은 in-place 정렬이 선호됩니다. 따라서, quick_sort() 내부에 sort(), partition() 2개의 내부 함수로 나눠 sort()는 재귀 함수며 정렬 범위를 시작 인덱스와 끝 인덱스로 인자를 받고 partition()은 정렬 범위를 인자로 받아 좌우측의 값들을 정렬하고 분할 기준점의 인덱스를 리턴합니다. 

```
def quick_sort(arr):
    def sort(low, high):
        if high <= low:
            return
        
        mid = partition(low, high)
        sort(low, mid-1)
        sort(mid, high)
    
    def partiion(low, high):
        pivot = arr[(low + high) // 2]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return low
    
    return sort(0, len(arr) - 1)
```

## 2. 그리디

그리디 알고리즘(Greedy Algorithm)이란 "매 선택에서 지금 이 순간 당장 최적인 답을 선택하여 적합한 결과를 도출하자"라는 모토를 가지는 알고리즘 설계 기법이다.

- 탐욕 선택 속성 : 앞의 선택이 이후의 선택에 영향을 주지 않음
- 최적 부분 구조 : 문제에 대한 최적해가 부분문제에 대해서도 역시 최적해임

특성을 가진 문제들을 해결하는데 강점이 있다. 즉, 한번의 선택이 다음 선택에는 전혀 무관한 값이여야 하며 매 순간의 최적해가 문제에 대한 최적해여야 한다는 의미이다. 

#### 사용되는 예시

- AI에 있어서 결정 트리 학습법
- 활동 선택 문제(Activity Selection Problem)
- 거스름돈 문제
- 최소 신장 트리(Minimum Spanning Tree)
- 제약조건이 많은 대부분의 문제
- 다익스트라 알고리즘
- 허프만 코드
- 크러스컬 알고리즘

#### 최적값을 구하는데 실패하는 문제들

- 외판원 순회 문제 (TSP, Traveling Salesperson Problem)
- 배낭 문제 (Knapsack Problem)

### 1) 거스름돈 문제

```
n = 1230
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin
    n %= coin

print(count)
```

### 2) 활동 선택, 스케쥴링 문제

- 활동 선택 문제란, 한번에 하나의 활동만 처리할 수 있는 하나의 강의실에서 제안된 활동들 중 가장 많은 활동을 처리할 수 있는 스케쥴을 짜는 문제임

> 백준 [회의실 배정](https://www.acmicpc.net/problem/1931) 보기

```
N = int(input())
times = []
for n in range(N) :
    times.append(list(map(int, input().split())))

# 일찍 끝나는 순서로 정렬
times.sort()

# 같은 end time 내에서
# 빠른 start time 순으로 정렬 되어있어야 한다.
# [[4, 4], [3, 4], [2, 4]] 의 경우 [4, 4] 만하고 끝나버리기 때문
times.sort(key = lambda x : x[1])

answer = 0
end = 0

for t in times :
    if t[0] >= end : # 회의 시간 겹치지 않기 위해..
        answer += 1
        end = t[1]

print(answer)
```

## 3. 구현

구현 알고리즘은 별도의 유형이 있다기 보다 문제를 보면서 푸는 방법은 아는데 코드로 옮기는 과정이 어려운 알고리즘인 것 같다. 구현에는 대표적으로 브루트 포스 알고리즘이 있고 파이썬 같은 경우에는 구현 난이도는 쉽지만 프로그램 실행시간이 길기에 PyPy3를 쓰는 것이 좋다.

### 예시) 상하좌우

```
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny
print(x, y)
```

## 4. DFS/BFS

BFS와 DFS는 그래프를 탐색하는 방법에 가장 많이 사용되는 알고리즘입니다. 여기서 그래프란, 정점과 그 정점을 연결하는 간선으로 이루어진 자료구조의 일종을 말하며 그래프를 탐색하는 것은 하나의 정점으로부터 시작하여 차례대로 모든 정점들을 한 번씩 방문하는 것을 말합니다.

### 1) DFS(Depth-First Search, 깊이 우선 탐색)

> 최대한 깊이 내려간 뒤, 더이상 깊이 갈 곳이 없을 경우 옆으로 이동

- 루트 노드에서 시작해서 다음 분기로 넘어가기 전에 해당 분기를 완벽하게 탐색하는 방식을 말합니다. 

1. 모든 노드를 방문하고자 하는 경우에 이 방법을 선택함
2. 깊이 우선 탐색이 너비 우선 탐색보다 좀 더 간단함
3. 검색 속도 자체는 너비 우선 탐색에 비해서 느림

#### 특징

1. 경로의 특징을 저장해야하는 문제 : 각각의 경로마다 특징을 저장해야할 경우 사용
2. 스택 또는 재귀함수로 구현
3. 검색 대상 그래프가 정말 크다면 DFS를 고려

#### 스택/큐를 활용한 DFS 구현

```
# 스택을 활용
def dfs(graph, start):
    need_visited, visited = list(), list()
    
    need_visited.append(start)
    
    while need_visited:
        node = need_visited.pop()
        
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
            
    return visited

# 큐를 활용
def dfs(graph, start):
    from collections import deque
    visited = []
    need_visited = deque()
    
    need_visited.append(start)
    
    while need_visited:
        node = need_visited.popleft()
        
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
    
    return visited
```

#### 재귀함수를 통한 DFS 구현

```
def dfs_recursive(graph, start, visited = []):
    visited.append(start)
    
    for node in graph[start]:
        if node not in visited:
            dfs_recursive(graph, node, visited)
    
    return visited
```

### 2) BFS(Breadth-First Search, 너비 우선 탐색)

> 최대한 넓게 이동한 다음, 더 이상 갈 수 없을 때 아래로 이동

- 루트 노드에서 시작해서 인접한 노드를 먼저 탐색하는 방법으로, 시작 정점으로부터 가까운 정점을 먼저 방문하고 멀리 떨어져 있는 정점을 나중에 방문하는 순회 방법입니다.
- 주로 두 노드 사이의 최단 경로를 찾고 싶을 때 이 방법을 선택합니다.

#### 특징

1. 최단 거리를 구해야하는 경우
2. 큐를 이용해서 구현

#### 기본 알고리즘 구현 

```
def bfs(graph, start):
    need_visited, visited = [], []
    need_visited.append(start)
    
    while need_visited:
        node = need_visited.pop(0)
        
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
    
    return visited
```

#### x, y를 응용하는 BFS 알고리즘 구현

- 범위가 0 <= x < M, 0 <= y < N 인 경우

```
def bfs(x, y):
    visited = []
    need_visited = []
    
    need_visited.append((x, y))
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    while need_visited:
        x_, y_ = need_visited.pop(0)
        
        for i in range(4):
            new_x_ = x_ + dx[i]
            new_y_ = y_ + dy[i]
            
            if 0 <= new_x_ < M and 0 <= new_y_ < N and (new_x_, new_y_) not in visited:
                visited.append((new_x_, new_y_))
                need_visited.append(new_x_, new_y_)
    
    return visited
```

## 5. 최단 경로

> 최단 경로 : 특정 지점까지 가장 빠르게 도달하는 방법을 찾는 알고리즘

최단 경로 알고리즘은 보통 그래프를 이용해 표현하는데 각 지점은 그래프에서 '노드'로 표현되고, 지점 간 연결된 도로는 그래프에서 '간선'으로 표현된다. 대표적으로 BFS, 다익스트라, 플로이드 워셜, 벨만 포드가 있다. (여기서는 BFS를 제외하고 설명할 예정이다.)

#### 구분하기

**간선의 가중치가 모두 같은 그래프 (Unweighted Graph)** : BFS
**간선의 가중치가 각각 다른 그래프 (Unweighted Graph)** : 다익스트라, 벨만포드(음수 가중치가 존재)
**하나의 정점에서 다른 모든 정점까지 최단 경로를 구하는 문제** : 플로이드 와샬

### 1) 다익스트라

다익스트라 알고리즘은 그래프에서 여러 개의 노드가 있을 때, 특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘이다. 다익스트라 알고리즘은 **'음의 간선'** 이 없을 때 정상적으로 작동한다. 

#### 원리

1. 출발 노드를 설정한다.
2. 최단 거리 테이블을 초기화한다.
3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다.
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.
5. 위 과정에서 3번, 4번을 반복한다.

#### 구현

```
import heapq

def dijkstra(graph, start):
    distances = {node: INF for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])
    
    while queue:
        current_distance, current_destination = heapq.heappop(queue)
        
        if distances[current_destination] < current_distance:
            continue
        
        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])
```

### 2) 벨만포드(Bellman-Ford)

한 노드에서 다른 노드까지의 최단거리를 구하는 알고리즘으로 다익스트라와 달리 벨만포드는 가중치가 음수 일 때도 사용이 가능합니다. (단, 음수가 사이클을 형성하면 사용하지 못합니다.)

#### 구현

V : 노드의 개수, E : 간선의 개수로 시작노드(src)가 1일 경우를 가정 "음의 사이클을 검토하는 과정"이 필요함

```
n(노드의 개수), m(간선의 수) = map(int, input().split())

graph = []

for i in range(m):
    u, v, w = list(map(int, input().split()))
    graph.append([u, v, w])

def BellmanFord(src):
    dist = [INF for _ in range(n+1)]
    dist[src] = 0
    
    for i in range(n-1):
        for u, v, w in graph:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    
    cycle = 0
    for u, v, w in graph:
        if dist[u] != INF and dist[u] + w < dist[v]:
            # 사이클 존재
            cycle = 1
            break
    
    if cycle == 0:
        for i in range(1, len(dist)):
            print(i, dist[i])
```

### 3) 플로이드 워셜(Floyd-Warshall)

플로이드 워셜 알고리즘은 모든 정점 사이의 최단 경로를 찾는 탐색 알고리즘으로 최단 경로는 길이 순으로 구해집니다. 

#### 과정

1. 하나의 정점에서 다른 정점으로 바로 갈 수 있으면 최소 비용을, 갈 수 없다면 INF로 배열에 값을 저장합니다.
2. 3중 for문을 통해 거쳐가는 정점을 설정한 후 해당 정점을 거쳐가서 비용이 줄어드는 경우에는 값을 바꿔줍니다.
3. 위 과정을 반복해 모든 정점 사이의 최단 경로를 탐색합니다.

#### 구현

```
def Floyd_Warshall(n, data):
    dist = [[INF]*n for _ in range(n)]
    
    for i, j, edge in data:
        dist[i-1][j-1] = edge
    
    for k in range(n): # 거치는 점
        dist[k][k] = 0
        for i in range(n): # 시작점
            for j in range(n): # 끝점
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

n = 4 # 정점 수
data = [[1, 3, -2], [2, 1, 4], [2, 3, 3], [3, 4, 2], [4, 2, -1]]

retsult = Floyd_Warshall(n, data)
```

## 6. 동적계획법(Dynamic Programming)

> 동적 계획법은 "어떤 문제를 풀기 위해 그 문제를 더 작은 문제의 연장선으로 생각하고, 과거에 구한 해를 활용하는" 방식의 알고리즘을 총칭한다.

#### 특징

- 분할 정복 알고리즘과 비슷하지만 "작은 문제가 중복이 일어나는지 안일어나는지"를 기준으로 분할 정복은 반복이 일어나지 않지만 동적계획법은 반복이 발생한다.
- 모든 작은 문제들은 한번만 풀어야 합니다. 따라서 정답을 구한 작은 문제를 어딘가에 메모해 놓아 큰 문제를 풀 때 작은 문제의 결과값을 이용합니다.
- 메모이제이션은 작은 문제들의 결과값을 저장해놓은 것으로 다시 사용할 수 있습니다.
- 예시로는 막대기 자르기, 최장 공통 부분 수열, 0/1 배낭이 있다.

### 예시) 최장 공통 부분 수열(LCS)

```
lcs = [[0 for _ in range(len(A) + 1)] for _ in range(len(B) + 1)]

for i in range(1, len(A) + 1):
    for j in range(1, len(B) + 1):
        if A[i-1] == B[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j])

print(lcs[len(A)][len(B)])
```

## 7. 최소 신장 트리(Minimum Spanning Tree)

신장 트리는 그래프 내에 있는 모든 정점을 연결하고 사이클이 없는 그래프를 의미합니다. N개의 정점이 있다면 신장 트리의 간선 수는 N-1개가 됩니다. 

최소 신장 트리는 각 간선이 가지고 있는 가중치의 합이 최소가 되는 신장 트리입니다. 가중치는 거리, 비용, 시간 등 여러가지로 응용할 수 있습니다.

#### 특징

1. 간선의 가중치의 합이 최소여야 한다.
2. N개의 정점을 가지는 그래프에 대해 반드시 (N-1)개의 간선만을 사용해야 한다.
3. 사이클이 포함되어서는 안된다.

#### 사례

통신망, 도로망, 유통망에서 길이, 구축 비용, 전송 시간 등을 최소로 구축하려는 경우

- 도로 건설 : 도시들을 모두 연결하면서 도로의 길이가 최소가 되도록 하는 문제
- 전기 회로 : 단자들을 모두 연결하면서 전선의 길이가 가장 최소가 되도록 하는 문제
- 통신 : 전화선의 길이가 최소가 되도록 전화 테이블 망을 구성하는 문제
- 배관 : 파이프를 모두 연결하면서 파이프의 총 길이가 최소가 되도록 연결하는 문제

### 1) Union-Find

#### Disjoint Set의 개념

- 서로 중복되지 않는 부분 집합들로 나눠진 원소들에 대한 정보를 저장하고 조작하는 자료구조
- 즉, 공통 우너소가 없는, 즉 "상호 배타적"인 부분 집합들로 나눠진 원소들에 대한 자료구조
- Disjoint Set = 서로소 집합 자료구조

#### Union-Find의 개념

- Disjoint Set을 표현할 때 사용하는 알고리즘
- 집합을 구현하는데 비트 벡터, 배열, 연결 리스트를 이용할 수 있으나 그 중 가장 효율적인 트리 구조를 이용하여 구현한다.

#### Union-Find의 연산

1. make-set(x)
    - 초기화
    - x를 유일한 원소로 하는 새로운 집합을 만든다.
2. union(x, y)
    - 합하기
    - x가 속한 집합과 y가 속한 집합을 합친다. 즉, x와 y가 속한 두 집합을 합치는 연산
3. find(x)
    - 찾기
    - x가 속한 집합의 대표값을 반환한다. 즉, x가 어떤 집합에 속해 있는지 찾는 연산

#### 구현

```
def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화하기

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# Union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력하기
print('각 원소가 속한 집합: ', end='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력하기
print('부모 테이블: ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')
```

### 2) 크루스칼 (Kruskal)

> 탐욕적인 방법을 이용하여 네트워크의 모든 정점을 최소 비용으로 연결하는 최적 해답을 구하는 것

- 탐욕적인 방법
    - 결정을 해야 할 때마다 그 순간에 가장 좋다고 생각되는 것을 선택함으로써 최종적인 해답에 도달하는 것
    - 탐욕적인 방법은 그 순간에는 최적이지만, 전체적인 관점에서 최적이라는 보장이 없기 대문에 반드시 검증해야 한다.
    - 다행히 Kruskal 알고리즘은 최적의 해답을 주는 것으로 증명되어 있다.
- MST가 1) 최소 비용의 간선으로 구성됨 2) 사이클을 포함하지 않음 의 조건에 근거하여 각 단계에서 사이클을 이루지 않는 최소 비용 간선을 선택한다.

#### 동작 과정

1. 그래프의 간선들을 가중치의 오름차순으로 정렬한다.
2. 정렬된 간선 리스트에서 순서대로 사이클을 형성하지 않는 간선을 선택한다.
    - 즉, 가장 낮은 가중치를 먼저 선택한다.
    - 사이클을 형성하는 간선을 제외한다.
3. 해당 간선을 현재의 MST 집합에 추가한다.

### 3) 프림 (Prim)

> 시작 정점에서부터 출발하여 신장트리 집합을 단계적으로 확장해나가는 방법

#### 동작 과정

1. 시작 단계에서 시작 정점만이 MST 집합에 포함된다.
2. 앞 단계에서 만들어진 MST 집합에 인접한 정점들 중에서 최소 간선으로 연결된 정점을 선택하여 트리를 확장한다. 즉, 가장 낮은 가중치를 먼저 선택한다.
3. 위의 과정을 트리가 (N-1) 개의 간선을 가질 때까지 반복한다.

#### 구현

- 프림 알고리즘은 다익스트라 알고리즘과 거의 유사하지만 프림 알고리즘은 인접 간선을 추출하여 우선 순위 큐에 삽입할 때, 순환이 발생하면 안되므로 방문한 노드인지 확인을 하고 우선순위 큐에 삽입을 합니다.

## 참고 사이트

- 정렬 알고리즘 모든 것 : https://namu.wiki/w/%EC%A0%95%EB%A0%AC%20%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98
- 선택 정렬 : https://www.daleseo.com/sort-selection/
- 삽입 정렬 : https://www.daleseo.com/sort-insertion/
- 버블 정렬 : https://www.daleseo.com/sort-bubble/
- 합병 정렬 : https://www.daleseo.com/sort-merge/
- 퀵 정렬 : https://www.daleseo.com/sort-quick/
- 그리디 알고리즘 모든 것 : https://namu.wiki/w/%EA%B7%B8%EB%A6%AC%EB%94%94%20%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98
- 활동 선택 문제 : https://yabyab2.tistory.com/102
- DFS : https://data-marketing-bk.tistory.com/44
- BFS : https://data-marketing-bk.tistory.com/45?category=901221
- 다익스트라 : https://justkode.kr/algorithm/python-dijkstra
- 벨만포드 : https://codingexplore.tistory.com/58
- 플로이드 워셜 : https://brownbears.tistory.com/560
- 최소 신장 트리 : https://gmlwjd9405.github.io/2018/08/28/algorithm-mst.html
- Union-Find : https://velog.io/@woo0_hooo/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-union-find-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98
- 크루스칼 알고리즘 : https://gmlwjd9405.github.io/2018/08/29/algorithm-kruskal-mst.html
- 프림 알고리즘 : https://gmlwjd9405.github.io/2018/08/30/algorithm-prim-mst.html
