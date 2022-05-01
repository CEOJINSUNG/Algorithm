from collections import deque
import sys

operators = set(['*', '/', '+', '-'])

def priority(operator):
    if operator == "*" or operator == "/":
        return 2
    else:
        return 1

def operator_compare(x, y):
    a = priority(x)
    b = priority(y)

    if a >= b:
        return True
    else:
        return False

def calculate(int1, express, int2):
    if express == "*":
        return int1 * int2
    
    if express == "/":
        return int(int1 / int2)
    
    if express == "+":
        return int1 + int2
    
    if express == "-":
        return int1 - int2

expression = sys.stdin.readline().strip()
q = deque([])

temp = ""
for i in expression:
    if i in operators:
        if len(temp) > 0: q.append(int(temp))
        q.append(i)
        temp = ""
    else:
        temp += i
q.append(int(temp))

if q[0] == '-':
    q.popleft()
    q[0] *= (-1)

while True:
    length = len(q)
    if len(q) == 1:
        print(q[0])
        break

    # 곱셈, 나눗셈을 덧셈, 뺄셈보다 더 먼저 계산한다.
    front_operator = priority(q[1])
    back_operator = priority(q[-2])

    temp = 0
    if front_operator > back_operator:
        temp = calculate(q[0], q[1], q[2])
        q.popleft()
        q.popleft()
        q.popleft()
        q.appendleft(temp)
    elif back_operator > front_operator:
        temp = calculate(q[-3], q[-2], q[-1])
        q.pop()
        q.pop()
        q.pop()
        q.append(temp)
    else:
        front = calculate(q[0], q[1], q[2])
        back = calculate(q[-3], q[-2], q[-1])

        if front >= back:
            temp = front
            q.popleft()
            q.popleft()
            q.popleft()
            q.appendleft(temp)
        else:
            temp = back
            q.pop()
            q.pop()
            q.pop()
            q.append(temp)

