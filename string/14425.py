n, m = map(int, input().split())
n_str = set([input() for _ in range(n)])

answer = 0
for _ in range(m):
    m_str = input()
    if m_str in n_str:
        answer += 1

print(answer)