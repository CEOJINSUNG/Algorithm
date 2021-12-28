def solution(routes):
    answer = 1
    # 내림차순으로 정렬
    routes.sort(key=lambda x:x[0], reverse=True)
    
    now = routes[0][0]
    for i in routes[1:]:
        # 겹칠 경우
        if i[1] >= now:
            continue
        # 겹치지 않을 경우
        else:
            now = i[0]
            answer += 1
    
    return answer