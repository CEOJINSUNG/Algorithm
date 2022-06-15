n = int(input())
array = [0] + list(map(int, input().split()))

memory = [(-int(1e9)-1)]
for num in array[1:]:
    if memory[-1] < num:
        memory.append(num)
    else:
        start = 0
        end = len(memory)

        while start < end:
            mid = (start + end) // 2

            if memory[mid] < num:
                start = mid + 1
            else:
                end = mid
        
        memory[end] = num

print(len(memory) - 1)