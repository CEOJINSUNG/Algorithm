# 효빈이에게 이모티콘을 S 개 보내려고 함
# 화면에 이모티콘 1개를 입력함 
# 1. 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장
# 2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기
# 3. 화면에 있는 이모티콘 중 하나를 삭제

from collections import deque

s = int(input())

visited = [[0] * 1001 for _ in range(1001)]

q = deque()
q.append((1, 0))

while q:
    screen, clip = q.popleft()

    if screen == s:
        print(visited[screen][clip])
        break
        
    if visited[screen][screen] == 0: 
        q.append((screen, screen))
        visited[screen][screen] = visited[screen][clip] + 1
        
    if screen + clip <= s and visited[screen + clip][clip] == 0:
        q.append((screen + clip, clip))
        visited[screen + clip][clip] = visited[screen][clip] + 1
        
    if screen - 1 >= 0 and visited[screen - 1][clip] == 0:
        q.append((screen - 1, clip))
        visited[screen - 1][clip] = visited[screen][clip] + 1