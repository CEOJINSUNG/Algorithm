number = 0
while True:
    number += 1
    string = input()
    if string[0] == '-':
        break
    stack = []
    
    for char in string:
        if char == "{":
            stack.append(char)
        elif char == "}":
            if len(stack) > 0 and stack[-1] == "{":
                stack.pop()
            else:
                stack.append(char)
    
    count = 0
    if len(stack) == 0:
        print('{0}. {1}'.format(number, count))
        continue
    
    element = []
    length = len(stack)
    for char in stack:
        if len(element) > 0 and element[-1] == char:
            element.pop()
            count += 1
        else:
            if len(element) > 0 and char == "}" and element[-1] == "{":
                element.pop()
            else:
                element.append(char)
    
    if len(element) == 0:
        print('{0}. {1}'.format(number, count))
    else:
        print('{0}. {1}'.format(number, count + len(element)))
    