n, m = map(int, input().split())

disease = []
for _ in range(m):
    r, b, d = map(int, input().split())
    disease.append([r, b, d])

student = []
for _ in range(n):
    r, b = map(int, input().split())
    student.append([r, b])

def solution(person):
    dp = [[0] * (m+1) for _ in range(m+1)]