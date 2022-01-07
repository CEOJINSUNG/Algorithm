N, M = map(int, input().split())

descarte = []
for _ in range(N):
    position = list(map(int, input().split()))
    descarte.append(position)

score = []
tetrominos = [
    [(0, 0), (0, 1), (1, 0), (1, 1)],
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 0), (0, 1), (0, 2), (1, 0)],
    [(0, 0), (0, 1), (0, 2), (-1, 2)],
    [(0, 0), (1, 0), (1, 1), (1, 2)],
    [(0, 0), (0, 1), (0, 2), (1, 2)],
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (1, 0), (2, 0)],
    [(0, 0), (1, 0), (2, 0), (2, -1)],
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (1, 0), (-1, 1)],
    [(0, 0), (0, 1), (1, 0), (1, -1)],
    [(0, 0), (0, 1), (1, 1), (1, 2)],
    [(0, 0), (0, 1), (0, 2), (1, 1)],
    [(0, 0), (1, 0), (1, 1), (1, -1)],
    [(0, 0), (1, 0), (2, 0), (1, -1)],
    [(0, 0), (1, 0), (1, 1), (2, 0)]
]

for i in range(N):
    for j in range(M):
        for tetro in tetrominos:
            amount = 0
            for x, y in tetro:
                try:
                    amount += descarte[i+x][j+y]
                except IndexError:
                    break
            score.append(amount)

print(max(score))