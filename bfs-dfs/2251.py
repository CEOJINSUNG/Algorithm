import sys

a, b, c = map(int, sys.stdin.readline().split())

result = []
status = []
q = [(0, 0, c)]

while q:
    first, second, third = q.pop(0)

    if first == 0 and third not in result:
        result.append(third)

    if (first, second, third) not in status:
        status.append((first, second, third))
        # a exists
        if first != 0:
            # a->b
            if (b-second) <= first:
                q.append((first - (b-second), b, third))
            else:
                q.append((0, second+first, third))
            
            # a->c
            if (c-third) <= first:
                q.append((first-(c-third), second, c))
            else:
                q.append((0, second, third+first))
        
        # b exists
        if second != 0:
            # b->a
            if (a-first) <= second:
                q.append((a, second-(a-first), third))
            else:
                q.append((first+second, 0, third))
            
            # b->c
            if (c-third) <= second:
                q.append((first, second-(c-third), c))
            else:
                q.append((first, 0, third+second))
        
        # c exists
        if third != 0:
            # c->a
            if (a-first) <= third:
                q.append((a, second, third-(a-first)))
            else:
                q.append((first+third, second, 0))
            
            # c->b
            if (b-second) <= third:
                q.append((first, b, third-(b-second)))
            else:
                q.append((first, second + third, 0))

print(*sorted(result))