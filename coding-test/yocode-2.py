# Plase note that external libraries, such as NumPy or Pandas
# are NOT available for this task

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# Jay 는 도시를 방문할 때마다 사진을 찍고 컴퓨터에 저장함
# 각 저장 확장자는 jpg, png, jpeg
# 기록 사진, 도시, 시간대
# 먼저, 도시로 그룹화하고 시간대별로 사진을 정렬함 - Dict 사용
# 그리고 이름을 다시 도시 + 숫자로 다시 지음 - 넣을 때 index 사용
# 목적 : 순서를 유지하면서 도시 + 숫자로 정렬함
# 사진 개수가 M

from collections import defaultdict

def solution(S):
    report = defaultdict(list)
    index = 0
    S = S.split("\n")
    for char in S:
        name, city, time = char.split(",")
        photo, extension = name.split(".")
        report[city.strip()].append((time.strip(), index, extension.strip()))
        index += 1

    result = [""] * (len(S))

    # 해당 for 문에서 걸리는 시간 O(n*(nlogn + n)) = (n**2)logn
    # M이 최대 100이니까 10000 * log100 = 10002
    for key in report.keys(): # 시간 복잡도 O(n)
        number = 1
        report[key].sort()  # 시간 복잡도 O(nlogn)
        
        length = (len(report[key]) // 10) + 1
        for time, index, extension in report[key]:  # 시간 복잡도 O(n)
            result[index] = '{0}{1}.{2}'.format(key, str(number).zfill(length), extension)
            number += 1
    
    return "\n".join(result)
    
    
