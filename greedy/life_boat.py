def solution(people, limit):
    answer = 0
    people.sort()
    first = 0
    last = len(people) - 1
    
    while True:
        if last == first:
            answer += 1
            break
        if last < first:
            break
        
        # 2명 타는 경우
        if people[first] + people[last] <=limit:
            answer += 1
            first += 1
            last -= 1
        # 1명 타는 경우
        else:
            last -= 1
            answer += 1
    
    return answer
