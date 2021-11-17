N = int(input())

num_list = list(map(int, input().split()))
calc_list = list(map(int, input().split()))

max_value = -1e9
min_value = 1e9

def dfs(result, idx):
    if idx == N:
        global max_value
        global min_value
        max_value = max(max_value, result)
        min_value = min(min_value, result)
        return
    for i in range(4):
        if calc_list[i] > 0:
            calc_list[i] -= 1
            if i == 0:
                dfs(result + num_list[idx], idx+1)
            elif i == 1:
                dfs(result - num_list[idx], idx+1)
            elif i == 2:
                dfs(result * num_list[idx], idx+1)
            else:
                dfs(int(result / num_list[idx]), idx+1)
            calc_list[i] += 1
    return
    
dfs(num_list[0], 1)
print(max_value)
print(min_value)