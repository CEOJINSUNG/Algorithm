array = [4, 3, 2, 7, 8, 2, 3, 1]
long_array = [4, 3, 2, 7, 8, 2, 3, 1] * 100

# 완전 탐색
def find_duplicates(array)
    current_num = array[0]
    result_array = []
    
    array.count.times do |i|
        array.count.times do |j|
            # next는 python의 continue와 같음
            next if i == j || current_num != array[j]

            result_array.push(current_num)
        end

        current_num = array[i+1]
    end
    # uniq는 배열에서 중복된 요소들을 전부 제거해 반환
    result_array.uniq
end

print(find_duplicates(array))
print(find_duplicates(long_array))

def find_duplicates(array)
    sorted_array = array.sort
    result_array = []

    (1..sorted_array.count).each do |i|
        next if sorted_array[i] != sorted_array[i-1]

        result_array.push(sorted_array[i])
    end

    result_array.uniq
end

print(find_duplicates(array))
print(find_duplicates(long_array))