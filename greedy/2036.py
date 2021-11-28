N = int(input())

# 양수, 음수, 1을 분리
positive=[]
negative=[]
one=[]

for _ in range(N):
    num = int(input())
    if num > 1:
        positive.append(num)
    elif num <= 0:
        negative.append(num)
    else:
        one.append(num)

# 그리디 탐색에 맞게 양수는 내림차순, 음수는 오름차순으로 정렬
positive.sort(reverse=True)
negative.sort()

# 결과
result = 0

# 양수 리스트 입력
if len(positive) % 2 == 0:
    for i in range(0,len(positive),2):
        result += positive[i] * positive[i+1]
else:
    for i in range(0,len(positive)-1,2):
        result += positive[i] * positive[i+1]
    result += positive[len(positive)-1]

# 음수 리스트 입력
if len(negative) % 2 == 0:
    for i in range(0,len(negative),2):
        result += negative[i] * negative[i+1]
else:
    for i in range(0,len(negative)-1,2):
        result += negative[i] * negative[i+1]
    result += negative[len(negative)-1]

result += sum(one)

print(result)