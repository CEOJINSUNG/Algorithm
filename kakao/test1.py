def solution(x, y, z):
    # Write your code here
    dist = abs(x - y)
    differ = z - dist
    if dist > z:
        return -1
    elif x == y:
        return z // 2 + x
    elif x > y:
        return x + differ // 2
    else:
        return y + differ // 2