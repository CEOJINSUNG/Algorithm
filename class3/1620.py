N, M = map(int, input().split())

pocket = {}
pocketmon = {}

for i in range(1, N+1):
    monster = input()
    pocket[i] = monster
    pocketmon[monster] = i

for _ in range(M):
    question = input()
    if question.isalpha():
        print(pocketmon[question])
    else:
        print(pocket[int(question)])