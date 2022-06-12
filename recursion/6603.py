from itertools import combinations
import sys
input = sys.stdin.readline

while True:
    test = list(map(int, input().split()))
    if test[0] == 0:
        break
    del test[0]

    for i in combinations(test, 6):
        print(*i)
    
    print()