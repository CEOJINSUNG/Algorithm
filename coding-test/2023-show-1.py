# 목적 : 연속한 몇 개의 돌상에 금칠
# 조건 1 : 신을 모시는사당 돌 N 개가 존재
# 조건 2 : 궁극의 깨달음을 얻기 위해서는 가능한 한 많은 금색 돌상들이 같은 방향
# 조건 3 : | (왼쪽을 바라보는 금색 돌상의 개수) - (오른쪽을 바라보는 금색 돌상의 개수) |
# 조건 4 : 돌상의 개수는 1개 이상 100,000개 이하
# 조건 5 : 왼쪽은 1, 오른쪽은 2

n = int(input())
stones = list(map(int, input().split()))

dp_left = [0] * (n + 1)
dp_right = [0] * (n + 1)

# 점화식
# 특정 범위에서 돌상의 차이가 최대가 되는 경우
# 1과 2의 개수 차이가 최대가 되는 경우

def maximum_value(dp, leftOrRight):
    for i in range(1, n + 1):
        stone = 1 if stones[i - 1] == leftOrRight else -1
        if (dp[i-1] + stone) > stone:
            dp[i] = dp[i-1] + stone
        else:
            dp[i] = stone
    return dp

# 1. 돌상의 개수가 1개인 경우
if n == 1:
    print(1)
# 2. 돌상의 개수가 2개 이상인 경우
else:
    dp_left = maximum_value(dp_left, 1)
    dp_right = maximum_value(dp_right, 2)
    left, right = max(dp_left), max(dp_right)
    print(max(left, right))