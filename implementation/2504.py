bracket = input()
length = len(bracket)

index = 1
stack = [bracket[0]]
while index < length:
    stack.append(bracket[index])

    # print(stack)
    if len(stack) >= 2 and stack[-2] == "(" and stack[-1] == ")":
        stack = stack[:-2]
        stack.append(2)
    
    if len(stack) >= 2 and stack[-2] == "[" and stack[-1] == "]":
        stack = stack[:-2]
        stack.append(3)
    
    if len(stack) >= 3:
        one = stack[-3]
        two = stack[-2]
        three = stack[-1]

        if one == "[" and str(two).isdigit() and three == "]":
            stack = stack[:-3]
            stack.append(3*two)

            if len(stack) >= 2 and str(stack[-2]).isdigit() and str(stack[-1]).isdigit():
                first = stack.pop(-2)
                second = stack.pop(-1)
                stack.append(first + second)
        
        if one == "(" and str(two).isdigit() and three == ")":
            stack = stack[:-3]
            stack.append(2*int(two))

            if len(stack) >= 2 and str(stack[-2]).isdigit() and str(stack[-1]).isdigit():
                first = stack.pop(-2)
                second = stack.pop(-1)
                stack.append(first + second)
    
    if len(stack) >= 2 and str(stack[-2]).isdigit() and str(stack[-1]).isdigit():
        first = stack.pop(-2)
        second = stack.pop(-1)
        stack.append(first + second)
    
    index += 1

if len(stack) == 1 and str(stack[0]).isdigit():
    print(stack[0])
else:
    print(0)