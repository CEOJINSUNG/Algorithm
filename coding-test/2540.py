# 받은 괄호를 리스트에 집어넣음
string_input = input()

# 초기 스택 배열 생성
stack = []

# 점수 받기
score = 0

# 곱하기가 있는 경우
case = 1

# 생성한 스택 배열에 받은 괄호를 집어넣기
for i in range(len(string_input)):
    stack.append(string_input[i])
    if string_input[0] == "]" or string_input[0] == ")":
        score = 0
        break
    
    elif len(stack) >= 2 :
        print(stack)
        if stack[-1] == "]" and stack[-2] == "[":
            del stack[-2:]
        if stack[-1] == ")" and stack[-2] == "(":
            del stack[-2:]
        if stack[-1] == "[" and stack[-2] == "[":
        if stack[-1] == "]" and stack[-2] == "]":
        if stack[-1] == "(" and stack[-2] == "(":
        if stack[-1] == ")" and stack[-2] == ")":
        if stack[-1] == "[" and stack[-2] == ")":
        if stack[-1] == "(" and stack[-2] == "]":

print(score)


# (
# (() => +2
# ([[] => +3
# ([] => 3 * 3
# 