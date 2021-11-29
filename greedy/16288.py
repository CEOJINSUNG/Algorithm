# 승객 및 창구
N, k = map(int, input().split())

# 입국장을 빠져나가는 순서
answer = list(map(int, input().split()))

# 창구 순서 저장
graph = [[101] for _ in range(k)]

final = ""

# 각 순서를 거꾸로 해서 집어 넣음
for i in reversed(answer):
    final = "NO"
    # 항상 모든 창구에 숫자가 들어갈 때는 이전에 들어갔던 숫자보다 크면 안된다.
    for j in range(k):
        if i < graph[j][0]:
            final = "YES"
            graph[j].insert(0, i)
            break
    if final == "NO":
        break

if final == "NO":
    print("NO")
else:
    print("YES")