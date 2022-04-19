import sys
n = int(sys.stdin.readline())

deck = {"left": 0, "middle": 27, "right":0 }
joker = {"left": 0, "middle": 1, "right": 0}

def shuffle_deck():
    if joker["middle"] <= 13:
        joker["left"] = joker["middle"]
        joker["middle"] = 0
    else:
        joker["right"] = joker["middle"] - 13
        joker["middle"] = 0

    deck["left"] = 13
    deck["middle"] = 0
    deck["right"] = 14

def odd(count):
    # 오른쪽에 조커 존재하지 않음
    if joker["right"] == 0:
        deck["middle"] += count
    
    # 오른쪽에 조커 존재함
    else:
        # 조커 위치보다 작은 곳에서 가져감
        if count < joker["right"]:
            deck["middle"] += count
        # 조커 위치보다 큰 곳에서 가져감
        else:
            joker["middle"] = deck["middle"] + joker["right"]
            joker["right"] = 0
            deck["middle"] += count

def even(count):
    # 왼쪽에 조커 존재하지 않음
    if joker["left"] == 0:
        deck["middle"] += count
    
    # 왼쪽에 조커 존재함
    else:
        # 조커 위치보다 작은 곳에서 가져감
        if count < joker["left"]:
            deck["middle"] += count
        # 조커 위치보다 큰 곳에서 가져감
        else:
            joker["middle"] = deck["middle"] + joker["left"]
            joker["left"] = 0
            deck["middle"] += count

for _ in range(n):
    shuffle_deck()

    array = list(map(int, sys.stdin.readline().split()))
    
    # 오른쪽 덱의 맨 위에서 Ai1장을 가져와서 새로운 덱의 맨 위에 배치한다.
    count = array[0]

    if joker["right"] != 0:
        if count < joker["right"]:
            deck["middle"] = count
            deck["right"] -= count
            joker["right"] -= count
        else:
            deck["middle"] = count
            deck["right"] -= count
            joker["middle"] = joker["right"]
            joker["right"] = 0

    else:
        deck["middle"] = count
        deck["right"] -= count
    
    for j in range(1, len(array)):
        # 오른쪽
        if j%2 == 0:
            odd(array[j])
        # 왼쪽
        else:
            even(array[j])

print(joker["middle"])