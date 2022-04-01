from collections import deque
import sys
input = sys.stdin.readline

# test means the number of test cases
test = int(input())

for _ in range(test):
    # command sequential
    command = list(input())

    # n means a length of array
    n = int(input())

    # when array input only add integer
    array = deque(input()[1:-2].split(','))

    # if error happens, stop the command
    error = False

    # reverse means initial position of queue
    reverse = 0

    for i in command:
        if i == 'R':
            array.reverse()
        else:
            if array:
                array.popleft()
            else:
                print("error")
                error = True
                break
    
    if error == False:
        print("[" + ",".join(array) + "]")