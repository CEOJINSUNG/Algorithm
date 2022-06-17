# 3 + 9 + 27
def solution(n):
    answer_list = [''] * 500000000
    answer_list[0] = '1'
    answer_list[1] = '2'
    answer_list[2] = '4'
    repeat = 3
    if n < 3:
        return answer_list[n-1]
    
    case = 0
    for i in range(3, n):
        if case == repeat:
            case = 0
        else:
            answer_list[i] = answer_list[i-repeat]
    return answer_list[n-1]

num = int(input())
print(solution(num))

# 0 3 6 
# 1 4 7
# 2 5 8
# 3 6 9