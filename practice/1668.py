# 민식이 트로피 많음
# 뒤 트로피가 앞의 트로피에 가려져 있음
# 왼쪽에서 보이는 개수 오른쪽에서 보이는 개수

n = int(input())
trophies = [int(input()) for _ in range(n)]

def find_count(start, end, reverse = 1):
    count, h = 1, trophies[start]
    for i in range(start + reverse, end, reverse):
        if h < trophies[i]:
            count += 1
            h = trophies[i]
    return count

left = find_count(0, n)
right = find_count(n - 1, -1, -1)

print(left, right)