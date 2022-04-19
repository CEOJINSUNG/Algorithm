n, m = map(int, input().split())

bridge = []

for _ in range(n):
    bridge.append(list(map(int, input().split())))

for col in range(n-2, -1, -1):
    for row in range(m):
        if bridge[col][row] != 0:
            whether = 0

            previous_col = col + 1
            left_row = row - 1
            middle_row = row
            right_row = row + 1

            left = 0
            middle = bridge[previous_col][middle_row]

            if middle != 0:
                whether += 1
            
            right = 0

            if 0 <= left_row:
                left = bridge[previous_col][left_row]
                if left != 0:
                    whether += 1
            
            if right_row < m:
                right = bridge[previous_col][right_row]
                if right != 0:
                    whether += 1
            
            if whether == 0:
                bridge[col][row] = 0
            elif whether == 1:
                bridge[col][row] = max(left, middle, right)%1000000007
            else:
                bridge[col][row] = (left + middle + right)%1000000007

print(sum(bridge[0])%1000000007)