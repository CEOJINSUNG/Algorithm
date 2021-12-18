n, c = map(int, input().split())

unsorted_list=[]
sorted_list=[]

# [divide]
# 리스트 요소가 1개가 될때까지 나눔 / 왼쪽,오른쪽 merge
def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    leftList = list[:mid]
    rightList = list[mid:]
    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)
    return merge(leftList, rightList)

# [merge]
#1. 분리한 왼쪽리스트, 오른쪽 리스트의 각각 첫번째 요소를 비교해 더 작은 값을 결과 리스트에 저장
#2. 저장한 값은 리스트에서 지움. 
#3. 두 리스트 모두 요소가 하나도 안남을 때까지 반복
def merge(left, right):
    merged_list = []
    l=h=0

    while l < len(left) and h < len(right):
        if (left[l] < right[h]):
            merged_list.append(left[l])
            l+=1
        else:
            merged_list.append(right[h])
            h+=1
    merged_list += left[l:]
    merged_list += right[h:]
    return merged_list

for i in range(n):
    num=int(input())
    unsorted_list.append(num)

sorted_list=merge_sort(unsorted_list)
distance = []


for i in range(1, len(sorted_list)):
    if sorted_list[i] - sorted_list[i-1] > 1:
        distance.append(sorted_list[i] - sorted_list[i-1])

print(min(distance))