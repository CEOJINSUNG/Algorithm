# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# a와 b 로 이루어진 S가 있을 때
# a가 왼쪽에만 있으면 True
# a 사이에 b가 있으면 False
# 시간 복잡도 현재 N + N

def solution(S):
    b_exist = False

    for char in S:
        # b가 존재하면 true로 바꿈
        if char == 'b':
            b_exist = True
        elif b_exist and char == 'a': # b가 존재하는 걸 알고나서 a를 발견한 경우 False
            return False
    return True

    # 다른 풀이
    # # b가 아예 없으면
    # set_S = set(list(S))
    # if 'b' not in set_S or 'a' not in set_S:
    #     return True
    
    # # b를 처음 발견한 곳
    # left = S.index('b')
    # right = len(S)

    # if 'a' not in set(list(S[left:right])):
    #     return True
    # return False