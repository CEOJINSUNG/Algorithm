# 목적 : 악수를 할 경우 가능한 만족도의 합의 최대값
# 조건 1 : A대학의 학생 N명과 B대학의 학생 M명
# 조건 2 : 의자에 앉을 때는 번호가 증가하는 순서대로 앉는다.
# 조건 3 : 한 사람은 최대 한 사람과 악수
# 조건 4 : 팔이 교차하면 악수를 할 때 불편하기 때문에, 팔이 교차하지 않게 악수
# 조건 5 : 학생의 성격을 1 이상, C 이하의 정수
# 조건 6 : 성격이 a인 사람과 b인 사람이 악수를 할 경우, W[a][b]만큼의 만족도

n, m, c = map(int, input().split())
w = [[0] * (c + 1) for _ in range(c + 1)]

for i in range(1, c+1):
    personality = list(map(int, input().split()))
    for index, value in enumerate(personality):
        w[i][index + 1] = w[index + 1][i] = value

a_university = [0] + list(map(int, input().split()))
b_university = [0] + list(map(int, input().split()))

handshake_satisfaction = [[0] * (m + 1) for _ in range(n + 1)]

for n_index in range(1, n + 1):
    for m_index in range(1, m + 1):
        handshake_satisfaction[n_index][m_index] = w[a_university[n_index]][b_university[m_index]]

# dp로 가장 증가하는 수열 느낌으로 값을 저장할 수 있을 것 같다. 
# dp가 아래와 같이 있다고 하자.
# 0 1 8 10
# 0 0 0 0
# dp[1][1]은 0이다. 왜냐하면 dp[1][1] = max(dp[0][0] + handshake_satisfaction[1][1], dp[1][0]) 이기 때문이다.
# dp[1][2] = max(dp[0][1] + handshake_satisfaction[1][2], dp[1][1]) 이다.
# dp[1][2]에서 dp[0][2]는 이미 악수를 하고 있기 때문에 교차될 수도 겹칠 수도 없어서 비교 대상이 될 수 없다. 

dp = [[0] * (m + 1) for _ in range(n + 1)]
for row in range(n):
    for col in range(m):
        dp[row + 1][col + 1] = max(dp[row][col] + handshake_satisfaction[row + 1][col + 1], dp[row + 1][col], dp[row][col + 1])

print(dp[n][m])

print("\n===== 성격 =====")
for row in w:
    print(row)

print("\n===== 나올 수 있는 성격 조합 =====")
for row in handshake_satisfaction:
    print(row)

print("\n===== 각 선택의 결과 =====")
for row in dp:
    print(row)

print("\n===== 최종 정답 =====")
print(dp[n][m])